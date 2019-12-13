import requests

headers = {
    # 'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    # 'Accept-Encoding': 'gzip, deflate',
    # 'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8',
    # 'Cache-Control': 'no-cache',
    # 'Connection': 'keep-alive',
    'Cookie': 'teRKN6lzIsE280S=U3v.gbo5M29HwpKOsno9qno.KFjX9FVy6JOJ7lRnu_TjVRsB8IoG0ctyRWu_4HXk; bg6=78|AANYh; JSESSIONID=e5d09b3c27826f9dce9b82929c69; _gscu_930750436=75420602etiqss10; _gscbrs_930750436=1; language=zh; _gscs_930750436=75420602lxp0c810|pv:3; teRKN6lzIsE280T=4beSob0ifItT8oEZZ2RL8w.YhR_uWHE9656MH_psPwRtlzJH8i.qHPcR6NV5Hto7LH1gSbYn2vkLTZB0c8nXvmxm3iWvw9nV6bU6sQL5QuTBqQYTfXmXsZLijKaLd..YlouFJNPGajE0efPXCvqyBfQFW5XCtBdbXTLDzbdfbjNGUIPWPECAZxGda.t_kokulB7W6NPijMjADJReYQcEZ.rZnyEr7fpkXI7jNM8TDiB1UsDRZV4KYcCqtBIslVHbQHOmkh3QjXOZ99AqmngBXPhICm2WswoVZ3pDu0Zb6XuN45yttV2WoeH5fKrQwVWczFeEFJOcbi84a9638IYWmKzhQ.EaO.efcl5QbIj79Z1gX9Pb.rBgM1uwX48eSFZeFKuL',
    # 'Host': 'cpquery.cnipa.gov.cn',
    # 'Pragma': 'no-cache',
    # 'Referer': 'http://cpquery.cnipa.gov.cn/',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
}

cookie = 'teRKN6lzIsE280S=U3v.gbo5M29HwpKOsno9qno.KFjX9FVy6JOJ7lRnu_TjVRsB8IoG0ctyRWu_4HXk; _gscbrs_930750436=1; language=zh; _gscs_930750436=75420602lxp0c810|pv:3; teRKN6lzIsE280T=4pGDFpNyZLUckaYhf1lIkjCPKXvlpgYsjxj71JW9djleRFAgkyC61YIXj8xx1eFMTgHH7pEmgA8ILhnkINBR_nVnmApEb0rMfFQWdIQkAKZQQyoeKBfVr_xOvMVfaXZA4dXhjqRncRYu9WVkxE088LrtL9li0mOp2o78WpgkcZrlKFU3pJCB7Ut3skHAY8yG7eoKKAXW5PfUYycQun54xnnc8tafrNkOkFWJWNUdcWYcug3623NOEZrnMG.b69D4R__2gQgdKWROjE502YQcqeuPDcCbWtLSDNSXmXYaV9HmSWng.CUZqE22LRbjRwrT8zYcLIBHm7heTORXtSmN0n25jVJIBJiC7slYNTv6Dm0rw4FAXU6ZxN19ngYTLsI2He39'
cookie = cookie.split('; ')
cookie = {i.split('=')[0]: i.split('=')[1] for i in cookie}

url_image = 'http://cpquery.cnipa.gov.cn/JcaptchaServlet?type=1&usertype=1&date=Wed%20Dec%2004%202019%2009:08:48%20GMT+0800%20(China%20Standard%20Time)0.49600585249825113'

url = 'http://cpquery.cnipa.gov.cn/JcaptchaServlet?usertype=1&date=Wed%20Dec%2004%202019%2008:38:21%20GMT+0800%20(China%20Standard%20Time)0.28103226175317575&JcucyyCu=4ooSANGYVfD9cRZ8BIp_kwj50Hvu4a6sesvfJrh6V0xfm9b3NyAuLw8p7sMPWXwG8ZrFlprnEwYrH421oYui0A96xWh9TlqLV3fyih4uLXbRRdE6LWMtbLtmucDK5brhcKEQB7ThszzC7F5oEjJqRBdF8sjQpFfb4y1AaWVYqOkGAO9DYxxwoLaCSZcGkk.tVxBZaf1TzaU1Fq2GVxqzoFuyN.5bTpKjCMCMcp4i3gUb4cwLTny47kuxGXerD_XKaTcMt98Pu_MQ_tSUjvdADYLEP0BecP7B1pQUHk1AdS4JnRZSjyWL3KMUxMm4T5ox_RtfYd9Rkz6nf8zDLZCJbrJfAxcf79Y1OqsseiPilrOqLgqRGhtLFBcIvNFrxEbagFKlD5zIIgpvGIhZk2MDGU1mZwDqpBYMjoK_G9hcTlu_GeM7RWyJSeMjhagMtk.DUpKJ'
url_home = 'http://cpquery.cnipa.gov.cn/'
r2 = requests.get(url_home)
print(r2.text)

with open(r'D:\Files\Learn-for-life\Python\Crawl\cookie.html', 'w+') as f:
    # f.write("111")
    f.write(r2.text)
    print(11)

# if 'tml' in r.text:
#     print('failed')
# else:
#     print('ok')