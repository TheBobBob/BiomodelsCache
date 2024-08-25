# BiomodelsCache
A biomodels cache for faster lookup of BioModels [https://www.ebi.ac.uk/biomodels/] information. It can be used the [BiomodelsStore repo](https://github.com/sys-bio/BiomodelsStore) for faster search and model download compared to using the REST API at Biomodels (https://www.ebi.ac.uk/biomodels/docs/). This model database is stored in json format (`../src/cached_biomodels.json`) and currently contains the following fields:
- Biomodel ID
- Model name
- SBML model file name
- Published paper title
- Authors
- Citations
- Data published
- Journal paper published in.

Note: Other field can be added as neccessary or requested. 

See https://github.com/sys-bio/BiomodelsStore for cached SBML models from Biomodels.
