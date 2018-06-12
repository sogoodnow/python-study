from scrapy import cmdline

com = "scrapy crawl jd"
log = "scrpay crawl jd  -s LOG_FILE=all.log "
json = "scrapy crawl jd -o ../a.json"
cmdline.execute(json.split())