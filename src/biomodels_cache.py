# Fetches BioModels that can be cached to enhance speed of searches though BioModels for 
# Sys-Bio Projects

# Install following package: 
# pip install biomodels_restful_api_client 

import json
from biomodels_restful_api_client import services as bmservices
import re

def remove_html_tags(text):
    """
    Removes html tags from a string

    Parameters:
    1. text: A string of text with HTML tags that must be removed.

    Returns:
    str: The input string with all HTML tags removed.
    """
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def update_cache(model, modelResults):
    """
    Update the cache with the model data if it's a curated BioModel and not already present.

    Parameters:
        1. model: A dictionary representing the model data to be cached.
        2. modelResults : A dictionary representing the cached models.

    Returns:
        bool: Returns True if the cache was updated with the model, False if it is not a BioModel or if the Biomodel
        is already in the cache.
    """
    modelNumber = model['publicationId']
    if "BIOMD" not in modelNumber:
        return False 
  
    if modelNumber in modelResults and modelResults[modelNumber] == model:
        return False 
    
    if "description" in model:
        model["description"] = remove_html_tags(model["description"])

    modelResults[modelNumber] = model
    return True

def cache_biomodels():
    """
    Fetch and cache information for a set number of BioModels.
    """
    totalModels = 2000
    i = 0

    modelIdentifiers = bmservices.get_model_identifiers()
    models = modelIdentifiers["models"]
    modelResults = {}

    for nModel in models:
        if i < totalModels:
            result = bmservices.get_model_info(nModel)
            if 'publicationId' in result:
              updated_cache = update_cache(result, modelResults)
              if updated_cache:
                  i += 1

    save_to_json(modelResults)


def save_to_json(modelInfo):
    """ 
    Saves the cached biomodel to the Json file.

    Parameters:
        1. modelInfo: A dictionary containing the model data to be saved to the file.
    """
    with open('cached_biomodels.json', 'w') as json_file:
        json.dump(modelInfo, json_file)
    