---
description: 한큐에 실습하고 요약
---

# Excercise For Docker

## 목차

#### 한 큐에 모든 image와 container 정지 및 삭제

#### Jenkins 검색

#### Jenkins 설치

#### Jenkins port 접속후 웹 서비스 열기

#### Jenkins 초기 password 찾아서 login까지

### 한 큐에 모든 image와 container 정지 및 삭제

```text
>>> docker stop $(docker ps -a -q)  
>>> docker rm $(docker ps -a -q)    
>>> docker rmi $(docker images -q)
```

### Jenkins 검색

```text
>>> docker search jenkins
```

### Jeinkins 설치

```text
>>> docker pull jenkins 
>>> sudo docker inspect jenkins
>>> docker run -d -p 8080:8080 --name jk jenkins
```

**8080포트를 지정은 jenkins pull 명령어 사용후 -&gt; inspect명령어로 살펴보면 안에 port 정보가 나와있어요. 이를 바탕으로 넣어주세요.**

![inspect &#xBA85;&#xB839;&#xC5B4;&#xB85C; &#xAC01; &#xC774;&#xBBF8;&#xC9C0; &#xD3EC;&#xD2B8; &#xD655;&#xC778; ](../../.gitbook/assets/image%20%28190%29.png)

\*\*\*\*

**jenkins는 버전 관리를 위해 실무에 많이 사용하는 appication이에요.**

### Jenkins port 접속후 웹 서비스 열기

```text
>>> firefox 127.0.0.1:8080
```

만약 브라우저에 캐시가 남아 있는 경우 아래 단축키로 캐시를 지워주세요.  
**ctrl + shift + del**

### Jenkins 초기 password 찾아서 login까지

#### 방법1: 경로를 통해서 확인하기

 웹브라우저 열고 127.0.0.1:8080 실행해보세요.   
아래와 같은 화면이 나와요. 노란색 부분이 초기 비밀번호가 있는 경로인데요.  
 

![&#xCD08;&#xAE30; &#xBE44;&#xBC00;&#xBC88;&#xD638;&#xAC00; &#xC788;&#xB294; path&#xB97C; &#xCD9C;&#xB825;&#xD574;&#xC90C;](../../.gitbook/assets/image%20%28176%29.png)

즉, initPasswod 디렉토리에서 확인 가능해요. initPasswod 디렉토리의 경로를 알아낸 다음cat 명령어로 확인 할 수 있어요.

```text
>>> docker exec -it jk cat /var/jenkins_home/secrets/initialAdminPassword
de62fcac227f4d679247178d71f19006
```

#### 

#### 방법2: docker의 logs 명령어 사용

```text
>>> docker logs jk
```

명령문에 대한 출력결과가 나오는데 그 일부분이 아래와 같이 나와요. password라는 단어를 찾아서 웹 브라우저에 넣으면 되요.

```text
Jenkins initial setup is required. 
An admin user has been created and a password generated. 
Please use the following password to proceed to installation:

de62fcac227f4d679247178d71f19006

This may also be found at
: /var/jenkins_home/secrets/initialAdminPassword
```



