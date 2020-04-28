__author__ = 'awakenedhaki'

# DEPENDENCIES
import json
import requests

from tqdm import tqdm
from time import sleep
from copy import deepcopy
from random import choice
from urllib.parse import urlparse
from requests.exceptions import HTTPError
from pipeline.litcovid import LOGGER, LITCOVID
from pipeline import HEADERS, PROXIES, USER_AGENTS

# CONSTANTS
URL = 'https://www.ncbi.nlm.nih.gov/research/coronavirus-api/publication/%s?format=json'

# FUNCTIONS
def scrape_litcovid(*pmids):
    for pmid in tqdm(pmids):
        url = urlparse(URL % pmid)

        headers = deepcopy(HEADERS)
        headers['path'] = f'{url.path}?{url.query}'
        headers['user-agent'] = choice(USER_AGENTS)
        
        with requests.get(url.geturl(), headers = headers) as r:
            try:
                r.raise_for_status()
                yield r.json()
            except HTTPError as e:
                LOGGER.exception(e)

        sleep(2)