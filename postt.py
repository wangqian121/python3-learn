#邮件发送方（发送方邮件地址，发送方客户端授权密码123456a，SMTP服务器地址smtp.163.com）
#邮件内容
#邮件接收方
import smtplib
from email.mime.text import MIMEText
msg_from="17600631242@163.com"#发送方
pwd="123456a"#授权码
to="1398803217@qq.com"
subject="这封邮件是python发的"   #邮件主题
content="你家着火了"       #邮件内容
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