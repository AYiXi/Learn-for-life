# https://github.com/Baiguanlab/xsyx.git

# runspider.py
```py
import os
import sys
import signal
import subprocess

sys.path.append('..')
SPIDER_NAME = 'products'
subpros = []

def sig_exit(signum, frame):
    if signum == signal.SIGINT:
        for pro in subpros:
            os.killpg(os.getpgid(pro.pid), 9)


signal.signal(signal.SIGINT, sig_exit)

def main_job():
    for _ in range(8):
        subpro = subprocess.Popen(
            'scrapy crawl {}'.format(SPIDER_NAME), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subpros.append(subpro)
    for pro in subpros:
        pro.wait()
# if __name__ == '__main__':
#     main_job()



# settings.py
USER_AGENT = 'Mozilla/5.0 (Linux; Android 6.0; Coolpad 8737 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/50.0.2661.86 Mobile Safari/537.36 MicroMessenger/7.0.5.1440(0x27000536) Process/appbrand0 NetType/WIFI Language/zh_CN'

DEFAULT_REQUEST_HEADERS = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en',
    'Host': 'mall.xsyxsc.com',
    'referer': 'https://servicewechat.com/wx6025c5470c3cb50c/116/page-frame.html',
    'content-type': 'application/x-www-form-urlencoded'
}



# pipelines.py
class XsyxPipeline(object):

    def open_spider(self, spider):
        if spider.name == 'single_shop_product_full':
            self.single_product_client_full = KafkaProducerHelper('xsyx-single_shop_product_full',
             value_serializer=lambda v: json.dumps(v).encode('utf-8'))
            self.single_price_client_full = KafkaProducerHelper('xsyx-single_shop_price_full',value_serializer=lambda v: json.dumps(v).('utf-8'))
        elif spider.name == 'shop_product_full':
            self.price_client = KafkaProducerHelper('xsyx-prices',
                                                    value_serializer=lambda v: json.dumps(v).encode(
                                                        'utf-8'))
        else:
            self.mongo_client = mongodb_helper.MongoDBHelper()

    def process_item(self, item, spider):
        list_from_json = item['detail']
        list_from_json['ts_string'] = str(datetime.date.today())
        list_from_json['ts'] = str(datetime.datetime.now())

        if spider.name == 'single_shop_product_full':
            if isinstance(item, PriceeItem):
                client = self.single_price_client_full
            else:
                client = self.single_product_client_full
            client.send(list_from_json)
        elif spider.name == 'shop_product_full':
            if isinstance(item, PriceeItem):
                client = self.price_client
            else:
                client = self.product_client
            client.send(list_from_json)
        else:
            collection = self.mongo_client.get_collection(
                collection_name=spider.name, database_name='xsyx')
            collection.insert_one(list_from_json)

    def close_spider(self, spider):
        if spider.name == 'single_shop_product_full':
            self.single_product_client_full.producer.close()
            self.single_price_client_full.producer.close()
        elif spider.name == 'shop_product_full':
            self.product_client.producer.close()
            self.price_client.producer.close()



# spider.py
def parse_product_data(self, response):
    area_id = response.meta['areaId']
    store_id = response.meta['storeId']
    _resp = json.loads(response.text)
    if _resp['rspCode'] == 'success':
        products = _resp['data']
        for p in products:
            p['storeId'] = store_id
            p['area_id'] = area_id
            item = PriceeItem()
            item['detail'] = p
            yield item
    else:
        self.log("errorcode: %s, errormsg: %s" % (_resp['rspCode'], _resp['rspDesc']))
