import tushare
import time
import smtplib
from email.mime.text import MIMEText
#获取股票信息方法
def getrealdate(share):
    date=tushare.get_realtime_quotes(share.code)
    share.name=date.loc[0][0]
    share.price=float(date.loc[0][3])
    share.high=date.loc[0][4]
    share.low=date.loc[0][5]
    share.volumn=date.loc[0][8]
    share.amount=date.loc[0][9]
    share.openprice=date.loc[0][1]
    share.pre_close=date.loc[0][2]
    share.timee=date.loc[0][30]
    share.describe="股票名："+share.name+"当前价格："+str(share.price)
    return share
#发送邮件
def sendemail(subject,content):
    msg_from="17600631242@163.com"#发送方
    pwd="123456a"#授权码
    to="1398803217@qq.com"

    #构造邮件
    msg=MIMEText(content)#邮件对象
    msg["Subject"]=subject #邮件主题
    msg["From"]=msg_from   #邮件发送方
    msg["To"]=to       #邮件接收方
    #发送邮件
    try:
        ss=smtplib.SMTP_SSL("smtp.163.com",994)#邮件内容对象
        ss.login(msg_from,pwd)
        ss.sendmail(msg_from,to,msg.as_string())
        print("发送成功")
    except Exception as e:
        print("发送失败，详情：",e)
#定义股票类
class Share():
    def __init__(self,code,buy,sale):
        self.name=""
        self.high=""
        self.low =""
        self.volumn =""
        self.amount = ""
        self.openprice = ""
        self.pre_close =""
        self.timee =""
        self.describe=""
        self.code=code
        self.buy=buy
        self.sale=sale

def main(sharelist):
    for share in sharelist:
        sh=getrealdate(share)
        print(sh.describe)

        if sh.price<=sh.buy:
            print("可以考虑买入了")
            sendemail("达到买点",sh.describe)
        elif sh.price>=sh.sale:
             print("可以考虑卖出了")
             sendemail("达到卖点", sh.describe)
        else:
            print("不买也不卖")
while 1==1:
    share1=Share("000591",3.2,3.8)
    share2=Share("600102",3.1,3.2)
    share3=Share("601988",3.3,3.5)
    list=[share1,share2,share3]
    main(list)
    time.sleep(5)

