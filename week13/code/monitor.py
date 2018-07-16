import psutil, time


# 从windows下复制文件到Linux
# pscp.exe monitor.py root@192.168.88.176:/root

class Monitor():
    cpu_data = []

    @classmethod
    def mem(cls, max=90):
        val = psutil.virtual_memory().percent
        if val > max:
            cls.send_msg('内存使用率为{:1.f}%，超过了{}%，请关注'.format(val, max))

    @classmethod
    def cpu(cls, max=90):
        val = psutil.cpu_percent(1)

        cls.cpu_data.append(val)

        # print(cls.cpu_data)

        if len(cls.cpu_data) >= 3:

            avg = sum(cls.cpu_data) / len(cls.cpu_data)

            if avg > max:
                cls.send_msg('CPU使用率为{:1f}%，超过了{}%，请关注'.format(avg, max))

            cls.cpu_data.pop(0)

    @classmethod
    def send_msg(cls, content):
        # print(content)
        cls.mail(content)
        cls.wechat(content)

    @classmethod
    def mail(cls, content):
        import smtplib
        from email.mime.text import MIMEText
        from email.utils import formataddr

        nickname = '监控程序'

        # 发送者的信息
        sender = '123456789@qq.com'
        password = '987654321'

        # 接收方的邮箱
        receiver = 'aa@bb.cc'

        msg = MIMEText(content, 'html', 'utf-8')
        msg['From'] = formataddr([nickname, sender])
        msg['Subject'] = '自动报警'

        server = smtplib.SMTP_SSL('smtp.qq.com', 465)

        try:
            server.login(sender, password)
            server.sendmail(sender, [receiver], msg.as_string())
        except Exception as ex:
            print(ex)
        finally:
            server.quit()

    @classmethod
    def wechat(cls, content):
        # pip install wechatpy
        # pip install pycrypto  cryptography  2选1

        from wechatpy import WeChatClient
        import datetime

        client = WeChatClient('oqZI700TICQqEk_LHluLxgsk2-qQ', '5354b6234736845c82345e')
        template_id = 'SVxtZHeS77EvBLyzl234tifLYt-234pORiN345No'
        openid = 'oV4P22J234JcnJD3YK34567c'

        data = {
            'msg': {"value": content, "color": "#173177"},
            'time': {"value": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "color": "#173177"},
        }

        try:
            client.message.send_template(openid, template_id, data)
        except Exception as ex:
            print(ex)

# Monitor.wechat('CPU超过90%')


while True:
    Monitor.mem(90)
    Monitor.cpu(90)

    time.sleep(5)
