import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = '418544725@qq.com'  # 发件人邮箱账号
my_pass = 'jtzxkkfeitcdbgdg'  # 发件人邮箱密码
# user_id = '18733181565@163.com'  # 收件人邮箱账号
# msg = "12312312312312"
send_email_code = ""


def mail(my_user, send_msg):
    ret = True
    try:
        msg = MIMEText(send_msg, 'plain', 'utf-8')
        msg['From'] = formataddr(["418544725", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["18733181565", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "管理系统修改密码"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:
        ret = False
    return ret


# ret = mail(user_id, msg)
# if ret:
#     print("邮件发送成功")
# else:
#     print("邮件发送失败")