# -*- coding: utf-8 -*-
from time import sleep
from settings import selenium_wait
import logging
import sys

def lazy_wait(func):
    def wrapper(*args, **kwargs):
        sleep(selenium_wait)

        return func(*args, **kwargs)

    return wrapper

def decorate_class(decorator):
    def wrapper(cls):
        for attr in cls.__dict__:
            if callable(getattr(cls,attr)):
                setattr(cls, attr, decorator(getattr(cls, attr)))
        return cls

    return wrapper

def decorate_object(cls):
    for attr in cls.__dict__:
        if callable(getattr(cls,attr)):
            setattr(cls, attr, lazy_wait(getattr(cls, attr)))
    return cls


def create_logger():
    logger = logging.getLogger("luncher-o-matic")
    logger.setLevel(logging.INFO)

    fh = logging.FileHandler(r"luncher-o-matic.log")

    fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)

    logger.addHandler(fh)

    return logger

def auto_logger(func):
    logger = create_logger()
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            err = "There was an exception in  "
            err += func.__name__
            logger.exception(err)
            sys.exit()

    return wrapper