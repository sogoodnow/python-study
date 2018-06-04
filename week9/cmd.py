from scrapy import cmdline

com = "scrapy crawl dangdang"
log = "scrpay crawl dangdang  -s LOG_FILE=all.log "
cmdline.execute(com.split())