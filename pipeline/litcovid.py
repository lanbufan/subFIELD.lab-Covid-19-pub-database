#! /usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'awakenedhaki'

# DEPENDENCIES
import re
import json
import pandas as pd

from tqdm import tqdm
from time import sleep
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from crossrefapiclient import Works
from requests.exceptions import HTTPError

# CONSTANTS
URL = 'https://www.ncbi.nlm.nih.gov/research/coronavirus/publication/%s'

# . Class names
TITLE = 'publication-title'
AUTHORS = 'authors'
TOPICS = 'topic'
ABSTRACT = 'content'
REGISTERED_DATE = 'date'
FULL_TEXT = 'full-text-btn'

# . Crossref API wrapper
WORKS = Works()

# . Regex
DOI = re.compile(r'https://doi.org/(.*)')
TODAY = datetime.now().strftime('%b. %d, %Y')

# FUNCTIONS
def ignore_exception(func):
    '''
    In case of an any exception, return "Failed"
    '''
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            return 'Failed'
    return wrapper

@ignore_exception
def text_element(driver, class_name):
    '''
    Get text element of a given HTML element.

    Arguments
        driver : selenium.webdriver.chrome.webdriver.Webdriver
        class_name : Class name of HTML element
    '''
    element = driver.find_element_by_class_name(class_name)
    return element.text

@ignore_exception
def href_attribute(driver, class_name):
    '''
    Get href from an HTML element.

    Arguments
        driver : selenium.webdriver.chrome.webdriver.Webdriver
        class_name : Class name of HTML element
    '''
    element = driver.find_element_by_class_name(class_name)
    return element.get_attribute('href')

@ignore_exception
def list_element(driver, class_name):
    '''
    Get listed text from HTML elements.

    Arguments
        driver : selenium.webdriver.chrome.webdriver.Webdriver
        class_name : Class name of HTML element
    '''
    elements = driver.find_elements_by_class_name(class_name)
    for element in elements:
        yield element.text


def parse_publication(driver):
    '''
    Parse publication view into dictionary.

    Arguments
        driver : selenium.webdriver.chrome.webdriver.Webdriver
    '''
    return {
        'title': text_element(driver, TITLE),
        'authors': text_element(driver, AUTHORS),
        'topics': list(list_element(driver, TOPICS)),
        'abstract': text_element(driver, ABSTRACT),
        'registered_date': text_element(driver, REGISTERED_DATE),
        'full_text': href_attribute(driver, FULL_TEXT)
    }


def parse_publications(data):
    '''
    Parse list of publications by PMID.

    Arguments
        data : pandas.Dataframe
            Dataframe of PMID and journal names.

    Notes
        Download TSV from LitCovid, which has (PMID, Title, Journal)
    '''
    for pmid, journal in tqdm(data.itertuples(index=False)):
        sleep(3)
        driver.get(URL % pmid)
        
        # Wait until title of publication appears
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, TITLE))
        )

        ncbi = parse_publication(driver)

        # Remove trailing journla name from authors list
        ncbi['authors'] = ncbi['authors'].strip(journal)

        ncbi['journal'] = journal
        ncbi['pmid'] = pmid

        try:
            # Search for a DOI in the 'full_text' button element
            doi = DOI.search(ncbi['full_text']).group(1)
            # Send a Crossref GET request for bibliometric data
            xref = WORKS.get(doi).execute()
        except HTTPError:
            # If DOI is not recognized by Crossref
            xref = 'Not in Crossref'
        except AttributeError:
            # If there was no DOI or recognizable DOI in 'full_text' button
            xref = 'Failed'

        yield {'litcovid': ncbi, 'xref': xref}
        # Reset GET request URL
        WORKS.reset()


if __name__ == '__main__':
    litcovid = pd.read_csv('litcovid.tsv', sep = '\t')

    with open('litcovid.json', 'r') as f:
        data = json.load(f)

    driver = webdriver.Chrome()
    for pub in parse_publications(litcovid[['pmid', 'journal']].iloc[len(data):, :]):
        data.append(pub)

    with open('litcovid.json', 'w') as f:
        json.dump(data, f)