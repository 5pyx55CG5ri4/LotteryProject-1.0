#-*- coding:utf-8 -*-
class str_tool():
    #标题模板
    h_str_template = '{}{}'
    #内容模板
    c_str_template = '<span style=font_size = 20px>{}</span></br>'
    #图片模板
    i_str_template = '<img src={}></img></br>'
    def __init__(self) -> None:
        pass
    #字符串转集合
    def strToList(self,str):
        if str == None:
            return None  
        return list(map(int,str.split(',')))
    #集合转字符串    
    def listToStr(self,l):
        if l == None:
         return ''     
        vS = [str(x) for x in l]
        return ','.join(vS)