# DEPENDENCIES
from crossrefapiclient import Works
from pipeline import PubTator update_litcovid_tsv

# CONSTANTS
PUBTATOR_TYPE = 'biocjson'

# OBJECTS
works = Works()
pubtator = PubTator(PUBTATOR_TYPE)

if __name__ == '__main__':
    # Update LitCovid TSV file
    # . Provides recently enter PMIDs
    pmids = update_litcovid_tsv()

    