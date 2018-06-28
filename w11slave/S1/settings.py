# Scrapy settings for S1 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
SPIDER_MODULES = ['S1.spiders']
NEWSPIDER_MODULE = 'S1.spiders'

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'

DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

ITEM_PIPELINES = {
    # 'S1.pipelines.ExamplePipeline': 300,
    'S1.pipelines.Mysql_pipeline': 300,
    # 'scrapy_redis.pipelines.RedisPipeline': 400,

}

LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
# DOWNLOAD_DELAY = 1
REDIS_HOST = '127.0.0.1'  # 也可以根据情况改成 localhost
REDIS_PORT = 6379

# Mysql
MYSQL_HOST = "localhost"
MYSQL_DATABASE = "test"
MYSQL_USER = "root"
MYSQL_PASS = "root"
MYSQL_PORT = 3306

# ===============代理 设置=============
# 代理API地址
# 快代理-代理池提取代理数量
PROXY_CNT = 1
# 快代理-代理取代API链接
PROXY_URL = 'http://svip.kdlapi.com/api/getproxy/?orderid=933015464233988&num='+str(PROXY_CNT)+'&b_pcchrome=1&b_pcie=1&b_pcff=1&protocol=2&method=2&an_an=1&an_ha=1' \
            '&sp2=1&quality=2&sort=1&format=json&sep=1'
