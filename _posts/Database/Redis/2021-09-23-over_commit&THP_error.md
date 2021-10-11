---
layout: post
title: "[Redis] Redis Warning 처리(feat. 511, overcommit, THP) "
date: 2021-09-23 15:33
category: Database
tags: [DB, Redis]

---
![Redis](https://media.vlpt.us/images/youngerjesus/post/4a09e691-a606-4c56-afe2-de78b9c757cd/redis3.png)

```python
# WARNING: The TCP backlog setting of 511 cannot be enforced because /proc/sys/net/core/somaxconn is set to the lower value of 128.
# WARNING overcommit_memory is set to 0! Background save may fail under low memory condition. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
# WARNING you have Transparent Huge Pages (THP) support enabled in your kernel. This will create latency and memory usage issues with Redis. To fix this issue run the command 'echo never > /sys/kernel/mm/transparent_hugepage/enabled' as root, and add it to your /etc/rc.local in order to retain the setting after a reboot. Redis must be restarted after THP is disabled.
```

### 1. TCP backlog 경고

WARNING: The TCP backlog setting of 511 cannot be enforced because /proc/sys/net/core/somaxconn is set to the lower value of 128.

기본적인 소켓 accept limit 값입니다. 보통 리눅스 배포판에는 128로 되어있고 이 때문에 tcp backlog 의 셋팅이 511 로 되어있지만 강제로 128로 적용 된다는 뜻입니다. 아래의 명령어로 1024 혹은 더욱 높은 값으로 설정해 주도록 합니다. ( 최고는 65535 )




## S3 버킷 생성 
양동이라느 의미이고 가상의 디스크라고 생각하면 되요. 
즉, 우리는 양동이를 만들어서 정적파일과 미디어 파일을 저장 할 것이에요.

- 대시보드 -> S3 이동!
- 버킷 만들기 클릭 
- 버킷이름 입력(AWS S3전체와 비교한 고유한 이름 설정!), 리전 선택(서울) 후 다음!
- 모든 퍼블릭 액세스 차단 항목을 체크 해제, 비활성화 후 다음!
  - 다른 사용자도 이 버킷에 액세스 할 수 있게되요. 이는 보안 측면에서 위험합니다. 상용화 단계에서는 활성화 하세요.
- 버킷 만들기 클릭!


---

## IAM 사용자 만들기(Identity and Access Management)
AWS 서비스에서는 보안을 강화하기 위해 하위 개념의 사용자를 생성할 수 있고, 각 사용자별로 권한을 따로 줄 수 있어요. 
처음 AWS에서 만든 계정은 root 계정입니다. 즉, 보스라고 보면되요. 
 - 콘솔 대시보드 -> IAM 메뉴 검색 후 클릭
 - 좌측 메뉴에서 `사용자` 클릭
 - 사용자 추가 버튼 클릭
 - 사용자 세부 설정 화면에서 `사용자 이름` 입력 후 `엑세스 유형`에서 `프로그래밍 방식 엑세스` 체크 후 다음 버튼 클릭
> `프로그래밍 방식 엑세스`: 지금 생성하는 사용자는 boto3 패키지를 활용하여 프로그래밍 방식으로 S3 자원에 액세스 합니다. 이 방식에는 사용자의 액세스 키와 비밀 액세스 키가 필요한데, 사용자 생성 마지막 단계에서 확인 할 수 있어요. 
 - 권할 설정 화면이 나오면, `기존정책직접연결`버튼 클릭!
 - 필터에 s3라고 입력하면 목록이 나오는데요. 그 중 `AmazonS3FullAccess` 정책을 체크한 후 우측 아래 다음 버튼을 클릭!
 - 태그 추가 화면에서는 아무것도 안하고 다음 버튼 클릭!
 - 검토 화면도 동일하게 다음 버튼 클릭!
 - 사용자 생성에 성공 화면이 나타나면 `.csv다운로드` 버튼을 눌러 access key와 secret key를 추후에도 확인 할 수 있어요.

## 패키지 설치 
장고 프로젝트에서 AWS S3와 연동하려면 해당 API를 사용해야합니다. 
2가지 패키지를 설치할게요. 
 
```
pip install boto3
pip install django-storages
```
#### boto3? 
S3 API를 쉽게 사용하도록 도와주는 파이썬 SDK입니다.
> boto3는 S3 서비스 이외에도 EC2, DynamoDB등 여러가지 AWS 서비스들을 제어하는 기능도 제공합니다. 

#### django-storages
장고의 저장소 엔진 기능을 제공합니다. 즉, django-storages 패키지에서 boto3dml SDK를 활용해서 S3 저장소를 제어해요. 
> 이 패키지를 이용하면 AWS S3이외에 Google Cloud Storage, Dropbox 등의 원격 저장소를 활용할 수도 있습니다. 

# Changing Source Code in Django
프로젝트 설정 파일을 모아둔 디렉토리의 settings.py파일과 urls.py을 수정하고 storage.py(다른 곳에 둬도 되요) 새로 생성합니다.

## settings.py

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    ...
    ...
    ...
    #'storages',
]


