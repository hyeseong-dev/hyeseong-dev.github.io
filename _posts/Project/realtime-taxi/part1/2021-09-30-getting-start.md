---
layout: post
title: "실시간 택시 앱(feat. Django Channels and React)"
date: 2021-09-30 11:09
category: Project/realtime-taxi
tags: [Channels, React, Django, Docker]

---

# 들어가기 앞서

- 실시간 양방향 통신을 이용한 앱
  - 장점 : 단방향 통신보다 리소스 소모가 적음
  - 단점 : http보다 다소 난이도가 상대적으로 높음

- 상용화 된 서비스 예
  - 우버 or Lyft

- 구현 앱 소개 : 
  - 탑승 고객과 드라이버간에 서로 커뮤니케이션을 원활하게 해주기 위한 앱
    - 고객은 탑승위치와 목적지를 선택
    - 이때 고객이 앱에 요청된 정보를 앱이 전달 받아 근처 드라이버에게 모드 broadcast하게됨
    - 고객이 요청한 데이터를 확인한 여러 드라이버중 특정 드라이버는 이를 수락
    - starting location에서 고객과 드라이버가 만나게됨
    - 그리고 드라이버가 운전을 하는 동안 일어난 움직임(좌표, GPS등)을 실시간으로 추적하여 해당 상태가 항시 파악할 수 있도록 함

- 요약 : 
 - 파트1 : Django, Django Channels를 이용하여 server-side에서 테스트 코드를 작성하고 소스코드를 작성함

 - 파트2 : client-side React app을 작성하여 인증 인가를 구현함. 더불어 도커까지 붙여 더욱더 개발 플로우를 원활히 만듬

 - 파트3 : React를 이용한 앱 UI를 만들어 진행함

 - 결론 : 2 유저가 실시간 앱으로 경험 할 수 있는 서비스 구현
  - 드라이버
  - 탑승 고객

# 시작

## 프로젝트 셋업

클라이언트, 서버사이드 앱 모두를 아우르기 위한 `taxi-react-app`이라는 프로젝트 디렉토리를 만들게요.

>$ mkdir taxi-react-app && cd taxi-react-app

가상환경을 생성하고 활성화 하겠습니다.

```sh
$ mkdir server && cd server
$ python3.9 -m venv env
$ source env/bin/activate
```

파이썬 가상 환경은 Pipenv, Poetry venv, virtualenvwrapper가 대표적으로 있습니다. 

아래 필요한 패키지와 프레임워크를 설치하도록 합니다. 
```bash
(env)$ pip install \
       Django==3.1.4 \ # 대표적인 파이썬 웹프레임워크
       djangorestframework==3.12.2 \ # API작성을 매끄럽게 해줄 프레임워크
       channels==3.0.2 \             # 소켓 통신을 위한 패키지
       channels-redis==3.2.0 \       # redis 사용을 위한 패키지
       pytest-asyncio==0.14.0 \      # 비동기 로직을 테스트 하기 위한 package
       pytest-django==4.1.0 \        # pytest 툴에서 django를 사용하기 위한 package
       Pillow==8.0.1 \               # image 생성 및 수정을 가능하게 하는 package
       djangorestframework-simplejwt==4.6.0 \ # JsonWebToken을 원할하게 만들수 있게 도와주는 package
       psycopg2-binary==2.8.6                 # postgres를 원활하게 사용할 수 있게 도와주는 packge

(env)$ django-admin.py startproject taxi .
(env)$ python manage.py startapp trips

```

프로젝트 tree 구조는 아래와 같습니다. 
```sh
└── server
    ├── manage.py
    ├── taxi
    │   ├── __init__.py
    │   ├── asgi.py       # 비동기를 가능하게 하는 파이썬 웹서버(feat. 단일 비동기 호출 가능 구조)
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── trips
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── migrations
        │   └── __init__.py
        ├── models.py
        ├── tests.py
        └── views.py
```

## Compose 구성

프로젝트 디렉토리 아래에 compose 디렉토리를 아래와 같이 구성합니다.

```sh
.
└── local
    └── django
        ├── celery
        │   ├── beat
        │   │   └── start
        │   ├── flower
        │   │   └── start
        │   └── worker
        │       └── start
        ├── Dockerfile
        ├── entrypoint
        ├── redis
        │   ├── Dockerfile
        │   └── start
        └── start
```

celery 디렉토리의 구성은 beat, flower, workder 디렉토리가 구성되요. 각각 start 스크립트 파일을 구성하는데요. 
컨테이너가 띄워 졌을 경우 각각의 컨테이너의 설정과 명령어들을 명시합니다. 

### docker-compose.yml

