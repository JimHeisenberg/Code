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
