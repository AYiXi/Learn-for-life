- Install JDK
- vim ~/.zshrc
   - ```sh
     export JAVA_HOME=/app/jdk1.7.0
     export PATH=$JAVA_HOME/bin:$PATH
     ```
   - `source ~/.zshrc`
- tar -zxvf hadoop-x.x.x -C /usr/local/hadoop
- Hadoop:
   - hadoop-env.sh
      - export JAVA_HOME=/app/jdk1.7.0
   - core-site.xml
    ```xml
        <configuration>
            <property>
                <name>fs.defaultFS</name>
                <value>hdfs://192.168.118.131:8020</value>
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

- [Export Port](https://havee.me/linux/2015-01/using-firewalls-on-centos-7.html)
  - firewall-cmd --zone=public --add-port=50070/tcp --permanent
  - firewall-cmd --reload

- ```sh
    export HADOOP_HOME=/root/apps/hadoop-2.7.7
    export PATH=$HADOOP_HOME/bin:$PATH
    alias hs="hdfs dfs"
    ```

- Start/Stop hadoop
   - cd hadoop/bin/ 
     - ./hdfs namenode -format (first time)
   - cd hadoop/sbin/
     - ./start-dfs.sh
     - ./stop-dfs.sh
   - Jps

