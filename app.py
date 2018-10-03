# -*- coding: utf-8 -*-
from service import Browser


if __name__ == "__main__":
    browser = Browser()

    browser.login_to_google()
    browser.open_meal_order()
    order_placed = browser.is_order()

    if not order_placed:
        browser.order_meal()
