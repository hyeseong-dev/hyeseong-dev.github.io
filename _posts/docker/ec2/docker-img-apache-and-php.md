# Docker img로 Apache & PHP 개발환경 구축

## PHP 개발환경 구축



### 컨테이너 목록 확인 

#### docker ps -a 

```text
docker ps -a # 도커 컨테이너 리스트를 모두 출력
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                NAMES
e8bfedabc155        example             "apachectl -D FOREGR…"   23 hours ago        Up 23 hourshours         0.0.0.0:80->80/tcp   serene_bose
```

이전 시간에 만들었던 아파치 컨테이너 하나가 있습니다. 

###  컨테이너 전부 삭제 

#### **docker rm -f $\(docker ps -a -q\)**

-f \(force\) 강제로 모두 지우겠다는 옵션이며 뒤의 $\(docker ps -a -q\)는 도커 컨테이너 전부를 의미해요.   

```text
docker rm -f $(docker ps -a -q) # $(명령문)은 컨테이너 전부를 삭제함                                       
e8bfedabc155
```

삭제된 컨테이너의 id가 출력되네요.   
시작에 앞서서  불필요한 컨테이너들을 말끔히 정리했습니다. 



###  Vim 에디터로 파일 수정 

#### Dockerfile 수정 

이전 시간 "Docker 설치 및 Dockerfile로 웹 서버 구동'에 만들었던 Docker파일을 수정 할 게요. 

```text
root@ip-172-31-35-20:/# cd /home/ubuntu/example
root@ip-172-31-35-20:~/example# ls
Dockerfile
root@ip-172-31-35-20:~/example# vi Dockerfile
```

Dockerfile 내부를 보면 Apache2만 설치한 모습이 보이조?  
이제는 **아파치 설치 이후 PHP까지 설치할수 있게 추가적으로 RUN명령어를 입력**해볼게요. 

{% code title="수정 전 Dockerfile" %}
```text
FROM ubuntu:18.04
MAINTAINER Hyeseong lee <hyeseong43@gmail.com>

RUN apt-get update
RUN apt-get install -y apache2

EXPOSE 80

CMD ["apachectl", "-D", "FOREGROUND" ]
```
{% endcode %}



{% code title="수정한 Dockerfile" %}
```text
FROM ubuntu:18.04
MAINTAINER Hyeseong lee <hyeseong43@gmail.com>

RUN apt-get update
RUN apt-get install -y apache2
RUN apt-get -y software-properties-common
RUN add-apt-repository ppa:ondrej/php
EXPOSE 80

CMD ["apachectl", "-D", "FOREGROUND" ]
```
{% endcode %}

 이전 버전인 PHP5.6 설치를 위해 먼저 software-properties-common이라는 명령어 6번째 줄의에  입력할게요. 

```text
RUN apt-get -y software-properties-common
```

> software-properties-common은 제 블로그글에서 검색해서 관련 내용을 확인해보세요.



7번째 줄에는 PHP5.6을 설치할수 있도록하는 추가 명령어를 입력할게요. 

```text
RUN add-apt-repository ppa:ondrej/php
```



Vim 에디터를 나와주세요.\( ESC + :wq! \)

## Volume 공유를 통한 PHP 소스코드 동작 

###  Dockerfile build하기 

 그리고 아래와 같이 docker build명령어를 입력해볼게요.

```text
docker build -t example .
```

 1~2분 소요가되고 마지막에 아래와 같은 옵션이 나오는걸 확인할 수 있어요.  하지만 아무것도 입력할 수 없는 상태에요.   
지금 docker image가 실행되고 있는 상태라서 그래요. 

  
도커 파일을 이용해서 하나의 서버 이미지를 만들때 추가적인 작업을 물어보는 경우가 아래와 같아요. 

일단, Ctrl + Z를 눌러 나가 볼게요.   


```text
------------------

Please select the geographic area in which you live. Subsequent configuration
questions will narrow this down by presenting a list of cities, representing
the time zones in which they are located.

  1. Africa      4. Australia  7. Atlantic  10. Pacific  13. Etc
  2. America     5. Arctic     8. Europe    11. SystemV
  3. Antarctica  6. Asia       9. Indian    12. US
Geographic area:
```

 TZ\(Time Zone\)을 물어보는 상황이었습니다. 사실   
이런 질문을 던지는걸 피하기 위해서 **사용자 interaction이 나타나는걸 방지하기 위해서 환경변수를 설정**해주면 해결되요. 

다시 vi Dockerfile 명령어를 입력하고 실행하세요.   
그리고 4번째 줄에 ENV DEBINAN\_FRONTEND=nointeractive  
입력하세요. 

```text
FROM ubuntu:18.04
MAINTAINER Hyeseong lee <hyeseong43@gmail.com>

ENV DEBIAN_FRONTEND=nointeractive

RUN apt-get update
RUN apt-get install -y apache2
RUN apt-get -y software-properties-common
RUN add-apt-repository ppa:ondrej/php
EXPOSE 80

CMD ["apachectl", "-D", "FOREGROUND" ]
```

 그리고 다시 빌드를 수행하기 위해 아래 명령어를 실해 볼게요.   
**Docker build -t example .  
그럼 이번엔 build가 성공적으로 된걸 확인 할수 있어요.** 

**혹시나 중간에 오류가 생겼다면 Dockerfile에 오타가 없는지 확인해보세요.\(저 같은 경우 ENV DEBIAN을 DEBINAN으로 써서 ;;;\)**

### 

### 빌드된 Docker 이미지 확인 

 아래 example이라는 이미지가생성된걸 잘 확인 할수 있어요.   
그리고 build에 실패했던 이미지들은 none이라는 이미지 이름과 tag를 갖고 있네요. 

