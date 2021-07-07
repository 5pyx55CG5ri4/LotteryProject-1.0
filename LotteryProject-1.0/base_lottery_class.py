#彩票基类
import random
import redis_tool
import request_tool
class base_lotter_class:
    
    open_base_url = "http://apis.juhe.cn/lottery/query?lottery_id={}&lottery_no=&key=d6bdcbef0fcf747ecd2f74426df5fe93";

    def_red_ball_pool = []
    
    def_blue_ball_pool = []
    
    red_ball_list = []
    
    blue_ball_list = []
    
    red_number = 0
    
    blue_number = 0
    
    lotter_type = None 

    lottery_id = None
    
    def __init__(self) -> None:
        pass
    
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
                        isTheSame = True
                    else:
                        ret.append(item[0])
                        break  
        return ret
    
    def sendEmail(email):
        pass    
    
    def get_now_day(self,k):
        return redis_tool.redis_tool().getListValue(k)

    def set_now_day(self,k,v):
        redis_tool.redis_tool().setListValue(k,v)  
    
    def assembly_key(self,weekedDay,index):
         return str(self.lotter_type + '$' + str(weekedDay) + '$' + str(index))

    def getLastWeekedDay(self,weekedDay):
        if weekedDay == 0:
            return 7
        else:
            return weekedDay - 1     

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
             