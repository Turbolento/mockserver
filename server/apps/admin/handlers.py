#coding=utf-8
import tornado.web
from concurrent.futures import ThreadPoolExecutor
import sys

reload(sys)
sys.setdefaultencoding('utf8')

_result = {}            #存储格式为：_result[tid]={'status': 'success', 'msg': context}
TIMEOUT = 30
MAX_WORKERS=50

class BaseHandler(tornado.web.RequestHandler):
    executor = ThreadPoolExecutor(max_workers=MAX_WORKERS)

    def get_current_user(self):
        return self.get_secure_cookie("user")

## 创建你自己的Handlers #####

class IndexHandler(BaseHandler):

    def get(self):
        self.write('world')
