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
