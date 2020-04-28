# IMPORTS
import pandas as pd
import logging

from pipeline import DATA, DATE_FORMAT

# CONSTANTS
LITCOVID = DATA / 'litcovid'

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
from pipeline.litcovid.pubtator import PubTator
from pipeline.litcovid.scraper import scrape_litcovid
from pipeline.litcovid.updater import update_litcovid_tsv