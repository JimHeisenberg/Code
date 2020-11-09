# 用腾讯云API实现 Dynamic DNS

因为想用Windows自带的Remote Desktop(如果公网访问，需要IP和端口)。
但又没有可以做端口映射的路由器，恰好学校WiFi提供了公网ip，于是想到可以用自己的域名做一个DNS。
但是学校WiFi分配的公网ip过一段时间就会变，而且不用DHCP会出问题。
所以就有了这篇博客，自己利用已有的动态公网ip + 调用API更改域名解析记录，
来变相实现一个Dynamic DNS (DDNS)的服务。

## Usage
1. 确保现在连接的网络为你分配了公网ip  
2. 在同一目录下，按照之后File Details的内容创建2个文件  
3. 修改```DDNS.py```中```__main__```的内容  
``` py
# SecretId: 你腾讯云的SecretId, str, see also https://console.cloud.tencent.com/cam/capi  
SecretId = "A********************p"
# SecretKey: 你腾讯云的SecretKey, str, see also https://console.cloud.tencent.com/cam/capi  
SecretKey = "********************"
# prefix: 子域名(subdomain), str, like www, rd  
# A subdomain is the part of a URL before the root domain. You can configure your subdomain as www or as a distinct section of your site, like blog.example.com.
prefix = "rd"
# domain: 域名(apex domain), str, like qq.com, jimheisenberg.xyz  
# An apex domain is a custom domain that does not contain a subdomain, such as example.com. Apex domains are also known as base, bare, naked, root apex, or zone apex domains.
domain = "jimheisenberg.xyz"
# timeInterval: 每次更新的时间间隔, int or float, there will be timeInterval seconds between each request  
timeInterval = 600
```

## Tips
1. 对比在设置里的ip和百度```ip```的查询结果，可知自己有没有公网ip  
2. 将```DDNS.py```改为```DDNS.pyw```可以无窗口后台运行

