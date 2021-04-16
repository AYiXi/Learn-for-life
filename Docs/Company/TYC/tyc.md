### Cods
- tail -f nohup.out | perl -pe 's/(.* DEBUG .*)|(.* INFO .*)|(.* ERROR .*)|(.* WARNING .*)|(SUCCESS .*)/\e[1;34m$1\e[0m\e[1;37m$2\e[0m\e[1;31m$3\e[0m\e[1;35m$4\e[0m\e[1;32m$5\e[0m/g'
- grep "offset:" nohup.out
- grep "len company" nohup.out

### Check Proxy
- grep "testing Proxy:" wrapper.log.bak | awk '{ print $6,$7,$10 }' >> test_proxy.txt
- grep "give up proxy" wrapper.log | awk '{ print $6,$7,$12 }' >> give_up_proxy.txt

### 北京红网运行
- 打包: `"/home/work/apache-maven-3.6.1/bin/mvn" package -f "/home/work/libowang/gsxt_spider/consumer/pom.xml"`
- 传输: `scp /root/projects/gsxt_spider/consumer/target/consumer.jar work@172.24.114.25:/home/work/commonlibs-gsxt/companyfetcher/consumer.jar`
- 重启: `/home/work/beijing_spider/companyfetcher-product/bin/companyfetcher restart`
- 日志: `cd /home/work/beijing_spider/companyfetcher-product/logs`
- TYC02 打包 gee_redis_server: `"/home/work/apache-maven-3.6.1/bin/mvn" package -f "/home/work/libowang/gee_redis_server/pom.xml"`
- TYC02 运行 gee_redis_server: nohup java -jar v

### Tail -F
- gee_redis_server: 
  - tail -f j.out | perl -pe 's/(.* DEBUG .*)|(.* INFO .*)|(.* ERROR .*)|(.* WARNING .*)|(.* SUCCESS .*)/\e[1;34m$1\e[0m\e[1;33m$2\e[0m\e[1;31m$3\e[0m\e[1;34m$4\e[0m\e[1;32m$5\e[0m/g'
- cods_company_all
  - tail -f company_all.out | perl -pe 's/(.* DEBUG .*)|(.* INFO .*)|(.* ERROR .*)|(.* WARNING .*)|(.* SUCCESS .*)/\e[1;34m$1\e[0m\e[1;33m$2\e[0m\e[1;31m$3\e[0m\e[1;34m$4\e[0m\e[1;32m$5\e[0m/g'
- makepolo phone
  - tail -f mp.out | perl -pe 's/(.*id.*phone.*)/\e[1;34m$1\e[0m\e/g'