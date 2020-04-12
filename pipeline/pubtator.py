__author__ = 'awakenedhaki'

# DOCS
# . Formats:
# . . pubtator
# . . biocxml
# . . biocjson

# . Types:
# . . pmids (abstracts)
# . . pmcids (full text)

# . Identifiers: the PMIDS or PMCIDS

# . Concepts (only biocxml or pubtator):
# . . gene
# . . disease
# . . chemical
# . . species
# . . mutation
# . . cellline.

# DEPENDENCIES
import requests

from uritemplate import URITemplate

# CONSTANTS
# URL = 'https://www.ncbi.nlm.nih.gov/research/pubtator-api/publications/export/[Format]?[Type]=[Identifiers]&concepts=[Bioconcepts]'
BASE = URITemplate('https://www.ncbi.nlm.nih.gov/research/pubtator-api/publications/export/{format}')

# FUNCTIONS
class PubTator(object):
    def __init__(self, format):
        if format not in ('pubtator', 'biocxml', 'biocjson'):
            raise ValueError('Invalid PubTator format.')
        self.URL = BASE.expand({'format': format})

    def get(self, **params):
        with requests.get(BASE, params = params) as resp:
            return resp.content

if __name__ == '__main__':
    pubtator = PubTator('biocjson')
    print(pubtator.get(pmids = '23819905'))