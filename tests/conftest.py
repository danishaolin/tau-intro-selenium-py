"""
This module contains shared fixtures.
Function 
"""
import json
import pytest
import selenium.webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def config(scope='session'):
    with open('config.json') as config_file:
        config = json.load(config_file)

    #assert values acceptable
    assert config['browser'] in ['Firefox','Chrome','Headless Chrome']
    assert isinstance(config['implicit_wait'],int)
    assert config['implicit_wait'] > 0
    return config
     

@pytest.fixture
def browser(config):

    if config['browser'] == 'Headless Chrome' :
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        b = selenium.webdriver.Chrome(options=opts)
    elif config['browser'] == 'Chrome' :
        #initialize chrome webdriver
        b = selenium.webdriver.Chrome()
    elif config['browser'] == 'Firefox' :
        #initialize chrome webdriver
        b = selenium.webdriver.Firefox()
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')


    #wait 10 seconds for elements to appear
    b.implicitly_wait(config['implicit_wait'])

    #return the webdriver instance for the setup
    yield b

    #quit the webdriver instance for the cleanup
    b.quit()