# File Details
一共2个文件，```TencentCloudAPI.py```和```DDNS.py```  
TencentCloudAPI封装了对腾讯云API的调用  
DDNS基于对腾讯云API的调用实现了 Dynamic DNS  
``` py
# TencentCloudAPI.py
import time
import random
import requests
import base64
import hmac
from hashlib import sha1
from urllib.parse import quote


class TencentCloudAPI(object):
    """
    class for calling Tencent Cloud API  
    parameters:
        SecretId: str, see also https://console.cloud.tencent.com/cam/capi  
        SecretKey: str, see also https://console.cloud.tencent.com/cam/capi  
        address: str, 接口请求域名 like https://cns.api.qcloud.com/v2/index.php?  

    example of usage:
        from TencentCloudAPI import TencentCloudAPI
        SecretId = "A**********************************b"
        SecretKey = "C******************************d"
        address = "cns.api.qcloud.com/v2/index.php"
        tcapi = TencentCloudAPI(SecretId, SecretKey, address)
        parameters = dict(Action="RecordList", domain="jimheisenberg.xyz")
        result = tcapi.request(parameters)
        print(result.json())
    """

    def __init__(self, SecretId, SecretKey, address):
        """
        initialization
        """
        self.SecretId = SecretId
        self.SecretKey = SecretKey
        self.address = address

    def _getHashBase(self):
        """
        return "GET" + self.address  
        used for calculating Signature  
        return:
            string
        """
        return "GET" + self.address

    def _getUrlBase(self):
        """
        return "GET" + self.address  
        used for making url of http get request  
        return:
            string
        """
        return "https://" + self.address

    def _convert(self, parameters):
        """
        convert parameters(dict) into string with the format for tencent cloud  
        parameters of this function:
            parameters: dict
        return:
            string
        """
        result = ""
        for key, value in sorted(parameters.items()):
            result += '&' + str(key).replace('_', '.') + '=' + str(value)
        result = result.replace('&', '?', 1)
        return result

    def _hashHmac(self, key, msg,  digestmod=sha1):
        """
        首先使用签名算法（HmacSHA256 或 HmacSHA1）对上一步中获得的 签名原文字符串 进行签名，然后将生成的签名串使用 Base64 进行编码，即可获得最终的签名串。  
        parameters of this function:
            key: The starting key for the hash.
            msg: if available, will immediately be hashed into the object's starting state.
            digestmod: see hashlib, default sha1
        return:
            string
        """
        hmac_code = hmac.new(key.encode(), msg.encode(), digestmod).digest()
        return base64.b64encode(hmac_code).decode()

    def request(self, parameters):
        """
        对腾讯云的 API 接口的调用是通过向腾讯云 API 的服务端地址发送请求，并按照接口说明在请求中加入相应的请求参数来完成的。  
        see also https://cloud.tencent.com/document/product/302/4032  
        parameters of this function:
            parameters: dict. note: [SecretId, Signature, Timestamp, Nonce] should not appear in parameters, they will be auto filled  
        return:
            <class 'requests.models.Response'>
        """
        parameters["Timestamp"] = int(time.time())
        parameters["Nonce"] = random.randint(0, 65535)
        parameters["SecretId"] = self.SecretId
        parameters["Signature"] = quote(self._hashHmac(
            self.SecretKey, self._getHashBase() + self._convert(parameters)))
        url = self._getUrlBase() + self._convert(parameters)
        result = requests.get(url)
        return result
```
``` py
# DDNS.py
import socket
import time
import datetime
from TencentCloudAPI import TencentCloudAPI


class DDNS(TencentCloudAPI):
    """
    Dynamic Domain Name Service  
    Dynamic update your DNS record on Tencent Cloud  
    parameters:
        SecretId: str, see also https://console.cloud.tencent.com/cam/capi  
        SecretKey: str, see also https://console.cloud.tencent.com/cam/capi  
        prefix: str, like www, rd  
        domain: str, like qq.com, jimheisenberg.xyz  
        timeInterval: int or float, there will be timeInterval seconds between each request  
        address: str, 接口请求域名 like https://cns.api.qcloud.com/v2/index.php?  
    """

    def __init__(self, SecretId, SecretKey, prefix, domain, timeInterval, address="cns.api.qcloud.com/v2/index.php"):
        """
        initialization
        """
        super().__init__(SecretId, SecretKey, address)
        self.prefix = prefix.lower()
        self.domain = domain.lower()
        self.timeInterval = timeInterval

    def getHostIp(self):
        """
        查询本机ip地址
        return: ip with str format
        """
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
        finally:
            s.close()
        return ip

    def getExistRecord(self):
        """
        get the existing record of prefix.domain
        return:
            dict, describing record of prefix.domain
        """
        parameters = dict(Action="RecordList", domain=self.domain)
        response = self.request(parameters)
        record = None
        for r in response.json()["data"]["records"]:
            if r["name"] == prefix:
                record = r
                break
        return record

    def updateRecord(self, ip, record):
        """
        update the record of prefix.domain
        return:
            <class 'requests.models.Response'>
        """
        parameters = dict(Action="RecordModify", domain=self.domain)
        parameters["subDomain"] = prefix
        parameters["value"] = ip
        parameters["recordId"] = record["id"]
        parameters["recordType"] = record["type"]
        parameters["recordLine"] = record["line"]
        response = self.request(parameters)
        return response

    def autoUpdateRecord(self):
        """
        automatically getHostIp and getExistRecord, then updateRecord if needed  
        """
        ip = self.getHostIp()
        record = self.getExistRecord()
        if ip == record["value"]:
            print(
                f"""{datetime.datetime.now().isoformat()}, IP {ip} not changed.""")
        else:
            response = self.updateRecord(ip, record)
            print(
                f"""{datetime.datetime.now().isoformat()}, IP {ip} update {response.json()["codeDesc"]}.""")

    def schedAutoUpdateRecord(self):
        """
        autoUpdateRecord with schedule
        """
        while True:
            try:
                self.autoUpdateRecord()
                time.sleep(self.timeInterval)
            except Exception as e:
                print(e)
                time.sleep(self.timeInterval)


if __name__ == "__main__":
    SecretId = "A********************p"
    SecretKey = "********************"
    prefix = "rd"
    domain = "jimheisenberg.xyz"
    timeInterval = 600
    ddns = DDNS(SecretId, SecretKey, prefix, domain, timeInterval)
    print("start")
    ddns.schedAutoUpdateRecord()
```