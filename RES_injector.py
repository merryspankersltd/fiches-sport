# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 16:49:46 2021

@author: marcl
"""
import pathlib
import shutil
import requests
import os
import re
from io import BytesIO
from zipfile import ZipFile
import pandas as pd
from sqlalchemy import create_engine

# DATASET_ID: dataset identifier according to datagouv
DATASET_ID = '53699ebba3a729239d205f4f'
# SOURCES_PATH: path to sources backup dir
SOURCES_PATH = pathlib.Path('J:\Etudes\laufma\20210716_RES\tmp_sources\python_raw')
# pgsql connection properties
PG_HOST = 'srv-pgdata'
PG_PORT = '5432'
PG_DATABASE = 'bdd_socle'
PG_SCHEMA = 'res_source'
# PG_USER = <fill with appropriate credentials>
# PG_PASSWORD = <fill with appropriate credentials>

def process_excel(df):
    """
    utility fct
    injects in_memory excel file using pandas and sqlalchemy"""
    
    df = pd.read_excel(df)
    
    return df
    
def process_csv(df):
    """
    utility fct
    injects in_memory csv file using pandas and sqlalchemy"""
    
    df = pd.read_csv(df)
    
    return df

def process_other(df):
    """
    utility fct
    do nothing for unknown extension"""
    
    return None

def get_resources_from_dataset(dataset_id):
    """
    retrieves resource urls from datagouv using api
    https://api.gouv.fr/les-api/api_data_gouv
    returns urls"""
    
    # get resources list from api
    dataset_url = f'https://www.data.gouv.fr/api/1/datasets/{dataset_id}/'
    res = requests.get(dataset_url).json()
    
    # download resources
    latest_resources = [
        requests.get(resource['latest']) for resource in res['resources']]
    
    return latest_resources

def dl_datafiles(resource, sources_path):
    """
    gets in_memory files, unzips if any, reads data and injects to pgsql
    returns list of datafile dicts"""
    
    # if any, unzip files recursively
    if 'application/zip' in resource.headers['Content-Type']:
        with ZipFile(BytesIO(resource.content)) as z:
            datafiles = [
                {'filename': os.path.splitext(zfile)[0],
                 'filetype': os.path.splitext(zfile)[1],
                 'content': z.read(zfile)}
                for zfile in z.namelist()]
                
    # else: populate datafiles list with 1 element (headers + response body)
    # filter out html pages
    elif 'text/html' not in resource.headers['Content-Type']:
        datafiles = [{
            'filename': os.path.splitext(resource.url.split('/')[-1])[0],
            'filetype': os.path.splitext(resource.url.split('/')[-1])[1],
            'content': resource.content}]
    
    # write to disk
    with open(SOURCES_PATH / resource.url.split('/')[-1], 'wb') as f:
        f.write(resource.content)
        
    return datafiles

def process_datafile(datafile):
    """
    switcher to map file extensions to appropriate pandas readers
    each will return a pandas df"""
    
    filetype_switcher = {
        '.xls': process_excel,
        '.xlsx': process_excel,
        '.csv': process_csv}
        
    # pgsql connexion string retrieved from fmw published parameters
    conn = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DATABASE}"
    
    # read data from buffer and injects to pgsql
    if datafile['filetype'] in filetype_switcher.keys():
        df = filetype_switcher[datafile['filetype']](datafile['content'])
        engine = create_engine(conn)
        df.to_sql(datafile["filename"], engine, schema=PG_SCHEMA) # injection
    
if __name__ == "__main__":
    
    print("main !")
    
    resources = get_resources_from_dataset(DATASET_ID)
    print('\nresources:')
    print('\n'.join([f"\t{r.url}" for r in resources]))
    
    for r in resources:
        datafiles = dl_datafiles(r, SOURCES_PATH)
        for d in datafiles:
            process_datafile(d)
        
    