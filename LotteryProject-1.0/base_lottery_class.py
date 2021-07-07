#彩票基类
import random
import redis_tool
import request_tool
class base_lotter_class:
    
    #获取最新一期彩票开奖的API接口
    open_base_url = "http://apis.juhe.cn/lottery/query?lottery_id={}&lottery_no=&key=d6bdcbef0fcf747ecd2f74426df5fe93";
    #默认的红球池
    def_red_ball_pool = []
    #默认的蓝球池
    def_blue_ball_pool = []
    #随机生成的红球集合
    red_ball_list = []
    #随机生成的蓝球集合
    blue_ball_list = []
    #需要生成的红球数量
    red_number = 0
    #需要生成的蓝球数量
    blue_number = 0
    #彩票类型
    lotter_type = None 
    #彩票编号
    lottery_id = None
    
    def __init__(self) -> None:
        pass

    #随机生成一组红球和蓝球
    def lotteryFun(self):
        redBool = self.boolFun(self.red_number,self.def_red_ball_pool)
        if self.isTheSame == True:
           self.lotteryFun()
        self.isTheSame = False   
        redBool.sort()
        blueBool = self.boolFun(self.blue_number,self.def_blue_ball_pool)
        if self.isTheSame == True:
           self.lotteryFun()
        self.isTheSame = False   
        blueBool.sort()
        return redBool + blueBool
    
    #随机生成号码
    def boolFun(self,_number,def_pool):
        ret = []
        for index in range(0, _number):
            mumber = []
            for i in range(1,len(def_pool)):
                mum = random.randint(1,len(def_pool))
                mumber.append(mum)
            result = {}
            for num in mumber:
                if num in result.keys():
                    result[num] +=1
                else:
                    result[num] = 1
            max_num = max(result.values())
            for item in result.items():
                if item[1] == max_num:
                    if item[0] in ret:
                        self.isTheSame = True
                    else:
                        ret.append(item[0])
                        break  
        return ret
    
    #发送邮件
    def sendEmail(email):
        pass    
    
    #获取指定日期缓存的机选号
    def get_now_day(self,k):
        return redis_tool.redis_tool().getListValue(k)
    #设置今天的机选号
    def set_now_day(self,k,v):
        redis_tool.redis_tool().setListValue(k,v)  
    #组装缓存的KEY
    def assembly_key(self,weekedDay,index):
         return str(self.lotter_type + '$' + str(weekedDay) + '$' + str(index))
    #获取昨天的星期编号
    def getLastWeekedDay(self,weekedDay):
        if weekedDay == 0:
            return 7
        else:
            return weekedDay - 1     
    #比较开奖号码和机选号码
    def compare_numbers(self,lastNumbers):
        listRet = []
        if lastNumbers == None:
            return lastNumbers
        res = request_tool.request_tool().getNowOpen(self.open_base_url)
        openNumbers = list(map(int,res['res'].split(',')))
        for i in range(0,len(openNumbers)):
            if(openNumbers[i] == lastNumbers[i]):
                listRet.append(openNumbers[i])
        return listRet
             