# 파일의 끝에 아래 내용을 추가합니다.
STATICFILES_STORAGE = '프로젝트디렉토리명.storage.S3StaticStorage'
DEFAULT_FILE_STORAGE = '프로젝트디렉토리명.storage.S3MediaStorage'

# AWS_ACCESS_KEY_ID = 'IAM 사용자 생성후 받게된 ACCESS KEY ID'
# AWS_SECRET_ACCESS_KEY = 'IAM 사용자 생성후 받게된 SECRET KEY ID'
# AWS_S3_REGION_NAME = 'ap-northeast-2' # 한국 아닌 지역은 다른 명칭으로 바꿔주세요.
# AWS_STORAGE_BUCKET_NAME = '버킷 이름'

# AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com'
# AWS_DEFAULT_ACL = 'public-read'
]
```

- STATICFILES_STORAGE: 정적 파일에 대한 저장소 클래스를 지정해요. STATICFILES_STORAGE 항목의 디폴트 값은 StaticFilesStorage클래스이며 이 클래스는 로컬에 있는
정적파일에 대한 저장소 역할을 해요. 반면 새로 지정한 S3StaticStorage클래스는 원격에 있는 S3 버킷을 저장소로 사용해요.

- DEFAULT_FILE_STORAGE: 미디어 파일에 대한 저장소 클래스를 지정해요. DEFAULT_FILE_STORAGE 항목의 디폴트 값은 FileSystemStorage클래스이며 이 클래스는 로컬에 있는 정적파일에 대한 저장소 역할을 해요. 반면 새로 지정한 S3MediaStorage클래스는 원격에 있는 S3 버킷을 저장소로 사용해요.

- AWS_DEFAULT_ACL = 'public-read'는 버킷에 대한 액세스 권한을 지정하는 것인데요. public-read는 버킷과 객체(정적파일, 미디어파일)에 대해 소유자느 모든 권한을 가지며 그외 사용자는 읽기만 가능한 권한입니다.

### 프로젝트디렉토리/storage.py
여기서는 정적 파일 및 미디어 파일 저장소 클래스를 정의해요.

아래 두 클래스 모두 S3Boto3Storage를 상속 받아 정의해요. 즉 장고에서 필요한 저장소 엔진 기능은 S3Boto3Storage 클래스에 이미 정의되어 있어요.
location 항목에는 S3 버킷 하위의 폴더명을 정의해요.
```
from storages.backends.s3boto3 import S3Boto3Storage

# 정적 파일용
class S3StaticsStorage(S3Boto3Storage):
  location = 'static'

# 미디어 파일용
class S3MediaStorage(S3BotoStorage):
  location = 'media'