```text
root@ip-172-31-35-20:~/example# docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
example             latest              59277117bebc        5 minutes ago       256MB
<none>              <none>              34951bfec79f        42 hours ago        189MB
ubuntu              18.04               c3c304cb4f22        5 weeks ago         64.2MB
hello-world         latest              bf756fb1ae65        4 months ago        13.3kB
```

####  none 이미지 삭제 

Image ID 2자리 혹은 3자리를  간단히 입력해도 delete가 되요. 

```text
root@ip-172-31-35-20:~/example# docker rmi 349
Deleted: sha256:34951bfec79fe3e083f2fd972dfa2868530bdfd19bbf16e25d913233bc2b59b2
Deleted: sha256:4db320fd12a70e8b1010505b15b403fcb1ba142c920ef5faea34f016defcd6d0
Deleted: sha256:ddc319f07cf933e3452134d7f70c131cebb0c00442299af045fc3d100de4ea8c
Deleted: sha256:ce2340187cfe8c53d589120fe73aa36d78613834e549b947dc5a7bf47c8925c7
Deleted: sha256:cc2a3e91c2069ed8ce9128f2c389eced064f962c6f33559cf614412c6e65d82b
Deleted: sha256:038fe5d5367f9e5c9f7c62902f7f70120844b6fa3296b09b046aa49980d82e68
root@ip-172-31-35-20:~/example# docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
example             latest              59277117bebc        8 minutes ago       256MB
ubuntu              18.04               c3c304cb4f22        5 weeks ago         64.2MB
hello-world         latest              bf756fb1ae65        4 months ago        13.3kB
```

만약 실행 중인 컨테이너가 있을경우 이미지 삭제가 안되요. 그럴경우 아래 명령어를 이용해주세요. 

![](../../.gitbook/assets/image%20%28209%29.png)

```text
docker ps -a 
docker rm -f 컨테이너ID 
```

![](../../.gitbook/assets/image%20%28205%29.png)

```text
docker rmi -f 이미지ID 
```

none이미지와 none 이미지로 만들어진 컨테이너를 정지 삭제 마지막으로 none이미지도 삭제해봤어요.  

###  빌드한 이미지 실행

-p 옵션으로 80번 포트를 열어줄게요.  

이후 -v 옵션으로 마운팅을 진행할건데요. : 콜론을 기준으로 좌항은 host에 해당되는데요. 

/home/ubuntu/example/html 은 호스트의 경로라는 말이에요. example까지는 현재 작업하는 경로네요!  

: 우항 /var/www/html은 컨테이너의 경로이며 php의 소스코드가 놓이는 기본적인 경로를  말해요. 

**즉 -v 옵션에서 호스트의 디렉토리에 어떤 파일A를 놓으면 그 A파일은 복사되서 컨테이너에 있는 아파치 경로에 복사된 파일이 놓이게 되는거에요.** 

```text
docker run -p 80:80 -v /home/ubuntu/example/html:/var/www/html example 
```



이제 본인 EC2 서버 IP주소:80 입력하고 실행하면 아래와 같이 실행되요. 

![](../../.gitbook/assets/image%20%28204%29.png)



터미널을 한개더 생성해 볼게요. 

New 탭버튼 클릭하고 Terminal 눌러주세요. 

![](../../.gitbook/assets/image%20%28201%29.png)

 아래 명령어로 실행해서 해당 디렉토리로 이동하세요.   
이곳 html디렉토리에서 html문서나 php 문서 작업하고 저장된 것들이 아파치 컨테이너에서 저장하게동일하게 적용된다는 말이에요. 

```text
cd /home/ubuntu/example/html 
```



일반적으로 웹서버에 올라가는 기본 파일명은 index가 된답니다.  
vim 에디터로 index.php 파일을 작성할텐데요.   
우선 &lt;?php phpinfo\(\);?&gt;  이렇게 작성, 저장까지 마무리하고 나와주세요.  

{% tabs %}
{% tab title="ubuntu" %}
```text
vi index.php
```
{% endtab %}

{% tab title="index.php" %}
```
<?php phpinfo(); ?>
```
{% endtab %}
{% endtabs %}

그리고 아까 켜놓은 php 웹브라우저를 켜보면 **컨테이너 안에 설치가된 php 버전명과 각종 환경 설정이 출력되는걸 확인 할 수 있어요.** 

![](../../.gitbook/assets/image%20%28210%29.png)



결론: 이번에는 도커파일을 작성해서 아파치 웹서버 및 PHP를 설치해 하나의 웹서버가 완성된 형태로써 나의 서버에 실행된걸 확인할수 있었음. 

![](../../.gitbook/assets/image%20%28200%29.png)

 구체적으로는 컨테이너 하나에 아파치와 PHP를 설치해서 간편하고 신속하게 도커 RUN 명령어로 이용 가능하다는 말이에요. 

예를 들어서 -p 옵션을 두고 호스트의 81번 포트를 열어서 컨테이너의 80번 포트와 연결할 수 있도록 하고 -v 옵션을 둬서 위에서 실습했던것과 동일하게 경로를 지정하면 

```text
docker run -p 81:80 -v /home/ubuntu/example/html:/var/www/html example
```

81번 포트로 웹 서버가 열린걸 확인 할 수 있어요.   
EC2에서 인바운드 규칙 편집에서 81번 포트를 방화벽으로 열어주게되면 81번 포트로도 마찬가지로 접속 할 수 있게 되는거에요. 

![](../../.gitbook/assets/image%20%28202%29.png)

![](../../.gitbook/assets/image%20%28206%29.png)

즉 다양한 웹 서버를 하나의 서버에서  실행 시킬수 있다는 말이에요.   
결국 서비스 배포와 관리가 매우 손쉽다는 말이기도 하겠지요?

---



