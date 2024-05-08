# Need following packages installed:
# pip install biomodels-restful-api-client 
# Ref: https://bitbucket.org/biomodels/biomodels-resftful-api-client/src/main/
# pip install PyGithub

import json
from biomodels_restful_api_client import services as bmservices
import re
import argparse
import time
from github import Github

class BioModelsCache:
    def __init__(self, total_models=2000):
        self.total_models = total_models
        self.model_results = {}

    def remove_html_tags(self, text):
        """
        Removes HTML tags from a string.
        Parameters:
        1. text: A string of text with HTML tags that must be removed.

        Returns:
        str: The input string with all HTML tags removed.
        """
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)
    
    def extract_urls(self, text):
        """
        Extracts URLs from anchor tags (<a href="...">) in a string.

        Parameters:
        1. text: A string of text with anchor tags.

        Returns:
        list: A list of URLs extracted from anchor tags.
        """
        pattern = re.compile(r'<a href="([^"]*)">')
        urls = pattern.findall(text)
        return urls 
    

    def update_cache(self, model, model_id):
        """
        Update the cache with the model data if it's not already present.

        Parameters:
        1. model: A dictionary representing the model data to be cached.

        Returns:
            bool: Returns True if the cache was updated with the model, False if it is not a BioModel or if the Biomodel
            is already in the cache.
        """
        if 'publication' not in model:
            return False
        if model_id not in self.model_results or self.model_results[model_id] != model:
            self.model_results[model_id] = {
                'name': model.get('name', ''),
                'authors': [author.get('name') for author in model.get('publication').get('authors', [])],
                'url': model.get('publication').get('link', ''),
                'model_id': model_id,
                'title': model.get('publication').get('title', ''),
                'synopsis': model.get('publication').get('synopsis', '')
            }
            return True
        return False

    def cache_biomodels(self):
        """Fetch and cache information for a set number of BioModels."""
        i = 0
        modelIdentifiers = bmservices.get_model_identifiers()
        models = modelIdentifiers["models"]

        for n_model in models:
            result = bmservices.get_model_info(n_model)
            updated_cache = self.update_cache(result, n_model)
            if updated_cache:
                i += 1
                #print(i)

        self.save_to_json()

    def save_to_json(self):
        """Saves the cached biomodel to the JSON file."""
        with open('cached_biomodels.json', 'w') as json_file:
            json.dump(self.model_results, json_file)
    
    def search_models(self, search):
        """Search the cache and return list of search results."""
        with open('cached_biomodels.json', 'r') as json_file:
            data = json.load(json_file)
        if search == "*":
            return list(data.keys())
        search_results = []
        # start_time = time.time()
        search = search.lower()

        """Search for the model in the cache. If the search
        term is found in the model ID, model name, authors, title or synopsis,
        add the model to the search results."""
        
        for model in data:
            if search in model.lower() or search in data[model]['name'].lower() or \
            search in [author.lower() for author in data[model]['authors']] or \
            search in data[model]['title'].lower() or search in data[model]['synopsis'].lower():
                search_results.append(model)
        # print("--- %s seconds ---" % (time.time() - start_time))
        # print(len(search_results))
        # print(len(data))
        return search_results

    def get_model(self, model_id):
        """Return the model data for the given model ID."""
        user = "konankisa"
        repo = "BiomodelsStore"
        repo = Github().get_user(user).get_repo(repo)
        try:
            content = repo.get_contents(f"biomodels/{model_id}.xml")
        except:
            content = None
        if content:
            with open('model.xml', 'wb') as file:
                file.write(content.decoded_content)
        else:
            raise ValueError("Model not found")

def main():
    cache = BioModelsCache()
    cache.cache_biomodels() # Update/build BioModelsCache
    cache.search_models("MODEL1903260003") # Check search()
    cache.get_model("MODEL1901090001") # Check get_model()

if __name__ == '__main__':
    main()
