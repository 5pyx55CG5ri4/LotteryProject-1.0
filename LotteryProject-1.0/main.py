import brings_class
import two_color_ball_class
from datetime import datetime

def mainFun(number):
    weekedDay = datetime.today().isoweekday()
    bringsDay = [1,3,6]
    twoColorBallDay = [2,4,7]
    base = None
    lastBase = None
    if weekedDay in bringsDay:
        print("大乐透")
        base = brings_class.brings_class()
        lastBase = two_color_ball_class.two_color_ball_class()
    elif weekedDay in twoColorBallDay:
        print("双色球")
        base = two_color_ball_class.two_color_ball_class()
        lastBase = brings_class.brings_class()
    for i in range(0, number):
        value = base.lotteryFun()
        #今日机选号码
        print(value)
        #缓存今日机选号码
        base.set_now_day(base.assembly_key(weekedDay,i),value)
        #获取昨日开奖号码
        lastNumber = base.get_now_day(base.assembly_key(base.getLastWeekedDay(weekedDay),i))
        #昨日开奖号码和缓存的机选号码对比
        winALotteryList = lastBase.compare_numbers(lastNumber)
        #昨日中奖号码
        print(winALotteryList)
        #return value




mainFun(5)