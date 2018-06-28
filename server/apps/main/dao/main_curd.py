# coding=utf-8
import sys, json

reload(sys)
sys.setdefaultencoding('utf-8')
from setting import engine
from sqlalchemy.orm import sessionmaker
from apps.main.service.consulOPT import getService,getAllService,newAgent
from mysql.connector.errors import OperationalError
from apps.main.models import *

Session = sessionmaker(bind=engine)

#############新增、创建#####################
def addUser(account, passwd, email, role, name='', status=True):
    session = Session()
    user = User(account=account, name=name, passwd=passwd, email=email, role=role, status=status)
    session.add(user)
    try:
        session.commit()
    except Exception, e:
        session.rollback()
        raise e
    finally:
        ret = user.id
        session.close()
    return ret


def addResponseType(name, value):
    session = Session()
    resType = ResponseType(name=name, value=value)
    session.add(resType)
    try:
        session.commit()
    except Exception, e:
        session.rollback()
        raise e
    finally:
        ret = resType.id
        session.close()
    return ret


def addProject(name, description, owner):
    session = Session()
    owner_id = getUserIdByAccount_ns(session,owner)
    project = Project(name=name, description=description, owner_id=owner_id)
    session.add(project)
    try:
        session.commit()
    except Exception, e:
        session.rollback()
        raise e
    finally:
        ret = project.id
        session.close()
    return ret


def addModule(name, pid):
    session = Session()
    module = Module(name=name, project_id=pid)
    session.add(module)
    try:
        session.commit()
    except Exception, e:
        session.rollback()
        raise e
    finally:
        ret = module.id
        session.close()
    return ret


def addApi(mid, aname):
    session = Session()
    if mid > 0:
        api = Api(name=aname, module_id=mid)
    else:
        api = Api(name=aname, project_id=-mid)
    session.add(api)
    try:
        session.commit()
    except Exception, e:
        session.rollback()
        raise e
    finally:
        ret = api.id
        session.close()
    return ret


##################保存数据####################################################
def saveConsulEnv(consulEnvs):
    session = Session()
    # 删除所有consul
    consuls = session.query(Consul).all()
    for cons in consuls:
        session.delete(cons)

    consulEnvs = json.loads(consulEnvs)         #[{u'ip': u'172.30.1.135', u'port': u'8500', u'desc': u'\u4e91\u8d37Consul Client'}, {u'ip': u'172.30.2.89', u'port': u'8500', u'desc': u'testConsul'}]
    for c in consulEnvs:
        consul = Consul(ip=c.get('ip'),port=c.get('port'),desc=c.get('desc'))
        session.add(consul)
    try:
        session.commit()
    except:
        session.rollback()
    finally:
        session.close()

def saveApiData(aid, serviceName, uri, requestType, method, apiName, apiDesc, requestHeaders, requestBodys,
                responseHeaders, responseBodys):
    session = Session()
    api = session.query(Api).get(aid)
    api.name = apiName
    api.service_name = serviceName
    api.uri = uri
    api.request_content_type = requestType
    api.request_method = method
    api.description = apiDesc
    session.add(api)
    #删除所有api.paras：
    paras = api.paras
    for p in paras:
        session.delete(p)
    #删除所有api.responseheader
    responseheader = api.responseheader
    for rh in responseheader:
        session.delete(rh)
    #删除所有api.response_set
    response_set = api.response_set
    for rs in response_set:
        session.delete(rs)

    responseHeaders = json.loads(responseHeaders)
    for responseHeader in responseHeaders:
        rh = ResponseHeader(key=responseHeader["key"], value=responseHeader["value"],
                            description=responseHeader["desc"])
        api.responseheader.append(rh)

    responseBodys = json.loads(responseBodys)
    for responseBody in responseBodys:
        typeid = getResponseTypeIdByName_ns(session, responseBody["type"])
        rsp = Response(name=responseBody["name"], description=responseBody["desc"],
                       status_code=responseBody["status"], response_content=responseBody["response"],
                       type_id=typeid)
        api.response_set.append(rsp)

    requestHeaders = json.loads(requestHeaders)
    for index, requestHeader in enumerate(requestHeaders):
        rp = RequestPara(order=index, name=requestHeader["name"], match=requestHeader["match"], value=requestHeader["value"],
                    response_id=getResponseIdByName_ns(session,requestHeader["response"]),position="header")
        api.paras.append(rp)

    requestBodys = json.loads(requestBodys)
    for index, requestBody in enumerate(requestBodys):
        rp = RequestPara(order=index, name=requestBody["name"], match=requestBody["match"], value=requestBody["value"],
                    response_id=getResponseIdByName_ns(session,requestBody["response"]),position="body")
        api.paras.append(rp)

    try:
        session.commit()
    except Exception, e:
        session.rollback()
        raise e
    finally:
        session.close()


