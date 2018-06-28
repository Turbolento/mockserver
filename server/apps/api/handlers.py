# coding=utf-8
import tornado.web
import tornado.concurrent
import tornado.gen
from concurrent.futures import ThreadPoolExecutor
from apps.main.dao.main_curd import checkPasswd, addProject, listAllProjects, addModule, getProjectNameById, \
    listProjectModules, addApi, listProjectApis, getProjectDescById, listApisByMid, getApiData, saveApiData, \
    listAllResponseTypes, saveConsulEnv,listConsulEnvs
from plugin.base import *
import sys, time, json
from plugin import logger

reload(sys)
sys.setdefaultencoding('utf8')

_result = {}  # 存储格式为：_result[tid]={'status': 'success', 'msg': context}
TIMEOUT = 30
MAX_WORKERS = 50


class BaseHandler(tornado.web.RequestHandler):
    executor = ThreadPoolExecutor(max_workers=MAX_WORKERS)

    def prepare(self):
        if self.request.method == "POST":
            self.check_xsrf_cookie()

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")  # FRONTEND
        self.set_header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")
        self.set_header('Access-Control-Allow-Methods', 'POST,GET,PUT,DELETE,OPTIONS')

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
    def prepare(self):
        pass

    def get(self):
        a = self.xsrf_token
        self.write('ok')


class LoginHandler(BaseHandler):
    def post(self):
        account = self.get_argument('account')
        password = self.get_argument('passwd')
        realpasswd = rsa_decrypt(password)
        ispass = checkPasswd(account, md5(hmac_sha256_encrypt(realpasswd, account)))
        if ispass:
            ret = {"status": 0, "msg": "登录成功!"}
            self.set_secure_cookie("user", account)
        else:
            ret = {"status": 1, "msg": "用户名或密码错误！"}
        self.write(ret)

class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie('user')
        ret = {"status": 0, "msg": "退出登录成功!"}
        self.write(ret)

class GetAuthInfoHandler(BaseHandler):
    def get(self):
        user = self.current_user
        if not user:
            ret = {"status": 10001, "msg": "用户未登录！"}
        else:
            ret = {"status": 0, "data": user}
        self.set_header("Content-Type", "application/json; charset=UTF-8")  # 设置返回类型为json的时候，需要返回的内容为字符串，而不是字典
        ret = json.dumps(ret)  # 不加这句上面的设置无效
        self.write(ret)

class NewProjectHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self):
        name = self.get_argument('pjname')
        description = self.get_argument('pjdesc')
        owner = 'admin'  # 后面要换成getCurrentUser
        result = addProject(name, description, owner)
        if result:
            ret = {"status": 0, "msg": "创建成功!", "data": result}
        else:
            ret = {"status": 1, "msg": "创建失败！"}
        self.write(ret)


class ListAllProjectsHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        result = listAllProjects()
        if result:
            ret = {"status": 0, "data": result}
        else:
            ret = {"status": 1, "msg": "记录为空！"}
        self.write(ret)


class NewModuleHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self):
        name = self.get_argument('mname')
        pid = self.get_argument('pid')
        result = addModule(name, pid)
        if result:
            ret = {"status": 0, "msg": "创建成功!", "data": result}
        else:
            ret = {"status": 1, "msg": "创建失败！"}
        self.write(ret)


class GetProjectNameHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        pid = self.get_argument('pid')
        result = getProjectNameById(pid)
        if result:
            ret = {"status": 0, "data": result}
        else:
            ret = {"status": 1, "msg": "查询项目名称失败！"}
        self.write(ret)


class GetProjectDescHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        pid = self.get_argument('pid')
        result = getProjectDescById(pid)
        if result:
            ret = {"status": 0, "data": result}
        else:
            ret = {"status": 1, "msg": "查询项目描述失败！"}
        self.write(ret)


class ListProjectModulesHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        pid = self.get_argument('pid')
        result = listProjectModules(pid)
        if result:
            ret = {"status": 0, "data": result}
        else:
            ret = {"status": 1, "msg": "查询项目模块失败！"}
        self.write(ret)


class NewApiHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self):
        mid = self.get_argument('mid')
        aname = self.get_argument('aname')
        result = addApi(int(mid), aname)
        if result:
            ret = {"status": 0, "data": result}
        else:
            ret = {"status": 1, "msg": "新增接口失败！"}
        self.write(ret)


class ListProjectApis(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        pid = self.get_argument('pid')
        try:
            result = listProjectApis(pid)
        except Exception, e:
            ret = {"status": 1, "msg": e.message}
        else:
            ret = {"status": 0, "data": result}
        self.write(ret)


class ListApisByMidHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        mid = self.get_argument('mid')
        try:
            result = listApisByMid(mid)
        except Exception, e:
            ret = {"status": 1, "msg": e.message}
        else:
            ret = {"status": 0, "data": result}
        self.write(ret)


class GetApiDataHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        aid = self.get_argument("aid")
        try:
            result = getApiData(aid)
        except Exception, e:
            ret = {"status": 1, "msg": e.message}
        else:
            ret = {"status": 0, "data": result}
        self.write(ret)


class SaveApiDataHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self):
        aid = self.get_argument("aid")
        serviceName = self.get_argument("serviceName")
        uri = self.get_argument("uri")
        requestType = self.get_argument("requestType")
        method = self.get_argument("method")
        apiName = self.get_argument("apiName")
        apiDesc = self.get_argument("apiDesc", "")
        requestHeaders = self.get_argument("requestHeaders", '[]')
        requestBodys = self.get_argument("requestBodys", '[]')
        responseHeaders = self.get_argument("responseHeaders", '[]')
        responseBodys = self.get_argument("responseBodys", '[]')
        try:
            saveApiData(aid, serviceName, uri, requestType, method, apiName, apiDesc, requestHeaders, requestBodys,
                        responseHeaders, responseBodys)
        except Exception, e:
            ret = {"status": 1, "msg": e.message}
        else:
            ret = {"status": 0, "msg": "保存成功！"}
        self.write(ret)


class ListAllResponseTypesHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        result = listAllResponseTypes()
        if result:
            ret = {"status": 0, "data": result}
        else:
            ret = {"status": 1, "msg": "查询响应类型失败！"}
        self.write(ret)


class GetConsulEnvInfoHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        result = listConsulEnvs()
        if result:
            ret = {"status": 0, "data": result}
        else:
            ret = {"status": 1, "msg": "查询consul环境失败！"}
        self.write(ret)


class SaveConsulEnvInfoHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self):
        consulEnvs = self.get_argument("consulEnvs", [])
        try:
            saveConsulEnv(consulEnvs)
        except Exception, e:
            ret = {"status": 1, "msg": e.message}
        else:
            ret = {"status": 0, "msg": "保存成功！"}
        self.write(ret)


if __name__ == '__main__':
    api_id = 2
