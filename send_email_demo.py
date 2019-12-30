import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = '418544725@qq.com'  # 发件人邮箱账号
my_pass = 'jtzxkkfeitcdbgdg'  # 发件人邮箱密码
my_user = '18733181565@163.com'  # 收件人邮箱账号



def mail():
    ret = True
    try:
        msg = MIMEText('测试邮件', 'plain', 'utf-8')
        msg['From'] = formataddr(["418544725", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["18733181565", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "菜鸟教程发送邮件测试"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:
        ret = False
    return ret


ret = mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")