###################查询###################################
def getResponseById(rid):
    session = Session()
    response = session.query(Response).get(rid)
    ret = {}
    ret.setdefault("statusCode",response.status_code)
    ret.setdefault("type",getResponseTypeById_ns(session,response.type_id))
    ret.setdefault("response",response.response_content)
    session.close()
    return ret

def getResponseTypeById_ns(session,tid):
    respType = session.query(ResponseType).get(tid)
    if not respType:
        return None
    else:
        return respType.value

def getResponseIdByName_ns(session,name):
    response = session.query(Response).filter_by(name=name).first()
    if not response:
        ret = None
    else:
        ret = response.id
    return ret

def getResponseTypeIdByName_ns(session,name):
    responseType = session.query(ResponseType).filter_by(name=name).first()
    if not responseType:
        ret = None
    else:
        ret = responseType.id
    return ret

def getUserIdByAccount_ns(session,account):
    user = session.query(User).filter_by(account=account).first()
    if not user:
        ret = None
    else:
        ret = user.id
    return ret


def getUserNameById_ns(session,uid):
    user = session.query(User).get(uid)
    if not user:
        ret = None
    else:
        ret = user.name
    return ret


def getProjectNameById(pid):
    session = Session()
    project = session.query(Project).get(pid)
    if not project:
        ret = None
    else:
        ret = project.name
    session.close()
    return ret


def getProjectDescById(pid):
    session = Session()
    project = session.query(Project).get(pid)
    if not project:
        ret = None
    else:
        ret = project.description
    session.close()
    return ret


def getApiData(aid):
    session = Session()
    api = session.query(Api).get(aid)
    apiName = api.name
    serviceName = api.service_name
    uri = api.uri
    requestType = api.request_content_type
    method = api.request_method
    apiDesc = api.description
    requestHeaders = getRequestHeadersByAid_ns(session, aid)
    requestBodys = getRequestBodysByAid_ns(session, aid)
    responseHeaders = getResponseHeadersByAid_ns(session, aid)
    responseBodys = getResponseBodysByAid_ns(session, aid)
    session.close()
    ret = {}
    ret.setdefault('apiName', apiName)
    ret.setdefault('serviceName', serviceName)
    ret.setdefault('uri', uri)
    ret.setdefault('requestType', requestType)
    ret.setdefault('method', method)
    ret.setdefault('apiDesc', apiDesc)
    ret.setdefault('requestHeaders', requestHeaders)
    ret.setdefault('requestBodys', requestBodys)
    ret.setdefault('responseHeaders', responseHeaders)
    ret.setdefault('responseBodys', responseBodys)
    return ret


def getRequestHeadersByAid_ns(session, aid):
    ret = []
    headers = session.query(RequestPara).filter_by(api_id=aid, position="header").order_by(RequestPara.order).all()
    for index, header in enumerate(headers):
        ret.append({"id": index, "name": header.name, "match": header.match, "value": header.value,
                    "response": getResponseNameById_ns(session, header.response_id)})
    return ret


def getResponseNameById_ns(session, rid):
    if not rid:
        return None
    response = session.query(Response).get(rid)
    if not response:
        ret = None
    else:
        ret = response.name
    return ret


