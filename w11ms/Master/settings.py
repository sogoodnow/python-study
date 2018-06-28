# Scrapy settings for Master project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
SPIDER_MODULES = ['Master.spiders']
NEWSPIDER_MODULE = 'Master.spiders'

# USER_AGENT = 'scrapy-redis (+https://github.com/rolando/scrapy-redis)'
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
}
DOWNLOADER_MIDDLEWARES = {
   'w11ms.Master.middlewares.MasterMiddleware': 543,
    # 不使用默认超时中间件
    'scrapy.downloadermiddlewares.retry.RetryMiddleware':None
}
# 指定使用scrapy-redis的去重
DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'

# DUPEFILTER_CLASS = 'scrapy_redis.dupefilters.RFPDupeFilter'
# 指定使用scrapy-redis的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# 在redis中保持scrapy-redis用到的各个队列，从而允许暂停和暂停后恢复，也就是不清理redis queues
SCHEDULER_PERSIST = True

# 指定排序爬取地址时使用的队列，
# 默认的 按优先级排序(Scrapy默认)，由sorted set实现的一种非FIFO、LIFO方式。
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'

#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

ITEM_PIPELINES = {
    'Master.pipelines.MasterPipeline': 300,
    # 'scrapy_redis.pipelines.RedisPipeline': 400,
}

LOG_LEVEL = 'DEBUG'
# LOG_FILE = './log.txt'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
# 下载延迟
DOWNLOAD_DELAY = 2

# ===============redis 设置=============
# REDIS_URL = None  # 一般情况可以省去
REDIS_HOST = '127.0.0.1'  # 也可以根据情况改成 localhost
REDIS_PORT = 6379

# ===============代理 设置=============
# 代理API地址
# 快代理-代理池提取代理数量
PROXY_CNT = 1
# 快代理-代理取代API链接
PROXY_URL = 'http://svip.kdlapi.com/api/getproxy/?orderid=933015464233988&num='+str(PROXY_CNT)+'&b_pcchrome=1&b_pcie=1&b_pcff=1&protocol=2&method=2&an_an=1&an_ha=1' \
            '&sp2=1&quality=2&sort=1&format=json&sep=1&dedup=1'
# 讯代理
# PROXY_URL = 'http://api.xdaili.cn/xdaili-api//privateProxy/applyStaticProxy?spiderId=2646d627908f47f2b0c9a6f55246163e&returnType=2&count=1'
