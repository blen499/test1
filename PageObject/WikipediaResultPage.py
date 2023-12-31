import allure
import Core.connectDB as db
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from BasePage.basePage import BasePage


class WikipediaResultPage(BasePage):

    def checkImgOnPage(self):
        return self.assertImgOnPage(alt="Билл Гейтс в 2021 году")

    def checkContents(self):
        contents =['Биография', 'Детство', 'Основание Microsoft', 'Личная жизнь', 'Дальнейшая жизнь'
        , 'Личностные качества', 'Благотворительность', 'Библиография', 'В массовой культуре', 'Книги о Билле Гейтсе',
                   'Фильмы о Билле Гейтсе', '«Ежегодное Послание Билла Гейтса»', 'Примечания', 'Литература', 'Ссылки']

        countContents = ['1', '1.1', '1.2', '1.3'
            , '1.4', '2', '3', '4', '5', '5.1'
            , '5.2', '6', '7', '8', '9']
        try:
            arrContents = self.findElements(By.XPATH, "//span[contains(@class,'toctext')]")
            assert self.checkNestingContents(arrContents) == contents
            assert len(self.checkNestingContents(arrContents))

            arrContents = self.findElements(By.XPATH,"//span[contains(@class,'tocnumber')]")
            assert self.checkNestingContents(arrContents) == countContents
            assert len(self.checkNestingContents(arrContents))

            self.checkTitleContents()



        except Exception:
            exit(f"\nНет списка {arrContents}")
        finally:
            self.takescreenshot()

    def checkNestingContents(self, elem):
        nesting = [nest.text for nest in elem]
        return nesting

    def checkTitleContents(self):
        try:
            title = "Содержание"
            titleContent = self.findElement(text_attribute="mw-toc-heading").text

            assert titleContent == title

            titleLabelContent = self.findElement(by="class", text_attribute="toctogglelabel")

            title = self.checkTitleCSSAfter()

            assert self.checkTitleCSSAfter().count("скрыть") == 1
            titleLabelContent.click()
            assert self.checkTitleCSSAfter().count("показать") == 1
            titleLabelContent.click()
            assert self.checkTitleCSSAfter().count("скрыть") == 1

        except Exception:
            exit("\nНет на странице " + title)
        finally:
            self.takescreenshot()

    def checkLastUpdate(self, client):
        elem = self.findElement(text_attribute="footer-info-lastmod").text

        arr = elem.split()

        obj = {
            "января": 1,
            "февраля": 2,
            'марта': 3,
            'апреля': 4,
            'мая': 5,
            'июня': 6,
            'июля': 7,
            'августа': 8,
            'сентября': 9,
            'октября': 10,
            'ноября': 11,
            'декабря': 12
        }
        date = f'{arr[9]}-{obj[arr[8]]}-{arr[7]}'

        db.checkUpdateClient(client,date)


    def checkTitleCSSAfter(self):
        chars = self.JS("return window.getComputedStyle(document.querySelector('.toctogglelabel'),':after').getPropertyValue('content')")
        return str(chars)


    def assertNotExistPage(self):
        return self.searchOnPageText("Соответствий запросу не найдено.")