def getRequestBodysByAid_ns(session, aid):
    ret = []
    bodys = session.query(RequestPara).filter_by(api_id=aid, position="body").order_by(RequestPara.order).all()
    for index, body in enumerate(bodys):
        ret.append({"id": index, "name": body.name, "match": body.match, "value": body.value,
                    "response": getResponseNameById_ns(session, body.response_id)})
    return ret


def getResponseHeadersByAid_ns(session, aid):
    ret = []
    headers = session.query(ResponseHeader).filter_by(api_id=aid).all()
    for index, header in enumerate(headers):
        ret.append({"id": index, "key": header.key, "value": header.value, "desc": header.description})
    return ret


def getResponseBodysByAid_ns(session, aid):
    ret = []
    bodys = session.query(Response).filter_by(api_id=aid).all()
    for index, body in enumerate(bodys):
        ret.append({"id": index, "name": body.name, "type": getResponseTypeNameById_ns(session, body.type_id),
                    "status": body.status_code, "response": body.response_content, "desc": body.description})
    return ret

def getResponseTypeNameById_ns(session, tid):
    if not tid:
        return None
    responseType = session.query(ResponseType).get(tid)
    if not responseType:
        ret = None
    else:
        ret = responseType.name
    return ret

def getServerHost(serviceName):
    session = Session()
    #1/判断requestService中是否存在serviceName；存在进入第2步，不存在进入第3步
    #2/存在直接取consul中心地址，从中心获取serviceName对应的主机，不能获取到的话进入第三步
    #3/依次从配置中的consul地址查询serviceName，返回找到的consul中心，并将信息记入/更新到requestService中
    #4/通过找到的consul和serviceName查询出当前可用主机并返回
    reqService = session.query(RequestService).filter_by(serviceName=serviceName).first()
    if reqService:
        consulIp = reqService.consul_ip
        consulPort = reqService.consul_port
        agent = newAgent(consulIp,consulPort)
        try:
            serverIP,serverPort = getService(agent,serviceName)
            session.close()
            return serverIP,serverPort
        except:
            pass
    consuls = listConsulEnvs_ns(session)
    for cons in consuls:
        cip,cport = cons.get("ip"),cons.get("port")
        agent = newAgent(cons.get("ip"),cons.get("port"))
        allServices = getAllService(agent)
        if serviceName in allServices:
            if reqService:
                reqService.consul_ip = cons.get("ip")
                reqService.consul_port = cons.get("port")
                session.add(reqService)
            else:
                rs = RequestService(serviceName=serviceName,consul_ip=cons.get("ip"),consul_port = cons.get("port"))
                session.add(rs)
                session.commit()
            try:
                serverIP, serverPort = getService(agent, serviceName)
            except:
                continue
            else:
                session.close()
                return serverIP, serverPort
        else:
            continue
    session.close()
    raise Exception("已配置consul中不存在服务：%s"%serviceName)

######################列出、展示#########################################
def listConsulEnvs_ns(session):
    consulEnvs = session.query(Consul).all()
    ret = []
    for consul in consulEnvs:
        ret.append({"ip":consul.ip,"port":consul.port,"desc":consul.desc})
    return ret

def listConsulEnvs():
    session = Session()
    consulEnvs = session.query(Consul).all()
    ret = []
    for consul in consulEnvs:
        ret.append({"ip":consul.ip,"port":consul.port,"desc":consul.desc})
    session.close()
    return ret

def listAllResponseTypes():
    session = Session()
    responseTypes = session.query(ResponseType).all()
    ret = []
    for rt in responseTypes:
        ret.append(rt.name)
    session.close()
    return ret

def listAllProjects():
    session = Session()
    projects = session.query(Project).all()
    ret = []
    for pj in projects:
        ret.append({"pid": pj.id, "pname": pj.name, "pdesc": pj.description, "powner": getUserNameById_ns(session,pj.owner_id),
                    "pctime": datetime.strftime(pj.createtime, "%Y-%m-%d %H:%M:%S")})
    session.close()
    return ret


def listModlueApis_ns(session, mid):  # _ns结尾的表示不需要重新获取session
    ret = []
    apis = session.query(Api).filter_by(module_id=mid).all()
    for api in apis:
        ret.append({"aid": api.id, "apiName": api.name})
    return ret


