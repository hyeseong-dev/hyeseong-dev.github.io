# Github에 Docker Project Uplaod

###  이전 배운 것  

지난 글들까지 종합해보면 도커파일을 생성, PHP서버를 통해 AWS -RDS 서버에 접속하여 연동해보는 실습을 해봤어요. 

##  Github에 도커소스 업로드 

 이번에는 도커 관련 소스들을 --&gt; Github에 업로드 해볼게요.  

###  Github   

 - 우선 Github에 Login해주세요.

  
 - Repository 생성을 할거에요. 

1. repository 이름에는 가볍게 Docker-Practice라고 정했어요. 

2. Public, Private가 있는데 Private로 설정해 줬어요.   
 본인이 github에 올리는 정보가\(개인정보, 중요한 정보, 계정정보\)등이 있기에 Private로 설정한거에요. 

###  AWS - EC2 

###  git 프로젝트 생성 

* Terminal 환경으로 가주세요. git 을 입력하고 실행해보세요.  그럼 git 명령어 사용법에 대한 내용들이 출력되는걸 볼 수 있어요. 

```text
git
```

> ubuntu 18.04 LTS 버전에는 git프로그램이 설치되어 있어요.

* 본격적인 git 작업을 할텐데요. 

{% tabs %}
{% tab title="EC2" %}
```text
cd /home/ubuntu/
git clone 본인저장소주
cd Docker-Practice
```
{% endtab %}
{% endtabs %}

```text
.
├── Docker-Practice
├── example
│   ├── Dockerfile
│   └── html
│       └── index.php
└── ssl
    ├── cert.key
    └── cert.pem
```

ubuntu 디렉토리로 가서  git clone 깃허브에서 만 주소를 붙여넣기해서 실행하면 위와 같이 'Docker-Practice' 디렉토리가 생성된걸 확인 할 수 있어요.  cd 명령어로 Docker-Practice 폴더로 진입해주세요.   
빈 도커파일을 만들건데요. 

```text
sudo vi Dockerfile # vim 에디터로 파일 생성
sudo touch Dockerfile # vim 에디터로 진입하지 안아도됨 
```

 위 두가지 방법중 편한 방법으로 Dockerfile을 생성해 주세요.   
그리고 주피터를 이용해서 해당 Dockerfile을 열어서 작성해볼게요. 

내용은 복붙 할건데요. /home/ubuntu/example/Dockerfile에 갈거에요. 주피터환경에서 GUI 환경으로 바로 클릭클릭해서 가면 빠르게 갈수 있을거에요. 

```text
FROM ubuntu:18.04
MAINTAINER Hyeseong lee <hyeseong43@gmail.com>

ENV DEBIAN_FRONTEND=nointeractive

RUN apt-get update
RUN apt-get install -y apache2
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:ondrej/php
RUN apt-get update 
RUN apt-get install -y php5.6

RUN apt-get install -y php5.6-mysql

EXPOSE 80

CMD ["apachectl", "-D", "FOREGROUND" ]

```

다시 /home/ubuntu/Docker-Practice/Dockerfile에 가시고 복사해온 내용을 붙여넣어주세요. 

**중간 요약 : 우분투 18.04에 특정한 프로그램\(아파치, PHP5.6, php5.6-mysql\)을 설치한 이미지라를 빌드하기 위함이에요.** 

 이제 우리는 git 프로젝트를 만든거에요. 

### php 소스코드 작성 

index.php 파일을 Docker-Practice 디렉토리에 생성할게요. 

내용은 바로 이전 시간\(AWS RDS를 이용 -DB 구축\)에 작성한 내용을 넣을 거에요.   
즉,  /[home](http://3.22.225.2:8888/tree/home)/[ubuntu](http://3.22.225.2:8888/tree/home/ubuntu)/[example](http://3.22.225.2:8888/tree/home/ubuntu/example)/[html](http://3.22.225.2:8888/tree/home/ubuntu/example/html)/index.php 파일 내용을 /[home](http://3.22.225.2:8888/tree/home)/[ubuntu](http://3.22.225.2:8888/tree/home/ubuntu)/[Docker-Practice](http://3.22.225.2:8888/tree/home/ubuntu/Docker-Practice)/index.php 파일에다가 복붙한다는 말이에요. 

일반적으로 Dockerfile과 index.php 내용을 같이 둬서 build하게 되요요.

###  깃허브에 업로드 

이 파일 2개를 깃허브에 upload하도록 할게요. \(깃 문법이에요\)

```text
git add . 
git commit -m "Initial Project Components"
git push 
Username for 'https://github.com': 깃허브유저명
Password for 'https://osori-magu@github.com': 비밀번
```

이제 모두 완료 했습니다. 본인 깃허브 Repository에 가면 소스코드 파일2개가 업로드 된걸 확인 할 수 있어요.   
git push 딱 두 단어만 넣고 push 된다는게 신기하네요. git push origin master까지 full로 적는줄 알았거든요. 더군다나 private 저장소라서 username과 password까지 입력하고요!.   


## **결론 :** 

#### 1. Dockerfile과 index.php 파일 생성과 작성

#### 2. 이전 소스 코드 내용을 복붙 

#### 3. 깃헙에 업로드



