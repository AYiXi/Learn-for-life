# JavaSE
### 认识
- Java 的诞生
  - 1995
    - java se
    - java me -> Android
    - java ee -> 企业级
  - 2006
    - Hadoop
- JDK
  - 开发者工具包
  - 配置环境变量
- JRE
  - Java 运行环境

### 基础语法
- 数据类型
  - 基本数据类型
    - 整数
      - byte 1
      - short 2
      - int 4(default)
      - long 8
    - 浮点数
      - float 4
      - double 8(default)
    - 字符
      - char 2
    - 布尔值
      - boolean 1
  - 引用数据类型
    - class
    - interface
    - array
- 类型转换
  - 自动类型转换
    - 低转高
  - 强制类型转换
    - 高转低
- 变量和常量
  - int a = 1;
  - 作用域
    - 类变量
    - 实例变量
    - 局部变量
  - 命名规范
    - 驼峰命名 studentAge
- 运算符
  - 算数运算符 + - * / % ++ --
  - 赋值运算符 =
  - 关系运算符 > < <= >= !=  == instanceof
  - 逻辑运算符 && || !
  - 位运算符 & | ^ ~ >> << >>>
  - 条件运算符 ? :
  - 扩展运算符 += -= ...
- 包机制
  - 域名倒写
  - 防止命名冲突
  - package
  - import
- JavaDoc
  - JDK 帮助文档
  - javadoc
    - @author, Version, Since, param, return, throws

### 流程控制
- if, else, while, for, switch, continue, break

### 面向对象
- 类与对象
- 构造方法
- new
- 封装
- 继承
- 多态
- 修饰符
  - public, protected, private, static, final, abstract
- 接口
- 内部类
  - 局部
  - 静态
  - 匿名

### 异常
- Throwable
  - Exception
    - 运行时异常
      - ClassNotFound
      - NullPoint
      - UnknowType
      - ...
    - 检查型异常
  - Error
    - AWT
    - JVM
      - StackOverFlow
      - OutOfMemory
- KeyWord
  - try, catch, finally, throw, throws

### 常用类
- Object
  - hashcode()
  - toString()
  - clone()
  - getClass()
  - notify()
  - wait()
  - equals()
- Math
- Random
  - uuid
- File
- 包装类
  - 自动装箱和拆箱
- Date
  - Date
  - SimpleDateFormat
    - yyyy-MM-dd HH:mm:ss
  - Calender(suggest)
- String
  - 不可变性 final
  - difference
    - "a" + 1 + 2
    - 'a' + 1 + 2
    - 1 + 2 + "a"
  - 操作量较少
- StringBuffer
  - 可变长 append()
  - 多线程, 数据量较大
  - 效率低, 安全
- StringBuilder
  - 可变长 
  - 单线程, 数据量较大
  - 效率高, 不安全

### 集合框架
- **Collection**
  - List(有序可以重复)
    - **ArrayList**
      - add
      - remove
      - contains
      - size
    - LinkedList
      - getFirst()
      - getLast()
      - ...
    - Vector
    - Stack
  - Set(无序不能重复)
    - **HashSet**
    - TreeSet
  - Iterator
- **Map**
  - **HashMap**
    - JDK 1.7: Array + LinkList
    - JDK 1.8: Array + LinkList + RedBlackTree
  - TreeMap
- Collection 工具类
- 泛型 < > 约束, 避免类型转换之间的问题
  
### IO Stream
- 字节流
  - InputStream
  - OutputStream
- 字符流
  - Reader
  - Writer
- 节点流
  - CharArrayReader, Writer, inputstream, outputstream
  - StringReader, Writer
  - pipe(管道流)
    - PipedOutputStream
    - PipedInputStream
  - File(文件流)
    - ...
- 处理流
  - buffer
    - bufferInputStream
    - bufferOutputStream
    - bufferReader
    - bufferWriter
  - 序列化
    - 反序列化
    - Serializable, transient
  - data
    - DataInputStream
    - DataOutputStream
  - 转换流
    - InputStreamReader
    - OutputStreamWriter
  - filter
    - 四个
  - print
    - PrintStream
    - PrintWriter

### 多线程
- 进程和线程
- run(), start()
- 线程创建的方式
  - Thread 
  ```java
  new Thread(() -> {
      int a=1;
  }).start();
  ```
  - Runnable
  - Callable 可以有返回值
- 静态代理
  - new Thread(Runnable).start();
  - Lambda
- 线程的状态
  - 新建
  - 就绪
  - 运行
  - 阻塞
  - 死亡
- 常用的方法
  - sleep
  - join
  - yield
  - isLive
  - start
  - setPriority
  - interrupt
- 线程同步
  - 多个对象操作同一个资源, 并发
  - 队列 + 锁
  - Synchronized
    - 同步方法, 弊端: 锁太多
    - **同步代码块**
    - 死锁四个条件
      - 互斥
      - 请求与保持
      - 不剥夺条件
      - 循环等待条件
- 线程通信
  - 缓冲区: 消息队列
  - 标志位: 红绿灯
  - wait()
  - notifyAll()
- 线程池(Pool)
  - 池化技术
  - 池的大小
  - 最大连接数
  - 保持时间
  - ...

### 网络编程
- ...

### GUI
- AWT
  - Frame
  - 监听事件
    - 鼠标, 键盘, 窗口...
- Swing
  - 文本框, 标签, 按钮...

### 注释和反射
- 注解
  - 元注解
  - 内置注解
  - 自定义注解
  - 反射读取注解
- 反射
  - Class newInstance()
  - 类加载机制
  - Method
    - invoke()
    - 存在重载, 也需要写参数的类型
  - Field
    - set()
  - Construct
    - newInstance()
    - 获取的时候需要, 传递参数的 class 类型
  - 破坏私有关键字
    - setAccessible(true)
  - 性能分析
    - 正常 > 检测关闭的反射 > 默认的反射
  - 反射获得注解, 泛型...
- Stream
- ForkJoin
  - 效率对比