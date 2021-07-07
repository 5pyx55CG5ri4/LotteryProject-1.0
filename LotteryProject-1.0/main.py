import brings_class
import two_color_ball_class
from datetime import datetime
import str_tool
import time

sObj = str_tool.str_tool()
lastRandomNumber = {}

#主方法
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
    #昨日的机选号码
    h = sObj.h_str_template.format(base.lottery_str,str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))+'机选号码')
    c = ''
    for i in range(0, number):
        value = base.lotteryFun(None,None)
        #今日机选号码
        print(value)
        c += sObj.c_str_template.format('第'+ str(i+1) + '注机选号为:'+ sObj.listToStr(value))
        #缓存今日机选号码
        base.set_now_day(base.assembly_key(weekedDay,i),value)
        #获取昨日机选号码
        lastNumber = base.get_now_day(base.assembly_key(base.getLastWeekedDay(weekedDay),i))
        #lastNumber = base.get_now_day(base.assembly_key(weekedDay,i))
        lastRandomNumber[i] = lastNumber

    
    #发送今天的机选到邮箱
    base.sendRandomNumber(None,h,c)
    #昨日的数据
    lastD = lastBase.getOpenByUrl()
    #昨日开奖的号码
    lastOpenNumber = lastBase.getLastOpenNumber(lastD,'res')
    l_t = sObj.h_str_template.format(lastBase.getValueByName(lastD,'date'), 
    '第' + lastBase.getValueByName(lastD,'no')+ '期' + 
    lastBase.getValueByName(lastD,'name') + '开奖结果')
    l_c = sObj.c_str_template.format('开奖结果为:' + sObj.listToStr(lastOpenNumber))
    for item in lastRandomNumber.items():
        l_c += sObj.c_str_template.format('第'+str(int(item[0]) + 1)+'注机选为:' + sObj.listToStr(item[1]))
        compareList = lastBase.compare_numbers(item[1],lastOpenNumber)
        l_c += sObj.c_str_template.format('第'+str(int(item[0]) + 1)+'注机选命中数字为:' + sObj.listToStr(compareList))
    #发送比对结果到邮箱
    l_c += sObj.c_str_template.format('中没中奖看下面:')
    l_c += sObj.i_str_template.format(lastBase.lottery_img)
    base.sendRandomNumber(None,l_t,l_c)

    

mainFun(5)