# coding=utf-8
import tornado.web
import tornado.concurrent
import tornado.gen
from concurrent.futures import ThreadPoolExecutor
from dao.main_curd import *
import sys, time, json
from tornado.httpclient import HTTPRequest
try:
    from tornado.curl_httpclient import CurlAsyncHTTPClient as AsyncHTTPClient
except ImportError:
    from tornado.simple_httpclient import SimpleAsyncHTTPClient as AsyncHTTPClient

reload(sys)
sys.setdefaultencoding('utf8')

_result = {}  # 存储格式为：_result[tid]={'status': 'success', 'msg': context}
TIMEOUT = 30
MAX_WORKERS = 50


class BaseHandler(tornado.web.RequestHandler):
    executor = ThreadPoolExecutor(max_workers=MAX_WORKERS)

    def get_current_user(self):
        return self.get_secure_cookie("user")


######### handler类异步处理编写方法 ##############
####前端同步获取结果####
class Test1Handler(BaseHandler):
    @tornado.concurrent.run_on_executor
    def background_task(self):
        # do some thing asynchronously
        res = 'hello,world'
        return res

    @tornado.gen.coroutine
    def get(self):
        res = yield self.background_task()
        self.write(res)

####前端异步获取结果####
##第一步，通知服务器执行处理，并生成、存储tid，并返回tid到前端
class Test2Handler(BaseHandler):
    @tornado.concurrent.run_on_executor
    def background_task(self, tid):
        try:
            # do some thing asynchronously
            res = {'status': 'success', 'msg': ''}
        except Exception, e:
            res = {'status': 'failed', 'msg': e.message}
        _result[tid] = res

    @tornado.gen.coroutine
    def get(self):
        tid = str(int(time.time() * 10000))
        yield self.background_task(tid)
        self.write(tid)

    @tornado.gen.coroutine
    def post(self):
        tid = str(int(time.time() * 10000))
        yield self.background_task(tid)
        self.write(tid)

# 第二步，根据tid查询结果内容
class AsynGetResultHandler(BaseHandler):
    @tornado.concurrent.run_on_executor
    def background_task(self, tid, timeout):
        start = time.time()
        while not tid in _result.keys():
            if time.time() - start > timeout:
                break
            time.sleep(0.2)
        if tid in _result.keys():
            out = _result[tid]  # 结果
            del _result[tid]  # 删除tid的数据。
            return out
        else:
            return "timeout."

    @tornado.gen.coroutine
    def get(self, timeout=TIMEOUT):
        tid = self.get_argument("tid")
        res = yield self.background_task(tid, timeout)
        self.write(res)

##  创建你自己的Handlers  ##
class IndexHandler(BaseHandler):
    def on_response(self, respnose):
        if respnose.code!=200:
            self.set_status(respnose.code, respnose.error.message)
        else:
            for k in respnose.headers:
                self.set_header(k,respnose.headers.get(k))
            self.write(respnose.body)
        self.finish()

    @tornado.web.asynchronous
    def post(self):
        req = self.request
        protocol = req.protocol
        host = req.host
        method = req.method
        uri = req.uri  # 全值匹配，包含query部分
        headers_o = req.headers
        body_o = req.body
        remote_ip = req.remote_ip
        path = req.path
        request_headers = req.headers  # <class 'tornado.httputill.HTTPHeaders'>;    类字典==>{name:key}
        request_query = req.arguments  # {name:[key1,key2]};   字典,value为list
        request_body = req.body  # string类型
        serviceName = request_headers.get("downstream-service-id", None)
        if not serviceName:
            self.set_status(500, "请求头解析失败!")
            self.finish()
        if not request_body:
            request_body = {}
        else:
            try:
                request_body = json.loads(request_body)  # 如果是post请求，请求内容是json格式的，则处理，否则不做任何处理；后面可以扩展处理
            except:
                request_body = {}
        t = {}
        for i in request_query:
            t.setdefault(i, request_query[i][-1])  # 取query中最后一个值为准
        request_query = t
        responseID, headers = checkMockMatch(serviceName, uri, request_headers, request_query,
                                             request_body)  # 返回None则表示没有匹配上，或者匹配上没有设置响应
        if responseID:
            response = getResponseById(responseID)
            self.set_status(response.get("statusCode"))
            self.set_header("Content-Type", response.get("type"))
            if headers:
                for hd in headers:
                    self.add_header(hd.get("name"), hd.get("value"))
            self.write(response.get("response"))
            self.finish()
        else:
            try:
                serverIP, serverPort = getServerHost(serviceName)
            except Exception, e:
                self.set_status(500, e.message)
                self.finish()
            else:
                serverhost = "%s://%s:%s" % (protocol, serverIP, serverPort)
                AsyncHTTPClient().fetch(
                    HTTPRequest(
                        url=serverhost + uri,
                        method=method,
                        headers=headers_o,
                        body=body_o,
                        validate_cert=False
                    ),
                    self.on_response)

    @tornado.web.asynchronous
    def get(self):
        req = self.request
        protocol = req.protocol
        host = req.host
        method = req.method
        uri = req.uri  # 全值匹配，包含query部分
        headers_o = req.headers
        body_o = req.body
        remote_ip = req.remote_ip
        path = req.path
        request_headers = req.headers  # <class 'tornado.httputill.HTTPHeaders'>;    类字典==>{name:key}
        request_query = req.arguments  # {name:[key1,key2]};   字典,value为list
        request_body = req.body  # string类型
        serviceName = request_headers.get("downstream-service-id", None)
        if not serviceName:
            self.set_status(500, "请求头解析失败!")
            self.finish()
        if not request_body:
            request_body = {}
        else:
            try:
                request_body = json.loads(request_body)  # 如果是post请求，请求内容是json格式的，则处理，否则不做任何处理；后面可以扩展处理
            except:
                request_body = {}
        t = {}
        for i in request_query:
            t.setdefault(i, request_query[i][-1])  # 取query中最后一个值为准
        request_query = t
        responseID, headers = checkMockMatch(serviceName, uri, request_headers, request_query,
                                             request_body)  # 返回None则表示没有匹配上，或者匹配上没有设置响应
        if responseID:
            response = getResponseById(responseID)
            self.set_status(response.get("statusCode"))
            self.set_header("Content-Type", response.get("type"))
            if headers:
                for hd in headers:
                    self.add_header(hd.get("name"), hd.get("value"))
            self.write(response.get("response"))
            self.finish()
        else:
            try:
                serverIP, serverPort = getServerHost(serviceName)
            except Exception, e:
                self.set_status(500, e.message)
                self.finish()
            else:
                serverhost = "%s://%s:%s" % (protocol, serverIP, serverPort)
                AsyncHTTPClient().fetch(
                    HTTPRequest(
                        url=serverhost + uri,
                        method=method,
                        headers=headers_o,
                        body=body_o,
                        validate_cert=False
                    ),
                    self.on_response)

if __name__ == '__main__':
    skip = False
    ret = ""

