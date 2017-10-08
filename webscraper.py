# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
FUNCTION DEFINITIONS

The following section will contain the function definitions for this program
"""

def get_search_terms():
    """ Captures the desired input variables and return them. Initially hard
        coded, but will add more functionality here later
    """
    DEFAULT_QUERY = 'mazda-cx5'
    MANUAL_INPUT_MODE = False
    
    if MANUAL_INPUT_MODE:
        query = input('Type your search query for kijiji: ')
    else:
        query = DEFAULT_QUERY
    main_url = 'https://www.kijiji.ca/b-ottawa/' + query + '/k0l1700185?dc=true'
    return main_url

def get_search_results(terms):
    """ Scrapes the website and stores the results"""
    pass

def display_results(results):
    """ Takes a dictionary with results and prints it out"""
    for index, row in results.items():
        print(index, row)

"""
CONSTANTS AND VARIABLE INITIALIZATION

The following section initializes variables and constants. Note that future
versions will refactor this and modify what is constant and what is variable
"""


"""
MAIN PROGRAM
"""

search_terms = get_search_terms()

search_results = get_search_results(search_terms)

display_results(search_results)