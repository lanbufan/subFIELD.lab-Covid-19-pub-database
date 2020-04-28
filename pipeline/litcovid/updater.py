__author__ = 'awakenedhaki'

import re
import requests
import pandas as pd

from io import StringIO
from datetime import datetime
from pipeline.litcovid import LOGGER, LITCOVID, DATE_FORMAT
from requests.exceptions import HTTPError

# CONSTANTS
LITCOVID_TSV = 'https://www.ncbi.nlm.nih.gov/research/coronavirus-api/export/tsv'
PREFACE = re.compile(r'# ={75}.*# ={74}\n', flags = re.DOTALL)
TODAY = datetime.now().strftime(DATE_FORMAT)

# FUNCTIONS
def update_litcovid_tsv():
    LOGGER.info('Updating litcovid.tsv.')
    with requests.get(LITCOVID_TSV) as resp:
        try:
            resp.raise_for_status()
            litcovid_tsv = resp.content.decode('utf-8')
            litcovid_tsv = StringIO(PREFACE.sub('', litcovid_tsv))
        except HTTPError as e:
            LOGGER.exception(e)

    updated_litcovid = pd.read_csv(litcovid_tsv, sep = '\t')
    previous_litcovid = pd.read_csv(LITCOVID / 'litcovid.tsv', sep = '\t')

    LOGGER.info(f'New entries: {len(updated_litcovid.index) - len(previous_litcovid.index)}.')
    litcovid = updated_litcovid.merge(previous_litcovid, how = 'left', on = 'pmid')

    new_pmids = updated_litcovid['pmid'][~updated_litcovid['pmid'].isin(previous_litcovid['pmid'])]
    
    LOGGER.info(f'Saved updated data/litcovid/litcovid.tsv.')
    litcovid.to_csv(LITCOVID / 'litcovid.tsv', index= False, sep = '\t')

    return new_pmids