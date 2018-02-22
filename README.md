# web-development

### pip install
```
django===1.10.7     
django-blog-zinnia===0.18.1 
markdown  
django-app-namespace-template-loader(替换主题组件)
zinnia-theme-bootstrap(可选)
```

### home/home/settings.py
```
INSTALLED_APPS = (
    # 工程建立时默认添加的app
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    
    # 项目添加的app
    'django.contrib.sites',
    'django_comments',
    'mptt',
    'tagging',
    'zinnia_bootstrap',
    'zinnia',
)
```