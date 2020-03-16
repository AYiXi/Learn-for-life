### 目前的技术在开发中存在的问题

- 一个项目就是一个工程, 如果项目非常庞大, 就不适合继续使用 package 来划分模块. 最好是每一个模块对应一个工程, 利于分工协作
    
- 借助于 Maven 就可以将一个项目拆分成多个工程
    
- 项目中需要的 jar 包必须手动"复制"、"粘贴"到 WEB-INF/lib 目录下
    - 带来的问题是: 同样的 jar 包文件重复出现在不同的项目工程中,一方面浪费存储空间,另外也让工程比较臃肿.

    - 借助 Maven, 将 jar 包仅仅保存在仓库中, 有需要使用的工程引用文件即可, 并不需要真的复制 jar 包

- jar 包需要别人替我们准备好,或到官网下载

- 一个 jar 包依赖的其他 jar 包需要自己手动加入到项目中

- 引用 jar 包的文本

    - ```xml
        <groupld>com.atguigu.maven</groupld>
        <artifactld>Hellos</artifactld>
        <version>0.0.1-SNAPSHOT</version>
      ```

