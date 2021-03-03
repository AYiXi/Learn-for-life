// 编码
import java.net.URLEncoder;

URLEncoder.encode(getUserAgent(), "UTF-8")


// 请求
// [OKHttp3 基本使用](https://www.jianshu.com/p/da4a806e599b)
// [Java Requests](https://github.com/hsiafan/requests)
public String httpGet(String url) {  
    String text = null;
    CloseableHttpClient httpclient = HttpClients.createDefault();  
    try {  
        // 创建httpget.    
        HttpGet httpget = new HttpGet(url);  
        System.out.println("executing request " + httpget.getURI());  
        // 执行get请求.    
        CloseableHttpResponse response = httpclient.execute(httpget);  
        try {  
            // 获取响应实体    
            HttpEntity entity = response.getEntity();  
            // 打印响应状态    
            System.out.println(response.getStatusLine());  
            if (entity != null) {  
                text = EntityUtils.toString(entity);
            }  
        } finally {  
            response.close();  
        }  
    } catch (Exception e) {  
        e.printStackTrace();  
    } finally {  
        // 关闭连接,释放资源    
        try {  
            httpclient.close();  
        } catch (IOException e) {  
            e.printStackTrace();  
        }  
    }  

    return text;
}
