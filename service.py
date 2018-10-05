# -*- coding: utf-8 -*-
from selenium import webdriver
from pyvirtualdisplay import Display
from utils import lazy_wait, decorate_class, auto_logger


@decorate_class(lazy_wait)
class Browser:
    def __init__(self):
        self.driver = self.create_web_driver()

    def create_web_driver(self):
        my_display = Display(visible=1, size=(1024,768)).start()

        driver = webdriver.Firefox()
        driver.implicitly_wait(15)
        driver.maximize_window()

        return driver

    def open_page(self, url):
        self.driver.get(url)

    def get_element_by_id(self, id):
        try:
            return self.driver.find_element_by_id(id)
        except:
            raise Exception("cannot find element with id %s" %id)

    def get_element_by_xpath(self, xpath):
        try:
            return self.driver.find_element_by_xpath(xpath)
        except:
            raise Exception("cannot find element with xpath %s" % id)

    def send_string(self, obj, string):
        obj.send_keys(string)

    def click_element(self, obj):
        obj.click()


@decorate_class(auto_logger)
class BrowserService:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.browser = Browser()

    def log_to_google(self):
        self.browser.open_page("http://accounts.google.com/signin")
        user_form = self.browser.get_element_by_id("identifierId")
        self.browser.send_string(user_form, self.login)
        next_button = self.browser.get_element_by_id("identifierNext")
        self.browser.click_element(next_button)
        pass_form_present = self.browser.get_element_by_id("profileIdentifier")
        if pass_form_present:
            pass_form = self.browser.get_element_by_xpath(
                "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/"
                "form/content/section/div/content/div[1]/div/div[1]/div/div[1]/input")
            self.browser.send_string(pass_form, self.password)
            submit_button = self.browser.get_element_by_id("passwordNext")
            self.browser.click_element(submit_button)
            self.browser.open_page("http://google.com")
            login_avatar = self.browser.get_element_by_xpath(
                "/html/body/div/div[3]/div[1]/div/div/div/div[2]/div[4]/div[1]/a")
            if login_avatar:
                return True
        else:
            return False

    def order_meal(self, meal):
        self.browser.open_page("http://luncher.codilime.com/")
        luncher_submit_button = self.browser.get_element_by_xpath(
            "/html/body/div[2]/div[3]/p[2]/a/img")
        self.browser.click_element(luncher_submit_button)
        choose_from_menu = self.browser.get_element_by_xpath(
            "/html/body/div[2]/div/div[1]/nav/ul/li[2]/a")
        self.browser.click_element(choose_from_menu)


#     def order_meal(self):
#         sushi_button = self.driver.find_element_by_xpath(
#         "//input[@value='%s']" % meal)
#         sushi_button.click()
#
#         order_submit = self.driver.find_element_by_xpath(
#         "/html/body/div[2]/div/div[2]/section/div/button")
#         order_submit.click()
#