def listProjectModules(pid):
    session = Session()
    modules = session.query(Module).filter_by(project_id=pid).all()
    ret = []
    if not modules:
        ret = None
    else:
        for module in modules:
            mid = module.id
            ret.append({"mid": mid, "moduleName": module.name, "apis": listModlueApis_ns(session, mid)})
    session.close()
    return ret


def listProjectApis(pid):
    session = Session()
    apis = session.query(Api).filter_by(project_id=pid).all()
    ret = []
    if not apis:
        ret = None
    else:
        for api in apis:
            ret.append({"aid": api.id, "aname": api.name})
    session.close()
    return ret


def listApisByMid(mid):
    session = Session()
    apis = session.query(Api).filter_by(module_id=mid).all()
    ret = []
    if not apis:
        ret = None
    else:
        for api in apis:
            ret.append({"aid": api.id, "aname": api.name})
    session.close()
    return ret

#################业务操作###############################################
#####################校验##############################################
def checkPasswd(account, passwd):
    session = Session()
    a = session.query(User).filter_by(account=account, passwd=passwd, status=1).first()
    if not a:
        ret = False
    else:
        ret = True
    session.close()
    return ret

def checkMatch(requestValue,matched_value,matchCondition):    #matchCondition ["等于","包含","大于","小于","开始于","结束于","任意值"]
    if not isinstance(requestValue,unicode):
        requestValue = json.dumps(requestValue,ensure_ascii=False)
    if(matchCondition==0):
        ret= True if requestValue==matched_value else False
    elif(matchCondition==1):
        ret = True if requestValue.__contains__(matched_value) else False
    elif (matchCondition == 2):
        try:
            ret = True if float(requestValue) > float(matched_value) else False
        except ValueError:
            ret = True if requestValue>matched_value else False
    elif (matchCondition == 3):
        try:
            ret = True if float(requestValue) < float(matched_value) else False
        except ValueError:
            ret = True if requestValue < matched_value else False
    elif (matchCondition == 4):
        ret = True if requestValue.startswith(matched_value) else False
    elif (matchCondition == 5):
        ret = True if requestValue.endswith(matched_value) else False
    elif (matchCondition == 6):
        ret = True
    else:
        ret = False
    return ret


def checkMockMatch(serviceName,uri,request_headers,request_query,request_body):     #匹配上就返回responseID，否则返回None
    session = Session()
    api = session.query(Api).filter_by(service_name=serviceName,uri=uri).first()
    if not api:
        session.close()
        return None,None
    else:
        aid = api.id
        rhs =session.query(ResponseHeader).filter_by(api_id=aid).all()
        headers = []
        for rh in rhs:
            headers.append({"name":rh.key,"value":rh.value})
        #分3种情况匹配参数：
        #1/匹配header:
        headerParas = session.query(RequestPara).filter_by(api_id=aid,position="header").order_by(RequestPara.order).all()
        for hp in headerParas:
            request_value = request_headers.get(hp.name)
            if not request_value:
                continue
            else:
                match = checkMatch(request_value,hp.value,hp.match)     #请求值，配置值，匹配规则
                if match:
                    session.close()
                    return hp.response_id,headers
        # 2/匹配body和urlQuery
        bodyParas = session.query(RequestPara).filter_by(api_id=aid,position="body").order_by(RequestPara.order).all()
        for bp in bodyParas:
            if bp.name.__contains__("."):
                #则表明为body匹配
                pList = bp.name.split(".")
                request_value = request_body
                for i in pList:
                    request_value = request_value.get(i,None)
                    if not request_value:
                        break
            else:
                request_value = request_query.get(bp.name) or request_body.get(bp.name)
            if not request_value:
                continue
            else:
                match = checkMatch(request_value,bp.value,bp.match)     #请求值，配置值，匹配规则
                if match:
                    session.close()
                    return bp.response_id,headers
        #3/没有匹配上：
        return None,None
###############################################################


if __name__ == '__main__':
    a = {"sign":None,"ext":None,"params":{"userId":"P00000017周静阿林"}}
    print json.dumps(["fa","dfasfas"],ensure_ascii=False)