## 以下两个函数等价
```py
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
```