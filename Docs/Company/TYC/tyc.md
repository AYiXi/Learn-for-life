### Cods
- tail -f nohup.out | perl -pe 's/(.* DEBUG .*)|(.* INFO .*)|(.* ERROR .*)|(.* WARNING .*)|(SUCCESS .*)/\e[1;34m$1\e[0m\e[1;37m$2\e[0m\e[1;31m$3\e[0m\e[1;35m$4\e[0m\e[1;32m$5\e[0m/g'
- grep "offset:" nohup.out
- grep "len company" nohup.out

### Check Proxy
- grep "testing Proxy:" wrapper.log.bak | awk '{ print $6,$7,$10 }' >> test_proxy.txt
- grep "give up proxy" wrapper.log | awk '{ print $6,$7,$12 }' >> give_up_proxy.txt

### 北京红网运行
- 打包: `"/home/work/apache-maven-3.6.1/bin/mvn" package -f "/home/work/libowang/gsxt_spider/consumer/pom.xml"`
- 传输: `scp /home/work/libowang/gsxt_spider/consumer/target/consumer.jar work@172.24.114.25:/home/work/commonlibs-gsxt/companyfetcher/consumer.jar`
- 重启: `/home/work/beijing_spider/companyfetcher-product/bin/companyfetcher restart`
- 