# Docker Useful CML

###  도커의 다양한 명령어 

####  포트포워딩으로 톰캣 실행 

```text
docker run -d name tc tc -p 80:8080 tomcat 
firefox 127.0.0.1:80
```

####  container shell 실행 

```text
docker exec -it tc /bin/bash
```

![](../../.gitbook/assets/image%20%28155%29.png)

-it 옵션은 **input terminal**의 약자에요.    
**노란부분은 터미널 id에요.**

container가 없어서 새로 생성 시키는 경우 run명령어로 해주면 되요.   
그게 아니면 start 명령어로 실행해주세요.  

####  container log 확인 

```text
sudo docker logs tc # stdout(standout), stderr(standout error) 
```

####  txt파일 생성및 내용 입력

```text
echo 하나,둘,셋 > test.txt
```

![echo &#xBA85;&#xB839;&#xBB38;&#xC73C;&#xB85C; &#xD30C;&#xC77C;&#xC0DD;&#xC131; &#xBC0F; &#xC791;&#xC131;](../../.gitbook/assets/image%20%28103%29.png)

#### 

#### 파일 이동 CP명령어 

logs의 기록들은 파일의 기록이 아니에요. 프로그램이 실행될때 그 출력을 logs에 담게되요. 

#### host &lt;-&gt; container 파일 복사 

```text
sudo docker cp <path> <to container>:<path>
sudo docker cp <from container>:<path> <path>
sudo docker cp <from container>:<path> <to container>:<path>
```

![cp &#xBA85;&#xB839;&#xC774;&#xD6C4; docker&#xC758; &#xD574;&#xB2F9; &#xCEE8;&#xD14C;&#xC774;&#xB108;&#xC5D0;&#xC11C; &#xC2E4;&#xD589;](../../.gitbook/assets/image%20%28118%29.png)

####  파일 이름 바꿔서 복사-&gt;생성

![](../../.gitbook/assets/image%20%2831%29.png)

> docker cp **A:/B ./C \# 방법1은 상대경로  
> or docker cp A:/B A:/C 방법2는 절대경로 방법**

> **A: 디렉토리이름  
> B: 기존 파일명  
> C: 새로 만들려는 파일명\(기존파일 내용 복사해서 만들거임\)**

\*\*\*\*

#### **프로세스 확인** 

![&#xBC29;&#xBC95;1, &#xBC29;&#xBC95;2](../../.gitbook/assets/image%20%2826%29.png)

방법1은 ps 명령문으로 실행  
방법2는 옵션 -a -q 를 추가해줘요. 

\*\*\*\*

실행중인 프로세스\(컨테이너\) 전체 stop

![&#xC774;&#xC911; &#xBA85;&#xB839;&#xBB38; &#xC791;&#xC131;](../../.gitbook/assets/image%20%2884%29.png)

 docker stop이라는 문장안에 $\(docker ps -a -q\) 명령문을 추가작성함.

> docker stop $\(docker ps -a -q\)

> 옵션 설명: **-q, --quiet Only display numeric IDs**

\*\*\*\*

#### 컨테이너 모두 지우기 

![](../../.gitbook/assets/image%20%2854%29.png)

docker **rm**이라는 문장안에 $\(docker ps -a -q\) 명령문을 추가작성함.

> docker rm $\(docker ps -a -q\)



#### 임시로 컨테이너를 만들고 싶은 경우 

**컨테이너를 잠깐 생성하고 이후 삭제를 한방에 하고 싶은 경우!**

![](../../.gitbook/assets/image%20%282%29.png)

> **docker run -d --name 컨테이너명 -p 포트번호:8080 --rm 이미지명  
> docker stop 컨테이너명   
> docker ps -a**

이미지명 앞에 --rm\(remove\) 옵션을 추가해주면 컨테이너를 생성하고 이후 stop명령문을 사용해서 정지하면 이미 삭제된걸 볼수 있다. 

