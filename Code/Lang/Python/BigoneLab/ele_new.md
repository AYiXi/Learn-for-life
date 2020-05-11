```py
# settings.py
# how to define code
RETRY_HTTP_CODES = [401, 429, 400]

# how to work?
REDIS_PARAMS = {
    'use_helper': True,
}

# what?
DNS_CACHE_ENABLED = False

SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# how to work?
EXTENSIONS = {
    'scrapy.telnet.TelnetConsole': None
}



# pipelines.py
# 以下两个函数等价
def item_name(item):
    name = {
        ElePoiidItem        : 'all_poiid',
        EleRestaurantItem   : 'restaurant_new',
        ElePoiLatLogItem    : 'restaurant_lat_log',
        ElePoiLatLogItemTest: 'restaurant_test',
        EleCityItem         : 'city',
        EleCityTestItem     : 'city_test',
    }

    collection_name = name[item.__class__]

def item_name(item):
    if isinstance(item, ElePoiidItem):
        collection_name = 'all_poiid'
    elif isinstance(item, EleRestaurantItem):
        collection_name = 'restaurant_new'
    elif isinstance(item, ElePoiLatLogItem):
        collection_name = 'restaurant_lat_log'
    elif isinstance(item, ElePoiLatLogItemTest):
        collection_name = 'restaurant_test'
    elif isinstance(item, EleCityItem):
        collection_name = 'city'
    elif isinstance(item, EleCityTestItem):
        collection_name = 'city_test'
    else:
        collection_name = 'menu'

def md5(self, item_set_str):
    h = hashlib.md5()
    h.update(bytes(item_set_str, encoding='utf-8'))  # md5加密
    return h.hexdigest()


# middleware.py
def process_request(self, request, spider):
    # Called for each request that goes through the downloader
    # middleware.

    # Must either:
    # - return None: continue processing this request
    # - or return a Response object
    # - or return a Request object
    # - or raise IgnoreRequest: process_exception() methods of
    #   installed downloader middleware will be called
    ABUYUN_ACCOUNT_LIST = [
        {
            "username": "---",
            "password": "---",
        },
        {
            "username": "---",
            "password": "---",
        }
    ]
    abu_yun_account = random.choice(ABUYUN_ACCOUNT_LIST)
    proxy = "http://{username}:{password}@http-dyn.abuyun.com:9020/".format(
        username=abu_yun_account["username"],
        password=abu_yun_account["password"]
    )
    request.meta['proxy'] = proxy

    return None



# spider.py
def make_request_from_data(self, data):
    data = json.loads(data)
    url = self.map_base_api.format(data['latitude'], data['longitude'], )
    return scrapy.Request(
        url,
        method="GET",
        callback=self.parse,
        errback=self.errback_httpbin,
        dont_filter=True,
        meta=data
    )

def errback_httpbin(self, failure):
    self.logger.error(repr(failure))
    yield scrapy.Request(
            url=failure.request.url,
            callback=self.parse,
            errback=self.errback_httpbin,
            dont_filter=True,
            meta=failure.request.meta
    )



# spider.py
def parse(self, response):
    poi = json.loads(response.text)
    if response.status == 401:
        yield scrapy.Request(response.url,
                                method="GET",
                                callback=self.parse,
                                errback=self.errback_httpbin,
                                dont_filter=True,
                                )
        return




today = str(datetime.date.today())
s = "scrapy crawl ele_lat_log  -s LOG_LEVEL=DEBUG -s LOG_FILE=ele_ele_lat_log_%s.txt" % today


def foo(i):
    cmdline.execute(s.split())


for i in range(2):
    p = Process(target=foo, args=(i,))
    p.start()
```