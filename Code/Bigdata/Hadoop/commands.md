- Install JDK
- vim ~/.zshrc
   - `export JAVA_HOME=/app/jdk1.7.0`
   - `export PATH=$JAVA_HOME/bin:$PATH`
   - `source ~/.zshrc
- tar -zxvf hadoop-x.x.x -C /usr/local/hadoop
- Hadoop:
   - hadoop-env.sh
      - export JAVA_HOME=/app/jdk1.7.0
   - core-site.xml
    ```xml
        <configuration>
            <property>
                <name>fs.defaultFS</name>
                <value>hdfs://Hadoop01:8020</value>
            </property>

            <property>
                <name>hadoop.tmp.dir</name>
                <value>/root/file/hadoop</value>
            </property>
        </configuration>
    ```
    - hdfs-site.xml
       ```xml
        <configuration>
            <property>
                <name>dfs.replication</name>
                <value>1</value>
            </property>
        </configuration>
       ``` 
    - slaves

- Export Port
  - firewall-cmd --zone=drop --add-port=8080-8081/tcp
- Start/Stop hadoop
   - cd hadoop/bin/ 
     - ./hdfs namenode -format (first time)
   - cd hadoop/sbin/
     - ./start-dfs.sh
     - ./stop-dfs.sh
   - Jps