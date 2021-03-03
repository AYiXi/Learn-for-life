## 控制台使用 Django

### 设置环境变量
```sh
export DJANGO_SETTINGS_MODULE=ShangIp.settings
```

### 示例
```python
import django
django.setup()

from django.contrib.auth.models import User
user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

>>> user.email
'lennon@thebeatles.com'
```

## 创建用户模型

### 关于用户系统
1. 使用 django 内置的 User 系统, 需要重新定制
2. 前后台通用一个 User 系统

### 自定义 User 模型
1. 创建一个 xfzauth(内置的app叫auth) 的 app, 全部重写,  继承自 AbstractBaseUser
2. 定义 UserManager
3. 设置 AUTH_USER_MODEL
4. 映射到数据库中
5. 主键是uuid, 用于保密用户数量信息(shortuuidfield)
6.  ```python
    from shortuuidfield import ShortUUIDField
        class User(AbstractBaseUser, PermissionMixin)
            uid = ShortUUIDField(primary_key=True)
        
            USERNAME_FIELD = 'telephone'
            REQUIRED_FIELDS = ['username']
    ```

