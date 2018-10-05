# -*- coding: utf-8 -*-
from service import BrowserService
from settings import user, passwd, meal

if __name__ == "__main__":
    my_browser = BrowserService(login=user, password=passwd)

    google_log = my_browser.log_to_google()

    if google_log:
        my_browser.order_meal(meal=meal)