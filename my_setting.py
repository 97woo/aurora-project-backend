DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'aurora',
        'USER': 'root',
        'PASSWORD': 'asd3689',
        'HOST': '127.0.0.1',
        'PORT': '3306',
     	'OPTIONS': {'charset': 'utf8mb4'}
    }
}
        
SECRET_KEY = 'django-insecure-w&ar0+tl8rk4a=&63i6=z*&x!xjj@3!!i=fq%vv*%&gsoo2@+-'

ALGORITHM ="HS256"

AWS_ACCESS_KEY_ID='AKIAVVTYAG3O3VNMEG5Q'
AWS_SECRET_ACCESS_KEY='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'
AWS_STORAGE_BUCKET_NAME='woosbucket'
BUCKET_ADDRESS    = 'https://woosbucket.s3.ap-northeast-2.amazonaws.com'
BUCKET_DIR_THUMBNAIL  = 'thumbnail'
BUCKET_DIR_IMAGE = 'image'
BUCKET_DIR_PROFILE = 'profile'