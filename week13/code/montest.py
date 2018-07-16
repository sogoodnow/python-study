import psutil,os
from wechatpy import WeChatClient
import datetime,time

CPU_LENTH = 3
CPU_MAX = 1
MEM_MAX = 1

class Monitor():
    cpu_datas = []
    # Cpu监控
    @classmethod
    def cpu_monitor(cls):
        # 查看cpu使用率
        cpu_per = psutil.cpu_percent(True)
        cls.cpu_datas.append(cpu_per)
        # 取使用率平均值
        if len(cls.cpu_datas)>= CPU_LENTH:
            cpu_avg = sum(cls.cpu_datas)/CPU_LENTH
            # 平均值超过警戒值，则发送消息
            if cpu_avg > CPU_MAX:
                print(cpu_avg)
                cls.send_msg("CPU使用率为{:.1f}超过警戒值{:.1f}，请查看服务器状态！".format(cpu_avg,CPU_MAX))
            # 列表超出数量，弹出
            cls.cpu_datas.pop(0)

    # 内存监控
    @classmethod
    def memery_monitor(cls):
        if psutil.virtual_memory().percent >= MEM_MAX:
            cls.send_msg("内存使用率为{:.1f}超过警戒值{:.1f}，请查看服务器状态！".format(psutil.virtual_memory().percent, CPU_MAX))



    # 消息通知
    @classmethod
    def send_msg(cls,content):
        cls.send_wechart(content)

    @classmethod
    def send_wechart(cls,content):
        appid = 'wxc7271858473e4717'
        secret = 'b2ff1a104d0572e1a5bd6b5c43fb61db'
        template_id = '9eLa4d4Y5kAr_zEJK2w38yxzc8hyi7JA-WTxuHQw7V8'
        client = WeChatClient(appid, secret)
        date = datetime.datetime.now().strftime("%Y%m%d:%H%M%S")
        data = {
            'msg': {"value": content, "color": "#173177"},
            'time': {"value": date, "color": "#173177"},
        }
        try:
            client.message.send_template('oqZI700TICQqEk_LHluLxgsk2-qQ', template_id, data)

        except Exception as ex:
            print(ex)



while True:
    Monitor.cpu_monitor()
    Monitor.memery_monitor()
    time.sleep(5)