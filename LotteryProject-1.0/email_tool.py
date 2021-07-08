#-*- coding:utf-8 -*-
import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email.header import Header
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
class email_tool():

    username = 'fleamarket@aliyun.com'
    password = '*********'
    replyto = 'fleamarket@aliyun.com'
    rcptto = ['zhu990611@gmail.com','1559422960@qq.com']

    def __init__(self) -> None:
        pass
    def _format_addr(self,s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))
    #设置要发送的邮箱地址 如果不设值 就按默认的    
    def setToEmail(self,toEmail):
        self.rcptto = toEmail
    #发送邮箱;参数C要发送的内容,s:内容的格式(包括plain,文本;html:超文本),h:要发送邮箱的标签
    def send(self,h,c,s):
        msg = MIMEMultipart('alternative')
        msg['From'] = self._format_addr('Fleamarket <%s>' % self.username)
        msg['Subject'] = Header(h, 'utf-8').encode()
        msg['Reply-to'] = self.replyto
        msg['Message-id'] = email.utils.make_msgid()
        msg['Date'] = email.utils.formatdate() 
        _text = MIMEText(c, _subtype= 'html', _charset='UTF-8')
        msg.attach(_text)
        client = smtplib.SMTP()
        client.connect('smtp.aliyun.com', 25)
        client.set_debuglevel(0)
        client.login(self.username, self.password)
        client.sendmail(self.username, self.rcptto, msg.as_string())
        client.quit()
