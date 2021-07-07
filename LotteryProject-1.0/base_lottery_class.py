#彩票基类
import random
class base_lotter_class:
    def_red_ball_pool = []
    def_blue_ball_pool = []
    red_ball_list = []
    blue_ball_list = []
    red_number = 0
    blue_number = 0    
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
        return ret;
    def sendEmail(email):
        pass    