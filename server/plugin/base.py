#coding=utf-8
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA
import yaml,os,hashlib,base64,sys,hmac,json
reload(sys)
sys.setdefaultencoding('utf-8')

_config = yaml.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)),"config.yml")))

def getCfgValue(*args):
    """从config.yml配置文件中读取配置值"""
    ret = _config
    for arg in args:
        ret = ret.get(arg)
    return ret

def md5(data):
    m = hashlib.md5()
    m.update(data)
    return m.hexdigest()

def AES_CBC_encrypt(data, password, iv):
    BS = AES.block_size
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
    cipher = AES.new(password.encode("utf-8"), AES.MODE_CBC, iv.encode("utf-8"))
    data = cipher.encrypt(pad(data.encode("utf-8")))
    return base64.b64encode(data)

def AES_CBC_decrypt(data, password, iv):
    iv = iv.encode("utf-8")
    data = iv + base64.b64decode(data.decode("utf-8"))
    bs = AES.block_size
    if len(data) <= bs:
        return data
    unpad = lambda s: s[0:-ord(s[-1])]
    iv = data[:bs]
    cipher = AES.new(password.encode("utf-8"), AES.MODE_CBC, iv)
    data = unpad(cipher.decrypt(data[bs:]))
    return data

def AES_ECB_encrypt(data, password="yyfax10086100861"):
    BS = AES.block_size
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
    cipher = AES.new(password.encode("utf-8"), AES.MODE_ECB)
    data = cipher.encrypt(pad(data.encode("utf-8")))
    return base64.b64encode(data)

def AES_ECB_decrypt(data, password="yyfax10086100861",iv="0102030405060708"):
    iv = iv.encode("utf-8")
    data = iv + base64.b64decode(data.decode("utf-8"))
    bs = AES.block_size
    if len(data) <= bs:
        return data
    unpad = lambda s: s[0:-ord(s[-1])]
    cipher = AES.new(password.encode("utf-8"), AES.MODE_ECB)
    data = unpad(cipher.decrypt(data[bs:]))
    return data

def rsa_encrypt(message):
    pem_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),"exts","public.pem")
    with open(pem_path) as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        cipher_text = base64.b64encode(cipher.encrypt(message))
    return cipher_text

def rsa_decrypt(encrypt_text):
    pem_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "exts", "private.pem")
    # 伪随机数生成器
    random_generator = Random.new().read
    with open(pem_path) as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        text = cipher.decrypt(base64.b64decode(encrypt_text), random_generator)
    return text

def hmac_sha256_encrypt(message,secret):
    message = bytes(message).encode('utf-8')
    secret = bytes(secret).encode('utf-8')
    signature = base64.b64encode(hmac.new(secret, message, digestmod=hashlib.sha256).digest())
    return signature

def strToDict(oristr):
    pass


if __name__=='__main__':
    print AES_ECB_encrypt("abc")