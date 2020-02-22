```sh
export DJANGO_SETTINGS_MODULE=ShangIp.settings
```

```py
import django
django.setup()

from django.contrib.auth.models import User
user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

>>> user.email
'lennon@thebeatles.com'
```


