#coding=utf-8

from tornado.web import url
from handlers import IndexHandler

urls = [
    url(r'', IndexHandler,name="index"),
]