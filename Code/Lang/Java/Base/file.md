### java 文件操作
```java
// 读取文件
public static String readToString(String fileName) {
    String encoding = "UTF-8";
    File file = new File(fileName);
    Long filelength = file.length();
    byte[] filecontent = new byte[filelength.intValue()];
    try {
        FileInputStream in = new FileInputStream(file);
        in.read(filecontent);
        in.close();
    } catch (FileNotFoundException e) {
        e.printStackTrace();
    } catch (IOException e) {
        e.printStackTrace();
    }
    try {
        return new String(filecontent, encoding);
    } catch (UnsupportedEncodingException e) {
        System.err.println("The OS does not support " + encoding);
        e.printStackTrace();
        return null;
    }
}
```