from selenium import webdriver

import pymongo
client = pymongo.MongoClient()
br = webdriver.Chrome()
br.get('http://www.baidu.com')