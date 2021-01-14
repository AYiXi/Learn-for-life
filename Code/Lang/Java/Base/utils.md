### java JSON 操作

```java
import com.alibaba.fastjson.JSONObject;

JSONObject yearReport = JSONObject.parseObject(html);
JSONObject data1 = yearReport.getJSONObject("data");


// hutool
<dependency>
    <groupId>cn.hutool</groupId>
    <artifactId>hutool-all</artifactId>
    <version>5.5.6</version>
</dependency>

import cn.hutool.json.JSONUtil;
import cn.hutool.json.JSONObject;

JSONObject j = JSONUtil.parseObj(s);
```


### String 操作
```java
// int -> String
String.valueOf(int);

// format
String.format(str, "str");


```