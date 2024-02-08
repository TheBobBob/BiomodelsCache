import unittest
from unittest.mock import patch, mock_open
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from BioModelsCache import BioModelsCache
cache = BioModelsCache()


class TestBioModelsCache(unittest.TestCase):

    def test_remove_html_tags(self):
        self.assertEqual(cache.remove_html_tags("<p>BIOMD007</p>"), "BIOMD007")
        self.assertEqual(cache.remove_html_tags("Remove"), "Remove")
        self.assertEqual(cache.remove_html_tags(""), "")

    def test_update_cache_1(self):
        model = {'publicationId': 'BIOMD007', 'description': 'description of BIOMD007'}
        self.assertFalse(cache.update_cache(model, 'BIOMD007'))

    def test_update_cache_2(self):
        model = {'publicationId': 'BIOMD008', 'description': 'description of BIOMD008', 
                 'publication': {'authors': [{'name': 'author1'}, {'name': 'author2'}], 
                                 'link': 'link', 'title': 'title', 'synopsis': 'synopsis'}}
        self.assertTrue(cache.update_cache(model, 'BIOMD008'))

    def test_search_models_1(self):
        self.assertEqual(cache.search_models('BIOMD007'), [])
    
    def test_search_models_2(self):
        self.assertEqual(cache.search_models('BIOMD0000000249'), ['BIOMD0000000249'])

if __name__ == '__main__':
    unittest.main()