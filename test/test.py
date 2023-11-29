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

def test_wiki_check_content(browser):
    wiki_action = wiki(browser)
    wiki_action.go()

    wiki_action.searchOnField("Bill Gates")
    wiki_action.clickOnSearchBtn()

    wiki_action = res(browser)
    wiki_action.checkContents()



def test_wiki_db_exist_client(browser):
    fi = pg.getRandomClient(True)

    wiki_action = wiki(browser)
    wiki_action.go()

    wiki_action.searchOnField(fi)
    wiki_action.clickOnSearchBtn()

    wiki_action = res(browser)

    wiki_action.checkLastUpdate(client=fi)

def test_wiki_db_not_exist_client(browser):
    fi = pg.getRandomClient(False)

    wiki_action = wiki(browser)
    wiki_action.go()

    wiki_action.searchOnField(fi)
    wiki_action.clickOnSearchBtn()

    wiki_action = res(browser)

    wiki_action.assertNotExistPage()