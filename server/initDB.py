#coding=utf-8
from setting import *

for module in INSTALLED_APPS:
    __import__(module+".models")

Base.metadata.create_all(engine)