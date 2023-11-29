from BasePage.basePage import BasePage

class WikipediaSearchActions(BasePage):


    def searchOnField(self, text):
        return self.findElement(text_attribute='searchInput').send_keys(text)


    def clickOnSearchBtn(self):
        return self.findElement(by='class',text_attribute="pure-button").click()



