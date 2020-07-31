- 当前插入时间
  - CURRENT_TIMESTAMP [timestamp]
  - 
    ```sql
    ALTER TABLE `stackoverflow_temp_question` MODIFY COLUMN `move_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    ```