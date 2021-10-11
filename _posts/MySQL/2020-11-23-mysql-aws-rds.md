---
layout: post
title: "[MySQL] AWS RDS를 이용하여 MySQL과 Django 연동"
date: 2020-11-23 13:34
category: MySQL
tags: [RDS,RDB,AWS, Django]

---
![MySQL, AWS, Django](https://www.pulumi.com/blog/deploying-a-django-application-to-aws/meta.png)

# AWS RDS를 이용하여 MySQL과 Django 연동

---
## Creating RDS MySQL Instance
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

### DB에 적용하기 
아래 명령어로 디비에 환경 설정 사항등을 반영해줄게요. 기존 DB인 sqlite3의 테이블들은 초기화 되므로, SQLite3 DB에 있던 예전 데이터는 삭제되요.
```
python manage.py migrate
python manage.py runserver # 서버 구동 후 정상적으로 확인!
```
