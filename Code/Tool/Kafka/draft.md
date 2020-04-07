解耦
可恢复性
缓冲-生成大于消费-削峰
灵活性(动态增减机器) & 峰值处理能力
异步通信

点对点模式   一对一
发布/订阅模式 一对多

消费者拉取
缺点: 消费者一直询问, 浪费资源
kafka cluster broker1 broker2 broker3

producer 1 producer 2

topic A partition 0
