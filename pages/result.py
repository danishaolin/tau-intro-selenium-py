"""
Contains DuckDuckGo Result Page
"""
from selenium.webdriver.common.by import By

class DuckDuckGoResultPage:

    #locators
    SEARCH_INPUT = (By.ID, 'search_form_input')
    RESULT_LINKS = (By.CSS_SELECTOR, 'a.result__a')
    #r1-0 > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > p:nth-child(1)
    #html.has-zcm.is-link-style-exp.is-link-order-exp.is-link-breadcrumb-exp.is-related-search-exp.is-vertical-tabs-exp.js.no-touch.opacity.csstransforms3d.csstransitions.svg.cssfilters.is-not-mobile-device.full-urls.breadcrumb-urls.dark-header.dark-bg.react.has-footer body.body--serp div.site-wrapper.js-site-wrapper div#web_content_wrapper.content-wrap div#react-layout div div div.qrc3T8W2PIYg9L63oA06.IlK3G8WDnnjkNGDV6qzo.h3EKGeHmRRkjbMqYfNUi.wuwdN2SgDOTwsnBO5PI7.rXBzGoYc_uM83jRoODrM.xWVFEW_kM7bYLASLNfsZ div.FMPme3X940xAt4SKPFuw section.At_VJ9MlrHsSjbfCtz2_.aDtqDaYogch0DyrGTrX6 ol.react-results--main li.wLL07_0Xnd1QZpzpfR4W article#r1-0.yQDlj3B5DI5YO8c8Ulio.CpkrTDP54mqzpuCSn1Fa.SKlplDuh9FjtDprgoMxk.Fr1jPX9uTqiYNJFs2Cfb div.OQ_6vPwNhCeusNiEDcGp div.mwuQiMOjmFJ5vmN6Vcqw.CmOawDMavJGKvqBIPeeC.SgSTKoqQXa0tEszD2zWF.VkOimy54PtIClAT3GMbr.LQVY1Jpkk8nyJ6HBWKAk span.DpVR46dTZaePK29PDkz8 a

    def __init__(self,browser):
        self.browser = browser
    
    def result_link_titles(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]
        return titles

    def search_input_value(self):
        search_input= self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value

    def title(self):
        #print(self.browser.title)
        return self.browser.title