# IMPORTS
import pandas as pd
import logging

from pathlib import Path
from time import strptime

# CONSTANTS
ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / 'data'
LITCOVID = DATA / 'litcovid'

DATE_FORMAT = r'%d-%m-%Y'

# LOGGING
LOGGER = logging.getLogger(__file__)
LOGGER.setLevel(logging.INFO)

# . Stream
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_format = logging.Formatter('%(levelname)s - %(message)s')
stream_handler.setFormatter(stream_format)
LOGGER.addHandler(stream_handler)

# . File
file_handler = logging.FileHandler('pipeline.log')
file_handler.setLevel(logging.INFO)
file_format = logging.Formatter(
    '%(asctime)s - %(funcName)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_format)
LOGGER.addHandler(file_handler)

# AVOID CIRCULAR IMPORTS
from litcovid.pubtator import PubTator
from litcovid.scraper import scrape_litcovid
from litcovid.updater import update_litcovid_tsv