import unittest
from unittest.mock import patch, mock_open
from  src.bioModels_cache import remove_html_tags, update_cache, save_to_json, cache_biomodels 

class TestBioModelsCache(unittest.TestCase):

    def test_remove_html_tags(self):
        self.assertEqual(remove_html_tags("<p>BIOMD007</p>"), "BIOMD007")
        self.assertEqual(remove_html_tags("Remove"), "Remove")
        self.assertEqual(remove_html_tags(""), "")

    def test_update_cache_existing_model(self):
        model = {'publicationId': 'BIOMD007', 'description': 'Test'}
        modelResults = {'BIOMD007': model}
        self.assertFalse(update_cache(model, modelResults))

    @patch('builtins.open', new_callable=mock_open)
    def test_save_to_json(self, mock_file_open):
        model_info = {'BIOMD007': {'description': 'Description of BioModel 7'}}
        save_to_json(model_info)


if __name__ == '__main__':
    unittest.main()