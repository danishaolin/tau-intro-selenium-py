"""
These tests cover DuckDUckGo search.
"""

import pytest
#nao usar assim explicito com tempo, validar se o campo está visivel
#from selenium.webdriver.support import WebDriverWait
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage

@pytest.mark.parametrize('Phrase',['panda','t-shirt','polar bear'])
def test_basic_duckduckgo_search(browser, Phrase):
    search_pg = DuckDuckGoSearchPage(browser)
    result_pg = DuckDuckGoResultPage(browser)

    #Phrase = "Tshirt"
    #Given the dudckduckgo home page is displayed
    search_pg.load()
    #
    search_pg.search(Phrase)

    #then the search result query is tshirt
    assert Phrase == result_pg.search_input_value()

    titles = result_pg.result_link_titles()
    matches = [t for t in titles if Phrase.lower() in t.lower()]
    assert len(matches) > 0

    assert Phrase in result_pg.title()
