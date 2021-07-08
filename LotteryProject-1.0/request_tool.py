#-*- coding:utf-8 -*-
#获取最新一期开奖记录API
import requests
import json
class request_tool():

    def __init__(self) -> None:
        pass
    #发送Get请求
    def get(self,url):
       return requests.get(url).text
    #获取最新一期的开奖号码
    def getNowOpen(self,url):
        jsonstr = self.get(url)
        obj = json.loads(jsonstr)
        resultObj  = obj['result']
        res = {}
        res['name'] = resultObj['lottery_name']
        res['date'] = resultObj['lottery_date']
        res['no'] = resultObj['lottery_no']
        res['res'] = resultObj['lottery_res']
        return res

#print(request_tool().getNowOpen('http://apis.juhe.cn/lottery/query?lottery_id=dlt&lottery_no=&key=d6bdcbef0fcf747ecd2f74426df5fe93'))