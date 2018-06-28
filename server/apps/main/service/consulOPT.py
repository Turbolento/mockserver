# coding=utf-8
import sys, requests, re
from consul import Consul

reload(sys)
sys.setdefaultencoding('utf-8')


def newAgent(cip, cport):
    return Consul(host=cip, port=cport)


def getAllService(agent):  # agent = Consul(host='172.30.1.71', port="8500")
    newestIndex, services = agent.catalog.services()  # ('23452', {u'test': [u'dev'], u'consul': [], u'mockPlatform': []})       ==>{'服务名1'：[tag1,tag2,...],...}
    servicesList = services.keys()
    servicesList.remove('consul')  # 排除掉名称为'consul'的服务,为server端自带服务
    return servicesList


def getConnectTime(url):
    return requests.head(url).elapsed.total_seconds()


def getService(agent, name):  # 负载均衡获取服务实例agent = Consul(host='172.30.1.71', port="8500")
    newestIndex, nodeList = agent.catalog.service(name)
    if not nodeList:
        raise Exception('There is no service: [%s] can be used!' % name)
    dcset = set()  # DataCenter 集合 初始化
    for service in nodeList:
        dcset.add(service.get('Datacenter'))
    serviceList = []  # 服务列表 初始化
    for dc in dcset:
        newestIndex, allNodeList = agent.catalog.service(name, dc=dc)
        for serv in allNodeList:
            serviceId = serv.get('ServiceID')
            healthNodeList = agent.health.checks(name)[1]
            for i in healthNodeList:
                if i.get('ServiceID') != serviceId:
                    continue
                else:
                    health_output = i.get('Output')
                    try:
                        health = re.search(r'HTTP GET (http:.*): 2.*', health_output).group(1)
                    except:
                        health = None
                if health:
                    address = serv.get('ServiceAddress')
                    port = serv.get('ServicePort')
                    serviceList.append({'address': address, 'port': port, 'health': health})
    if len(serviceList) == 0:
        raise Exception('no serveice can be used')
    else:
        ret = ()
        fastest = None
        for s in serviceList:
            health = s.get('health')
            if health:
                http_conn_time = getConnectTime(health)
                if not fastest:
                    fastest = http_conn_time
                    ret = (s['address'], int(s['port']))
                else:
                    if http_conn_time < fastest:
                        ret = (s['address'], int(s['port']))
        return ret


if __name__ == '__main__':
    agent1 = Consul(host='172.29.0.140', port="8500")
    agent2 = Consul(host='172.29.0.15', port="8500")
    agent = Consul(host='172.29.0.15', port="8500")
    print getService(agent2, 'yyfax-agreement-job')
