import smtplib,time
from email.mime.text import MIMEText
from email.header import Header
def sendEmail(content,title,from_name,from_address,to_address,serverport,serverip,username,password):
    msg=MIMEText(content,_subtype='html',_charset='utf-8')
    msg['Subject']=Header(title,'utf-8')
    msg['To']=','.join(to_address)
    msg['From']=from_name
    try:
        s=smtplib.SMTP_SSL(serverip,serverport)
        s.login(username,password)
        s.sendmail(from_address,to_address,msg.as_string())
        print('%s---发送邮件成功' % time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    except Exception as e:
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
        print(e)

def main2():
    TO = ['liuguicen@scmagic.cn']
    config={
        "from":"773767639@qq.com",
        "from_name":"易直播API测试报告",
        "to":TO,
        "serverip":"smtp.qq.com",
        "serverport":"465",
        "username":"773767639@qq.com",
        "password":"qewhurfttjctbbib" #QQ邮箱的SMTP授权码
    }
    title="易直播API自动化测试报告"
    f=open("C:\\Users\\Magic\\PycharmProjects\\easylive_api\\report\\result.html",'rb')
    main_body=f.read()
    f.close()
    sendEmail(main_body,title,config['from_name'],config['from'],config['to'],config['serverport'],config['serverip'],config['username'],config['password'])