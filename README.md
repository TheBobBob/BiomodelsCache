# BiomodelsCache
A biomodels cache for faster lookup of BioModels [https://www.ebi.ac.uk/biomodels/] information. It can be used with the [BiomodelsStore repo](https://github.com/sys-bio/BiomodelsStore) for faster search and model download compared to using the REST API at Biomodels (https://www.ebi.ac.uk/biomodels/docs/). This model database is stored in json format (`../src/cached_biomodels.json`) and currently contains the following fields:
- Biomodel ID
- Model name
- SBML model file name
- Published paper title
- Authors
- Citations
- Date published
- Journal paper published in.

Note: Other fields can be added as neccessary or requested. This database is updated once a month. 

See https://github.com/sys-bio/BiomodelsStore for cached SBML models from Biomodels.

## Using the Biomodels cache
The model database can be accessed by any coding language that supports JSON and can make calls to GitHub. Currently we have a JavaScript client that makes the interaction straightforward. The file is at **`../src/searchClient/getBiomodels.js`**. Using this JavaScript client requires only one function call to get model information:

- `const searchResults = await searchModels(searchTerms);`

This function takes in a string that contains the search terms separated by a space `' '` and returns model information of all the curated models that match the search.

Once you have the BioModel ID of the model you are interested in you can then download the model using this call:
- `const model_text = await getModel(modelID);`

This takes a string corresponding to the model ID (ex: `"BIOMD0000000002"`) and returns the SBML model as a string. This function calls the [BiomodelsStore repo](https://github.com/sys-bio/BiomodelsStore) to get the SBML model code.

## Example usage
- A simple HTML/js webpage that uses the JavaScript client is here: [https://github.com/sys-bio/BiomodelsCache/tree/main/examples]. See `example_usage.js` for the actual calls to the JavaScript client and BioModels cache.
- A more developed application is [MakeSBML](https://sys-bio.github.io/makesbml/) which translates Antimony to SBML and vice-versa.

