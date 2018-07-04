import psutil
import time
import datetime
print(psutil.cpu_count())
print(psutil.cpu_percent(percpu=True))
print(psutil.pids())
print(psutil.cpu_freq(True))
print(psutil.boot_time())
print(time.localtime(psutil.boot_time()))
print(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%H:%M:%S"))