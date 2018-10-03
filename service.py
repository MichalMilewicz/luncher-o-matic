# -*- coding: utf-8 -*-
from selenium import webdriver
from settings import user, passwd, meal
from pyvirtualdisplay import Display
from utils import lazy_wait, decorate_class, auto_logger


@decorate_class(lazy_wait)
@decorate_class(auto_logger)
class Browser:
    def __init__(self):
        self.driver = self.create_web_driver()

    def create_web_driver(self):
        my_display = Display(visible=0, size=(1024,768)).start()

        driver = webdriver.Firefox()
        driver.implicitly_wait(15)
        driver.maximize_window()

        return driver

    def open_google_login_form(self):
        self.driver.get("http://google.com")
        login_button = self.driver.find_element_by_id("gb_70")
        login_button.click()

    def send_user_to_google_form(self):
        email_form = self.driver.find_element_by_id("identifierId")
        email_form.send_keys(user)

        next_button = self.driver.find_element_by_id("identifierNext")
        next_button.click()

    def check_send_user_to_google_form(self):
        try:
            return self.driver.find_element_by_id('profileIdentifier')
        except:
            raise Exception("cannot send user to google")

    def send_pass_to_google_form(self):
        pass_form = self.driver.find_element_by_xpath(
        "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/"
        "form/content/section/div/content/div[1]/div/div[1]/div/div[1]/input")
        pass_form.send_keys(passwd)

        submit_button = self.driver.find_element_by_id("passwordNext")
        submit_button.click()

    def check_send_pass_to_google_form(self):
        try:
            return self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div[1]/div/div/div/div[2]/div[4]/div[1]/a")
        except:
            raise Exception("cannot send password to google")

    def open_codilime_luncher(self):
        self.driver.get("http://luncher.codilime.com/")

        luncher_submit_button = self.driver.find_element_by_xpath(
        "/html/body/div[2]/div[3]/p[2]/a/img")
        luncher_submit_button.click()

    def open_codilime_luncher_order_form(self):
        choose_from_menu = self.driver.find_element_by_xpath(
        "/html/body/div[2]/div/div[1]/nav/ul/li[2]/a")
        choose_from_menu.click()

    def is_order(self):
        try:
            return self.driver.find_element_by_id("selections_0_").is_selected()
        except:
            return True

    def order_meal(self):
        sushi_button = self.driver.find_element_by_xpath(
        "//input[@value='%s']" % meal)
        sushi_button.click()

        order_submit = self.driver.find_element_by_xpath(
        "/html/body/div[2]/div/div[2]/section/div/button")
        order_submit.click()

    def login_to_google(self):
        self.open_google_login_form()
        self.send_user_to_google_form()
        if self.check_send_user_to_google_form():
            self.send_pass_to_google_form()

    def open_meal_order(self):
        self.driver.get("http://google.com")
        if self.check_send_pass_to_google_form():
            self.open_codilime_luncher()
            self.open_codilime_luncher_order_form()