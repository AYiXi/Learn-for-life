- 当前插入时间
  - CURRENT_TIMESTAMP [timestamp]
  - 
    ```sql
    ALTER TABLE `stackoverflow_temp_question` MODIFY COLUMN `move_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    ```

- 更改 mysql 编码以适应 emoji
  ```sql
  <!-- 1366, "Incorrect string value: '\\xF0\\x9F\\x94\\x9D T...' for column -->
  SHOW VARIABLES LIKE '%char%';
  SHOW FULL COLUMNS FROM `medium`;
  
  ALTER DATABASE <DB_NAME> CHARACTER SET utf8mb4;
  ALTER TABLE <TABLE_NAME> CONVERT TO CHARACTER SET utf8mb4;
  ```

- 终止 Sql 语句
  ```sql
  SHOW processlist;
  KILL id
  ```

- 更改表名
  ```sql
  RENAME TABLE stackoverflow.medium_url TO stackoverflow.medium
  ```

- view
  - create view user_count as select username, count(*) as count from medium group by username;
  - select * from user_count;