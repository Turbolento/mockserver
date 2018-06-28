#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from dao.main_curd import *
from plugin.base import md5,hmac_sha256_encrypt
import time

#数量5
def createUser():
    # 创建模拟用户
    addUser(account='admin',name='管理员',passwd=md5(hmac_sha256_encrypt('abc123456', 'admin')), email='zhoujlc@yonyou.com',
            role=100)
    addUser(account='test', passwd=md5(hmac_sha256_encrypt('abc123456', 'test')), email='zhoujlc@yonyou.com', role=100)
    addUser(account='fengyca', passwd=md5(hmac_sha256_encrypt('abc123456', 'fengyca')), email='zhoujlc@yonyou.com',
            role=100)
    addUser(account='zhoujlc', passwd=md5(hmac_sha256_encrypt('abc123456', 'zhoujlc')), email='zhoujlc@yonyou.com',
            role=100)
    print("用户创建成功！")

#数量5
def createResponseType():
    # 创建响应类型
    addResponseType('json', 'application/json; charset=UTF-8')
    addResponseType('text', 'text/plain; charset=UTF-8')
    addResponseType('xml', 'text/xml; charset=UTF-8')
    addResponseType('jpeg', 'image/jpeg')
    addResponseType('html', 'text/html; charset=UTF-8')
    print("响应类型创建成功！")




if __name__ == '__main__':
    print "开始模拟数据创建"
    createUser()
    createResponseType()

    print "完成！"