```sh
version: '3.8'

services:
  web:
    build:
      context: .
      dockerfile: ./compose/local/django/Dockerfile
    # '/start' is the shell script used to run the service
    command: /start
    # this volume is used to map the files and folders on the host to the container
    # so if we change code on the host, code in the docker container will also be changed
    volumes: 
      - .:/app 
    ports:
      - 8930:8930
    expose:
      - 8930
    # env_file is used to manage the env variables of our project
    env_file:
      - ./.env/.dev-sample
    depends_on:
      - redis
      - db
    container_name: taxi_web
    networks:
      - taxi-network    
    

  db:
    image: postgres:12.0-alpine
    volumes:
      - postgres_data:/var/lib/postgresql/data/
    environment:
      - POSTGRES_DB=taxi
      - POSTGRES_USER=taxi
      - POSTGRES_PASSWORD=taxi
      - TZ=Asia/Seoul
    ports:
      - 54323:5432
    container_name: taxi_db
    networks:
      - taxi-network    
    

  redis:
    image: redis:5-alpine
    container_name: taxi_redis
    networks:
      - taxi-network
    

  celery_worker:
    build:
      context: .
      dockerfile: ./compose/local/django/Dockerfile
    command: /start-celeryworker
    volumes:
      - .:/app
    env_file:
      - ./.env/.dev-sample
    depends_on:
      - redis
      - db
    container_name: taxi_celery_worker
    networks:
      - taxi-network

  celery_beat:
    build:
      context: .
      dockerfile: ./compose/local/django/Dockerfile
    command: /start-celerybeat
    volumes:
      - .:/app
    env_file:
      - ./.env/.dev-sample
    depends_on:
      - redis
      - db
    container_name: taxi_celery_beat
    networks:
      - taxi-network

  flower:
    build:
      context: .
      dockerfile: ./compose/local/django/Dockerfile
    command: /start-flower
    volumes:
      - .:/app
    env_file:
      - ./.env/.dev-sample
    ports:
      - 5557:5555
    depends_on:
      - redis
      - db
    container_name: taxi_celery_flower
    networks:
      - taxi-network

volumes:
  postgres_data:

networks:
  taxi-network:
    driver: bridge

```

### Dockerfile, entripoint, start 파일

- FROM 키워드에서 언어:3.9-`slim-buster`란 무엇일까요?
  - slim-buster라고 붙은 건 각 이미지의 여러 종류(Operating System)중 하나를 의미 
  - 참고 https://hyeseong-dev.github.io/docker/2020/11/19/images-concept/

- ENV PYTHONUNBUFFERED 1
  - 컴포즈에서 파이썬 로그가 한 발 늦게 출력됨을 방지
  - 버퍼가 기본으로 작동하면서 출력 로그를 붙잡고 있기 때문. 이를 해결하기 위해 환경변수를 추가

- PYTHONDONTWRITEBYTECODE 1
  - .pyc 파일을 생성하지 않도록함(도커 이용시에는 필요없기 때문)

- build-essential : 컴파일시 필요한 패키지들을 다운로드함
- libpq-dev : libpq 는 PostgreSQL에 대한 C 애플리케이션 프로그래머의 인터페이스 입니다. libpq 는 클라이언트 프로그램이 PostgreSQL 백엔드 서버에 쿼리를 전달 하고 이러한 쿼리 결과를 수신 할 수 있도록 하는 라이브러리 함수 세트입니다.
- gettext : gettext는 유닉스 계열 컴퓨터 운영 체제의 다국어 프로그램을 작성할 목적으로 흔히 쓰이는 국제화와 지역화(i18n, L10n) 시스템이다.
- `apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false` : 우분투 apt 추천 패키지 자동설치 해제
- sed : sed는 명령행에서 파일을 인자로 받아 명령어를 통해 작업한 후 결과를 화면으로 확인하는 방식

```sh
FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Translations dependencies
  && apt-get install -y gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# Requirements are installed here to ensure they will be cached.
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./compose/local/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY ./compose/local/django/redis/start /start-redis
RUN sed -i 's/\r$//g' /start-redis
RUN chmod +x /start-redis

COPY ./compose/local/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./compose/local/django/celery/beat/start /start-celerybeat
RUN sed -i 's/\r$//g' /start-celerybeat
RUN chmod +x /start-celerybeat

COPY ./compose/local/django/celery/flower/start /start-flower
RUN sed -i 's/\r$//g' /start-flower
RUN chmod +x /start-flower

WORKDIR /app

ENTRYPOINT ["/entrypoint"]

```


`entrypoint` 파일을 아래와 같이 작성합니다. 

