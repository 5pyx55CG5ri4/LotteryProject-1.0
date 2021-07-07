#大乐透
import base_lottery_class
import random
class brings_class(base_lottery_class.base_lotter_class):
    isTheSame = False
    def __init__(self) -> None:
        super().__init__()
        self.def_red_ball_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
        self.def_blue_ball_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.red_number = 5
        self.blue_number = 2
        self.isTheSame = False
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