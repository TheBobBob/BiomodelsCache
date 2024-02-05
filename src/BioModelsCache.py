import json
from biomodels_restful_api_client import services as bmservices
import re
import argparse


class BioModelsCache:
    def __init__(self, total_models=2000):
        self.total_models = total_models
        self.modelResults = {}

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
    

    def update_cache(self, model):
        """
        Update the cache with the model data if it's not already present.

        Parameters:
        1. model: A dictionary representing the model data to be cached.

        Returns:
            bool: Returns True if the cache was updated with the model, False if it is not a BioModel or if the Biomodel
            is already in the cache.
        """
        model_id = model['publicationId']
        if model_id not in self.modelResults or self.modelResults[model_id] != model:
            self.modelResults[model_id] = {
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

        for nModel in models:
            if i < self.total_models:
                result = bmservices.get_model_info(nModel)
                if 'publicationId' in result:
                    updated_cache = self.update_cache(result)
                    if updated_cache:
                        i += 1

        self.save_to_json()

    def save_to_json(self):
        """Saves the cached biomodel to the JSON file."""
        with open('cached_biomodels.json', 'w') as json_file:
            json.dump(self.modelResults, json_file)


def main():
    parser = argparse.ArgumentParser(description='Cache BioModels data.')
    parser.add_argument('--total', type=int, default=2000,
                        help='Total number of models to cache (default: 2000)')
    args = parser.parse_args()

    cache = BioModelsCache(total_models=args.total)
    cache.cache_biomodels()

if __name__ == '__main__':
    main()
