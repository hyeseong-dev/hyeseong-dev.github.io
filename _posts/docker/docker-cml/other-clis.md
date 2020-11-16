# other CLIs

 실제 환경에서 ㅔ운용할 떄 이미 가동 중인 컨테이너의 상태 확인하거나 임의의 프로세스를 실행시킬 떄 하는 조작에 대해 알아볼게요. 

## docker container attach - 가동 컨테이너 연결

 가동 중인 컨테이너에 연결할 떄는 docker container attach 명령을 사용합니다.   
**예를 들어 /bin/bash가 실행되고 있는 "컨테이너A" 연결하려면 아래와 같이 실행**합니다. 연결한 **컨테이너를 종료하려면 exit**를 입력하, 컨테이너를 시작한 채로 컨테이너 안에서 움직이는 **프로세스\(이 경우 /bin/bash\)만 종료하려면 Ctrl + P누르고 다시 Q를 눌러줍니다.**

 

![](../../.gitbook/assets/image%20%28954%29.png)

## 가동 컨테이너에서 프로세스 실행

#### 문법 

> **docker container exec    옵션     컨테이너식별자    실행명령어    인수**

#### **주요 옵션** 

* --detach, -d       : 명령을 백그라운드에서 실행
* --interactive, -i  : 컨테이너의 표준 입력을 연다
* --tty, -t                :  false  tty\(단말 디바이스\)를 사용한다
* --user, -u            : 사용자명을 지정한다

####  컨테이너에서 bash 실행

![](../../.gitbook/assets/image%20%28953%29.png)

####  컨테이너에서 echo 명령어 실

 또한 명령을 직 실행 할 수 도 있습니다. echo 명령어를 아래와 같이 실행해 볼게요. 

![](../../.gitbook/assets/image%20%28942%29.png)

## **가동 컨테이너 프로세스 확인**

####  문법

> **docker container top 컨테이너식별자**

![](../../.gitbook/assets/image%20%28949%29.png)

##  가동 컨테이너 포트 전송 확인

 프로세스가 전송되고 있는 포트를 확인 할 떄는 docker container port명령을 사용하는데요.   


####  syntax

> **docker container port 컨테이너식별자**

```text
$ docker container port webserver
80/tcp -> 0.0.0.0:80
```

### 잠깐! 포트에 대해서

TCP/IP를 이용한 데이터 통신에서, 특정 프로토콜에서 사용하는 것으로 예약되어 있는 포트 번호를 잘 알려진 포트\(well-known port\)라고 합니다. 0부터 65535까지의 포트 번호 중 잘 알려진 포트는 1부터 1023까지를 사용하므로, 보통의 애플리케이션에서는 1024 이후의 포트 번호를 사용하는 것이 관례입니다. 

![](../../.gitbook/assets/image%20%28952%29.png)

![](../../.gitbook/assets/image%20%28951%29.png)

\*\*\*\*

##  컨테이너 이름 변경

####  문법

> docker rename 기존컨테이너이름  변경하고자하는이름  
> or  
> docker container rename 기존컨테이너이름  변경하고자하는이름

![](../../.gitbook/assets/image%20%28948%29.png)

##  컨테이너 안의 파일을 복사 

####  문법

> docker container cp  &lt;컨테이너식별자&gt;:&lt;컨테이너안의파일경로&gt; &lt;호스트 디렉토리 경로&gt;  
> or  
> docker container cp &lt;호스트의 파일&gt;  &lt;컨테이너식별자&gt;:&lt;컨테이너안의 파일 경로&gt;

 예를 들어 test라는 이름의 컨테이너 안에 있는 /etc/nginx/nginx.conf 파일을 호스트의 /tmp/etc에 복사할 때는 아래 명령어를 실행합니다. 혹은 아무 파일이나 생성하여 진행해도 됩니다.

 컨테이너 안에서 &gt;&gt;&gt;&gt; 호스

![](../../.gitbook/assets/image%20%28941%29.png)

호스트 &gt;&gt;&gt;&gt;&gt;&gt;&gt; 컨테이너 안으로 

![](../../.gitbook/assets/image%20%28950%29.png)

##  컨테이너 조작의 차분 확인 

 컨테이너 안에서 어떤 조작을 하여 컨테이너가 이미지로부터 생성되었을 떄와 달라진점을 확인 할 수 있어요. 

####  문법

> docker container diff  컨테이너 식별자

####  변경의 구분 

* A   : 파일추가\(add, append\)
* D   : 파일 삭제\(Delete\)
* C   : 파일 수정\(Change\)

####  Example

> #### 컨테이너 안에서 신규 사용자 작성

![](../../.gitbook/assets/image%20%28945%29.png)









