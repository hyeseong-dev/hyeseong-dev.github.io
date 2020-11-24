---
layout: post
title: "[Heroku] Heroku로 Django 앱 운영"
date: 2020-11-23 15:45
category: Heroku
tags: [Heroku,GIT,Django,Python]

---
![Django, Heroku](https://simpleisbetterthancomplex.com/media/2016-08-09-how-to-deploy-django-applications-on-heroku/featured.jpg)

Heroku는 클라우드 애플리케이션 플랫폼이며 기본적으로 PaaS (Platform-as-a-Service)입니다. Python을 포함한 여러 프로그래밍 언어를 지원하며 Heroku에 Django 애플리케이션을 배포하는 것은 어렵지 않습니다.

# Heroku Service
## 설치하기
- [헤로쿠 가입](https://signup.heroku.com/)
- [헤로쿠 설치](https://devcenter.heroku.com/articles/heroku-cli)


## Ready to Deploy Django Application

### 패키지 설치
헤로쿠는 gunicorn 서버를 추천하고 있어요. 
가볍고 설정이 심플하다는점!
> pip install gunicorn

### requirements.txt 파일 생성 
의존성 패키지들을 텍스트 파일에 모아볼게요. 헤로쿠에도 똑같이 설치할 거라서요.
```
pip freeze > requirements.txt
```

### Procfile 등 몇가지 파일 만들기

헤로쿠는 docker랑 비슷하게 Dockerfile에 관련 정보를 파일에 정의하듯이 Procfile에 앱에 관한 설치와 실행에 관한 정보를 기입합니다. 이 프로젝트 전반적인 파일들을 다이노(dynao)에 업로드합니다 헤로쿠의 용어로 다이노는 가상머신, 정확하게는 가상의 리눅스 컨테이너를 의미하며 웹 애플리케이션이 실행되는 독립된 환경이에요. 


첫째, Proc파일에 웹 서버의 프로세스 정보, 즉 프로세스 타입과 프로세스 실행 명령을 정의해요. gunicorn 명령의 인자로 `프로젝트설정디렉토리/wsgi.py` 모듈을 지정했고 로그는 포준출력(stderr)으로 보냅니다. 

``` Procfile
web: gunicorn 프로젝트디렉토리명.wsgi --log-file -
```

``` runtime.txt
python-3.x.x # 파이썬 버전명 기입
```

``` .gitignore
.env/
env/
venv/
.venv/
*.pyc
__pycache__
db.sqlite3
...
...
...

```

### setiings.py  수정

setiings.py 파일에 있는 비밀 데이터를 환경변수에 저장하고, 이들 환경 변수를 사용하도록 수정해볼게요. 

즉, 기존 아이디, 비밀번호, 시크릿 아이디, 시크릿키등이 그대로 노출된 걸 쉽게 읽지 못하도록 할게요.

```

SECRET_KEY = os.environ['DJANGO_SECRET_KEY]

DEBUG = FALSE

ALLOWED_HOSTS = ['.herokuapp.com','127.0.0.1']

DATABSE = {
  'default':{
    'ENGINE':'django.db.backends.mysql',
    'NAME': os.environ['DATABASE_NAME'],
    'USER': os.environ['DATABASE_USER'], # 
    'PASSWORD': 'os.environ['DATABASE_PASSWORD'],
    'HOST': '엔드포인트' # 
    'PORT': 3306, # 변동하지 않았다면 기본 3306입니다.
    'OPTIONS':
      'init_command': 'SET sql_mode='STRICT_TRANS_TABLES'",
  }
}

DISCUS_MY_DOMAIN = 'https://`앱이름`.herokuapp.com/'

...
...
STATICFILES_STORAGE = '프로젝트디렉토리명.storage.S3StaticStorage'
DEFAULT_FILE_STORAGE = '프로젝트디렉토리명.storage.S3MediaStorage'

# AWS_ACCESS_KEY_ID = 'os.environ['AWS_ACCESS_KEY_ID']'
# AWS_SECRET_ACCESS_KEY = 'os.environ['AWS_SECRET_ACCESS_KEY']'
# AWS_S3_REGION_NAME = 'ap-northeast-2' # 한국 아닌 지역은 다른 명칭으로 바꿔주세요.
# AWS_STORAGE_BUCKET_NAME = '버킷 이름'

# AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com'
# AWS_DEFAULT_ACL = 'public-read'
```

## CLI 명령으로 Heroku Deploying
Heroku Service에서는 CLI명령으로만 배포가 가능해요. 또한 Heroku CLI 및 Git CLI명령을 같이 사용해야해요.
아래 CLI를 통해서 헤로쿠 다이노에 배포할게요. 

```
$ git init
$ heroku login
$ heroku create `앱이름`

# 특정 데이터를 다이노의 환경변수로 등록합니다.
# 리눅스에서는 홑따옴표, 윈도우는 쌍따옴표를 사용할게요.
$ heroku config:set DJANGO_SECRET_KEY='기존시크릿키를넣어주세요'
$ heroku config:set DATABASE_NAME='해당 키를 입력해주세요.'
$ heroku config:set DATABASE_USER='해당 키를 입력해주세요.'
$ heroku config:set DATABASE_PASSWORD='해당 키를 입력해주세요.'
$ heroku config:set AWS_ACCESS_KEY_ID='해당 키를 입력해주세요.'
$ heroku config:set AWS_SECRET_ACCESS_KEY='해당 키를 입력해주세요.'

$ git add -A
$ git commit -m 'initial upload'

$ git push heroku master

$ heroku run python manage.py migrage

$ heroku run python manage.py createsuperuser

# 브라우저로 해로쿠에 접속합니다.
$ heroku open

```
> 참고로 S3 서비스에서 물리적인 저장소 위치는 리전에 의해 ㄱㄹ정되는데요. 그리고 웹 서버와 스토리지 서버는 물리적으로 
가까울수록 응답 속도가 빨라요. 그래서 헤로쿠 서비스를 선택하는 경우, 헤로쿠의 웹 서버 위치느 ㄴ미국으로 고정되므로 S3 서비스의 리전을 미국으로 맞추는 것이 좋아요. 즉 S3 버킷을 생성하는 단계에서 리전을 미국 동부로 지정하면 되요.

> 클라우드 용어로 EC2 서비스는 인프라를 제공하는 IaaS(Infra as a Service)서비스이고, EB서비스와 Heroku 서비스는 플랫폼을 제공하는 PaaS(Platform as a Service)서비스 입니다. 일반적으로 처음에는 작업이 쉬운 PaaS 서비스를 선택하고, 경험을 쌓은 후 Iaas 서비스를 선택합니다. 그래서 PaaS서비스로 분류되는 EB와 Heroku 서비스를 비교해서 좀 더 나은 선택을 하면 될거에요.