from selenium.webdriver.common.by import By

from PageObject.wikipediaSearchActions import WikipediaSearchActions as wiki
from PageObject.WikipediaResultPage import WikipediaResultPage as res
from Core.initBrowser import browser
import Core.connectDB as pg


def test_wiki_search(browser):
    wiki_action = wiki(browser)
    wiki_action.go()

    wiki_action.searchOnField("Bill Gates")
    wiki_action.clickOnSearchBtn();

    wiki_action.searchOnPageText("Гейтс, Билл")

def test_wiki_result_page(browser):
    wiki_action = wiki(browser)
    wiki_action.go()

    wiki_action.searchOnField("Bill Gates")
    wiki_action.clickOnSearchBtn()

    wiki_action = res(browser)
    wiki_action.checkImgOnPage()

def test_wiki_checkContent(browser):
    wiki_action = wiki(browser)
    wiki_action.go()

    wiki_action.searchOnField("Bill Gates")
    wiki_action.clickOnSearchBtn()

    wiki_action = res(browser)
    wiki_action.checkContents()



def test_wiki_db(browser):
    fi = pg.getRandomClient()

    wiki_action = wiki(browser)
    wiki_action.go()

    wiki_action.searchOnField(fi)
    wiki_action.clickOnSearchBtn()

    wiki_action = res(browser)

    wiki_action.checkLastUpdate(client=fi)