```

### 프로젝트디렉토리/urls.py

`urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)` 부분은 미디어 파일을 로컬 저장소에 저장하는 경우 사용해요. 
이제는 S3에 서비스 하므로 삭제하거나 주석 처리할게요. 
```
from django.conf import settings
from django.conf.urls.static import static

...
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
```


### collectstatic 명령어
정적 파일을 한곳에 모아주는 명령어를 사용할게요.
요 명령으로 정적 파일들을 S3버킷에 업로드해요.
```
python manage.py collectstatic

```
버킷 아래 static, media 디렉토리와 그 아래 파일들이 있으면 정상이에요.

### Creating RDS MySQL Instance
인스턴스는 가상머신, 즉 가상으로 만든 서버 H/W 박사를 의미해요. 
- 대시브드에서 검색란에 RDS검색후 진입
- 대시보드 생성 버튼 클릭
- 버전 정보에 MySQL 8.x.x 버전 선택
- 템플릿 항목에서 프리티어 선택(월 750시간 무료)
- 설정 부분 입력(인스턴스 식별자, 마스터 사용자 이름, 마스터 암호)
- 추가 연결구성(퍼블릭 액세스 가능: 예), 외부에서도 연결 할 수 있도록 설정함. 또한 포트는 3306으로 설정.
- 데이터베이스 옵션(초기 데이터베이스 이름, 자동 백업 활성화 체크 해제), 백업 활성화 할 경우(월 20GB까지 무료이지만 이후 돈나감)
- 생성 버튼 클릭(시간이 소요됨)
- 데이터 베이스 상세화면, 엔드포인트 항목!(settings.py에 사용함)
---

### Installing mysqlclient driver to connect with Django
이제 AWS MySQL <--> Django를 연동해 볼게요.
그러기 위해선 드라이버 설치가 필요해요.

가상 환경을 실행한 이후 아래 명령어를 입력할게요.
```
pip install mysqlclient
```

> 참고! mysqlclient 설치 실패시
- 원인: Visual C++ 빌드 과정에서 에러 발생. 
- 해결책: *.whl 패키지를 아래 사이트에서 다운하고 설치함.
  - https:www.lfd.uci.edu/~gohlke/pythonlibs/#mysql-python 으로 접속
  - mysqlclient-1.4.4-cp38-win_amd64.whl패키지를 선택해 다운로드 한 경우, 
  - pip install mysqlclient-1.4.4-cp38-win_amd64.whl

다른 방법으로는 mysqlclient 대신 pymysql 패키지를 이용하는 것이에요. 순수 파이썬 패키지이므로 빌드 에러가 발생하지 않아요.

---

### Settings' Django Project
프로젝트 설정 디렉토리안의 settings.py 파일로 가서 DATABASE 변수를 변동 할게요.
```

DATABSE = {
  'default':{
    'ENGINE':'django.db.backends.mysql',
    'NAME': '데이터베이스 이름'
    'USER': '인스턴스 생성시 입력한 마스터 사용자', # 
    'PASSWORD': '인스턴스 생서시 입력한 비번',
    'HOST': '엔드포인트' # 
    'PORT': 3306, # 변동하지 않았다면 기본 3306입니다.
    'OPTIONS':
      'init_command': 'SET sql_mode='STRICT_TRANS_TABLES'",
  }
}
```
STRICT_TRANS_TABLES 항목은 레코드 생성, 변경 시 컬럼 타입이나 데이터 길이 등을 정확하게 체크하여 데이터 일부가 잘리는 것을 방지하는 기능을 해요.(잘못 입력시 오료률 발생시킴)

#### DB에 적용하기 
아래 명령어로 디비에 환경 설정 사항등을 반영해줄게요. 기존 DB인 sqlite3의 테이블들은 초기화 되므로, SQLite3 DB에 있던 예전 데이터는 삭제되요.
```
python manage.py migrate
python manage.py runserver # 서버 구동 후 정상적으로 확인!
```
