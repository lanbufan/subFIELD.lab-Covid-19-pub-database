__author__ = 'awakenedhaki'

# DEPENDENCIES
import json
import requests

from tqdm import tqdm
from time import sleep
from litcovid import LOGGER, LITCOVID
from requests.exceptions import HTTPError

# CONSTANTS
URL = 'https://www.ncbi.nlm.nih.gov/research/coronavirus-api/publication/%s'

# FUNCTIONS
def scrape_litcovid(*pmids):
    for pmid in tqdm(pmids):
        with requests.get(URL % pmid) as r:
            try:
                r.raise_for_status()
                yield r.json()
            except HTTPError as e:
                LOGGER.exception(e)
        sleep(2)