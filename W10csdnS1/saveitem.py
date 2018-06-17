import json
import redis
import pymongo

def main():

    # 指定Redis数据库信息
    rediscli = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
    # 指定MongoDB数据库信息
    mongocli = pymongo.MongoClient(host='localhost', port=27017)

    # 创建数据库名
    db = mongocli['spider']
    # 创建空间
    sheet = db['csdn']

    while True:
        # FIFO模式为 blpop，LIFO模式为 brpop，获取键值
        source, data = rediscli.brpop(["myspider_redis:items"])

        item = json.loads(data)
        sheet.insert(item)

        try:
            # print(u"Processing: %(name)s <%(link)s>" )%item
            print(item)
        except KeyError:
            print(u"Error procesing: %r")%item

if __name__ == '__main__':
    main()