import os
import yaml 
import logging
import time
import pandas as pd  
import json 

def read_yaml(path_to_yaml: str) ->dict:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
    logging.info(f"yaml file: {path_to_yaml} loaded successfully")
    return content

def create_directories(path_to_directories: list) -> None:
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        logging.info(f"Created directory at: {path}")
    