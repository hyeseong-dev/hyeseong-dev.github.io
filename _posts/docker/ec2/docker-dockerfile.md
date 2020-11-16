# Docker 설치 및 Dockerfile로 웹 서버 구동

### 현재 메모리 사용공간 확인 명령어

> df -h

## 도커 설치 명령어 

> sudo apt update

### 각종 유틸 설치 

> sudo apt install ca-certificates

{% tabs %}
{% tab title="ca-certificates" %}
```text
루트 인증서(root certificate)는 루트 인증 기관(CA)에서 관리하는
공개 키 인증서나 자체 서명 인증서이다.[1] 루트 인증서는 
공개 키 기반계획의 일부이다. 가장 상업적으로 공통되는 
ITU-t X.509 표준형, 일반적으로 루트인증기관(CA)에서 나온 
디지털 서명을 포함
```
{% endtab %}
{% endtabs %}

> sudo apt install curl

**curl의 경우 특정 웹사이트에서 데이터를 다운로드 받을때 사용함**

> sudo apt install software-properties-common

  


> curl -fsSl [https://download.docker.com/linux/ubuntu/gpg](https://download.docker.com/linux/ubuntu/gpg) \| sudo apt-key add -

도커 설치를 위해 gpg 내용을 다운받아요. 위 명령어 add 뒤에 - \(대시\)가 있어요.



> sudo add-apt-repository "deb \[arch=amd64\] [https://download.docker.com/linux/ubuntu](https://download.docker.com/linux/ubuntu) focal stable"

반드시 위 명령어의 focal이란 부분은 우분투 버전에 따라 바껴요.   
focal의 경우 ubuntu20.04에요.  
인터넷에 예를들어 ubuntu 20.04 / ubuntu 18.04/ ubuntu 16.04 docker APT sources 라는 유사 검색어로 입력하셔서 해당 버전에 맞는 이름을 입력하세요. 



> sudo apt update   
> apt-cache policy docker-ce  
> sudo apt install docker-ce

마지막 명령어로 인해 도커\(엔진\)가 설치 되었어요. 

> systemctl status docker

도커 설치 상태를 확인 할 수 있어요. 



### Hello World 이미지 다운 컨테이너 실행 및 삭

> docker pull hello-world  
> docker images

pull 명령어로 hello-world 이미지를 다운로드하게되요.   
이후 docker images 명령어로 hello-world 이미지가 다운로드 된걸 확인 할 수 있어요.

> docker run hello-world  
> docker ps -a

run 명령어는 hello-world 컨테이너를 생성시켜요.\(만약 docker pull hello-world를 생략하고 바로 run 명령어를 하게되면 기존에 hello-world가 없다면 자동으로 pull 명령어를 내포해서 실행함.\)

docker ps\(process\) -a\(all\) 명령어는 컨테이너들 목록을 쫙 보여준다.

### 도커파일 작성으로 서버 이미지 만들기

> cd /home/ubuntu

이 경로로 이동해서 도커 파일을 만들어 볼게요. 

> mkdir example   
> cd example   
> sudo vi Dockerfile

example이라는 디렉토리를 만들고 Dockerfile\(D는 항상 대문자\)이라 파일을 작성할게요.

```text
FROM ubuntu:18.04
MAINTAINER Hyeseong lee <hyeseong43@gmail.com>

RUN apt-get update
RUN apt-get install -y apache2 

EXPOSE 80 

CMD ["apachectl", "-D", "FOREGROUND" ]


```

```text
# 해설 
-y 옵션은 설치 할지 말지 설치 중에 묻게 되는 경우 미리 yes를 작성해주는 역할임. 
그리고 아파치 웹서버는 기본적으로 80포트를 이용하는 특징이 있어요. 
다만 우리가 컨테이너를 만들어 실행하기 위해서는 EXPOSE명령어를 통 실제로 몇번 포트를 연결해서 이용할 것인지
설정해 줄수 있어요. 

그리고 CMD는 특정 컨테이너는 실행되자마자 종료되기에 아파치가 항상 실행되도록 하기 위해
daemon 상태로 만들어 준다는 말이에요.
```

#### Dockerfile Build

> docker build -t example .

-t 옵션은 태그인데요. example이라는 태그 이름을 달았어요. 그리고 마지막에 잘 안보이겠지만 띄우고 .\(점\)을 찍어주세요. 현재 디렉토리에서 빌드하겠다는 말이에요. 

> docker images

위 명령어를 입력하면 우리가 만든 아파치2 이미지 example이 만들어 진걸 확인 할수 있어요.

#### 이미지 구을 위한 container 실행 

> docker run -p 80:80 example

exmaple 이미지 같은 경우는 80번 포트로 구동된다고 앞에서 말했어요. 그래서 80번 포트와 우리의 EC2 서버를 연결해줘야해요. 왼쪽 80번은 우리의 호스트 \(우리 서버\)의 포트번: 오른쪽 80번은 테이너의 포트번호에요. 

### EC2 80번 포트를 열어주세요. 

> 보안그룹 - 인바운드 규칙 - 편집 - 규칙추가 - 
>
> 사용자 지정 : http, 프로토콜 : TCP,  소스: 0.0.0.0/0, ::/0

> 본인 서버IP:80

![](../../.gitbook/assets/image%20%2883%29.png)

 아래와 같이 성공적으로 접속되요.



  




\*\*\*\*

### \*\*\*\*

\*\*\*\*



