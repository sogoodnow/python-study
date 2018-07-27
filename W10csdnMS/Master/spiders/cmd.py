from scrapy import cmdline

com = "scrapy runspider Mcsdn.py"
log = "scrpay crawl jd  -s LOG_FILE=all.log "
json = "scrapy crawl jd -o ./a.json"
cmdline.execute(com.split())