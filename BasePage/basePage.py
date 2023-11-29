import allure
from allure_commons.types import AttachmentType
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp
from selenium.webdriver.common.by import By
from selenium import webdriver


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.wikipedia.org/'

    @allure.step("Находим элемент на странице")
    def findElement(self, by='ID', attribute=None, text_attribute=None, idx_browser=0, timeout=10):
        # self.driver.switch_to.window(self.driver.window_handles[idx_browser])

        elem = None
        # поскольку нет switch/case в py3.9 буду делать if elif
        try:
            if (by == 'ID'):
                elem = WebDriverWait(self.driver, timeout).until(
                    exp.presence_of_element_located((By.ID, text_attribute))
                )
            elif (by == "XPATH"):
                elem = WebDriverWait(self.driver, timeout).until(
                    exp.presence_of_element_located((By.XPATH, text_attribute))
                )
            elif (by == "IMG"):
                locator = f"//{by}[@{attribute}='{text_attribute}']"
                elem = WebDriverWait(self.driver, timeout).until(
                    exp.presence_of_element_located((By.XPATH, locator))
                )
            elif (by == None):
                locator = f"//{attribute}[contains(text(),'{text_attribute}')]"
                elem = WebDriverWait(self.driver, timeout).until(
                    exp.presence_of_element_located((By.XPATH, locator))
                )
            elif (by == "class"):
                elem = WebDriverWait(self.driver,timeout).until(
                    exp.presence_of_element_located((By.CLASS_NAME, text_attribute))
                )
            return elem

        except TimeoutException:
            exit("\nУпали по таймауту, не нашли элемент: " + text_attribute)

    @allure.step("Находим элементы на странице")
    def findElements(self,by, text_attrubute=None, idx_browser=0):
        self.driver.switch_to.window(self.driver.window_handles[idx_browser])

        return self.driver.find_elements(by,text_attrubute)
    @allure.step("Переход на страницу")
    def go(self):
        return self.driver.get(self.base_url)


    @allure.step("Поиск текста на странице")
    def searchOnPageText(self,text):
        page = self.driver.page_source

        try:
            assert text in page
        except Exception:
            exit("\nНа странице не найден элемент - " + text)
        finally:
            self.takescreenshot()
    @allure.step("Проверка фото на странице")
    def assertImgOnPage(self, src=None, alt=None):
        try:
            text = None

            if alt is not None:
                attributeImg = "alt"
                text = alt

            if src is not None:
                attributeImg = "src"
                text = src

            img = self.findElement(by="IMG", attribute=attributeImg, text_attribute=text)

        except Exception:
            exit(f"Не найдено на странице фото с именем - {text}")
        # finally:
            # allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    @allure.step("Screenshots")
    def takescreenshot(self):
        return allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def JS(self, script):
        return self.driver.execute_script(script)