import brings_class
import two_color_ball_class
from datetime import datetime

def mainFun(number):
    weekedDay = datetime.today().isoweekday()
    for i in range(0, number):
        bringsDay = [1,3,6]
        twoColorBallDay = [2,4,7]
        if weekedDay in bringsDay:
            print("大乐透")
            base = brings_class.brings_class()
            value = base.lotteryFun()
            print(value)
            #return value
        elif weekedDay in twoColorBallDay:
            print("双色球")
            base = two_color_ball_class.two_color_ball_class()
            value = base.lotteryFun()
            print(value)
            #return value
mainFun(5)