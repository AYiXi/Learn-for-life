#!/bin/bash

path=~/.virtualenv/Scrapy

echo "验证爬虫环境是否已存在"
if [ -d $path]; then
    source ~/.virtualenv/Scrapy/bin/active
else
    yum update
    yum install -y virtualenv
    virtualenv ~/.virtualenv/Scrapy
    source ~/.virtualenv/Scrapy/bin/active
    pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
fi

if [ ${#} == 1 ];then
    echo "正在定向爬取数据..."
    scrapy crawl pj -s CLOSESPIDER_ITEMCOUNT=$1
else
    echo "初次开启爬虫..."
    scrapy crawl pj
fi

