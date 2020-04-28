__author__ = 'awakenedhaki'

# DEPENDENCIES
import os
import json

from pathlib import Path
from time import strptime

# CONSTANTS
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'
USER_AGENTS = json.loads(os.environ['USER_AGENTS'])
PROXIES = json.loads(os.environ['PROXIES'])
HEADERS = json.loads(os.environ['HEADERS'])

DATE_FORMAT = r'%d-%m-%Y'