- [set errexit 명령어](https://secmem.tistory.com/606)
- [set pipefail 명령어](https://secmem.tistory.com/606)
- [set nounset 명령어](https://secmem.tistory.com/606) : 변수 확장을 할 때 존재하지 않는 변수 일 경우 에러로 간주하여 exit

- shell 스크립트 : while은 true일때 동작한다면 until은 false일때 동작
- >&2 : 모든 출력을 강제로 
- [exec](https://wikidocs.net/111050) : 주어진 명령어를 실행하는데 새로운 프로세스를 생성하지 않고, 쉘 프로세스를 대체합니다. 예를 들어 bash 쉘에서 자바 프로그램을 실행하면 자바 프로그램의 ppid가 bash 쉘이 되고, 자바 프로그램이 bash 쉘의 하위 프로세스로 실행됩니다. exec 커맨드로 실행하면 bash쉘의 프로세스가 자바 프로그램이 됩니다. ppid가 따로 업습니다. 그리고 자바프로그램이 종료되면 프로세스가 종료됩니다. bash 쉘로 돌아오지 않습니다.

```sh
#!/bin/bash

# if any of the commands in your code fails for any reason, the entire script fails
set -o errexit
# fail exit if one of your pipe command fails
set -o pipefail
# exits if any of your variables is not set
set -o nounset

postgres_ready() {
python << END
import sys

import psycopg2

try:
    psycopg2.connect(
        dbname="${SQL_DATABASE}",
        user="${SQL_USER}",
        password="${SQL_PASSWORD}",
        host="${SQL_HOST}",
        port="${SQL_PORT}",
    )
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)

END
}
until postgres_ready; do
  >&2 echo 'Waiting for PostgreSQL to become available...'
  sleep 1
done
>&2 echo 'PostgreSQL is available'

exec "$@"
```

Dockerfile, entrypoint 파일과 동일한 디렉토리 위치에 아래와 같이 start shell스크립트를 작성합니다.
```sh
#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8930
```

### Django Config

백엔드 프로젝트 환경 설정 settings.py에 몇가지 필요한 환경 셋업을 아래와 같이 합니다. 

- DJANGO 앱 등록
- DB 설정
  - compose 파일의 db 서비스의 환경변수로 등록하여 활용
- Django에서 이미 구성한 built-in user model 활용

```python

import os 

import os # add with the other imports

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.postgres', # new
    'django.contrib.staticfiles',
    'rest_framework', # new
    'trips', # new
]

# changed
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('PGDATABASE'),
        'USER': os.getenv('PGUSER'),
        'PASSWORD': os.getenv('PGPASSWORD'),
        'HOST': os.getenv('PGHOST', 'localhost'),
        'PORT': os.getenv('PGPORT', '5432'),
    }
}

AUTH_USER_MODEL = 'trips.User' # new

```

### Custom User Model

`trips/models.py`을 아래와 같이 구성

```python
# server/trips/models.py

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
```

마이그레이션 진행

> $ python manage.py makemigrations
> $ python manage.py migrate


### Admin 

- superuser 생성 
  - `createsuperuser` management 명령어 활용 
    - username, email, password 사용

> $ python manage.py createsuperuser

```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    pass

```

서버를 실제 돌려 관리자 페이지에 접속하여 관리자 추가 등록 혹은 변경 및 삭제가 되는지 확인해볼게요. 

### Channels Config

매우 중요합니다. 
Django에 소켓 통신 구현을 위한 밑작업으로 설정을 셋업할게요. 
아래와 같이 구성합니다. 

```python 
# server/taxi/settings.py

REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379')

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [REDIS_URL],
        },
    },
}
```


```python
# server/taxi/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.postgres',
    'django.contrib.staticfiles',
    'channels', # new
    'rest_framework',
    'trips',
]
```

위와 같이 `INSTALLED_APPS`에 `channels`를 등록하고 `python manage.py runserver` 명령어를 돌리면 아래와 같이 오류가 발생해요. 
asgi 설정을 하라고 오류를 뱉어내는 거에요. 
```sh
(env) $ python manage.py runserver
CommandError: You have not set ASGI_APPLICATION, which is needed to run the server.
```

`settings.py` 파일이 있sms rudfhdp `routing.py` 파일을 만들고 아래와 같이 소스코드를 작성 할 게요. 

```python
# server/taxi/routing.py

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
})
```

`settings.py` 파일 안에 아래 코드 스니펫을 작성합니다. 

```python
# server/taxi/settings.py

ASGI_APPLICATION = 'taxi.routing.application'
```

`asgi.py` 모듈 수정역시 진행합니다. 

주의해야 할 사항으로 os.environ.setdefault('첫 번째 인자', '두 번째 인자')
 - 두 번째 인자를 프로젝트 디렉토리명(settings.py이 속한)과 동일하게 함

```python
import os
import django

from channels.routing import get_default_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taxi.settings')
django.setup()
application = get_default_application()
```
그리고 다시 서버 재기동을 통하여 오류 없이 되는 것을 확인함. 
