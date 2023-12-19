import unittest
from unittest.mock import patch, mock_open
from  src.bioModels_cache import remove_html_tags, update_cache, save_to_json, cache_biomodels 

class TestBioModelsCache(unittest.TestCase):

    def test_remove_html_tags(self):
        self.assertEqual(remove_html_tags("<p>BIOMD007</p>"), "BIOMD007")
        self.assertEqual(remove_html_tags("Remove"), "Remove")
        self.assertEqual(remove_html_tags(""), "")

    def test_update_cache_1(self):
        model = {'publicationId': 'BIOMD007', 'description': 'description of BIOMD007'}
        modelResults = {'BIOMD007': model}
        self.assertFalse(update_cache(model, modelResults))

    def test_update_cache_2(self):
        model = {'publicationId': 'BIOMD007', 'description': 'description of BIOMD007'}
        newModel = {'publicationId': 'BIOMD008', 'description': 'description of BIOMD008'}
        self.assertTrue(update_cache(model, newModel))

    



if __name__ == '__main__':
    unittest.main()