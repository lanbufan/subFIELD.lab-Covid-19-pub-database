__authors__ = 'awakendhaki'

# DEPENDENCIES
import json
import pandas as pd

from pathlib import Path

# CONSTANTS
DATA = Path(__file__).resolve().parents[1] / 'data'
ZIPFILES = DATA / 'zipfiles'
LITCOVID = DATA / 'litcovid'
RAW = 'Link_Cov_P_database_2020_04_11__9233.zip'

# FUNCTIONS


if __name__ == '__main__':
    current_raw = pd.read_csv(ZIPFILES / RAW, compression = 'zip')

    with (LITCOVID / 'litcovid.json').open('r') as f:
        litcovid = json.load(f)

    

