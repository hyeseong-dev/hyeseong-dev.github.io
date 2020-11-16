---
description: 볼륨마운트로 주피터 노트북 구축
---

# Jupyter notebook with volume mounting

볼륨 마운트로 주피터 노트북 구축 및 실행 

##  주피터 노트북 dockerhub에서 확인하기 

![jupyter notebook &#xC6F9;&#xD398;&#xC774;&#xC9C0; ](../../.gitbook/assets/image%20%283%29.png)

##  볼륨 마운트 옵션 이용 로컬 파일 공유하기 

```text
docker run -v <호스트 경로>:<컨테이너 내 경로 >:<권한> # /tmp:home/user:ro (reand only
```

* 권한의 종류  - ro: read only 읽기 전용 - rw: read & write 일기 및 쓰기

#### nginx로 불륨 마운트 하기 

```text
> docker run -d -p 80:80 --rm --name nx -v /var/www:/usr/share/nginx/html:ro nginx
> curl 127.0.0.1
> echo 1234 > /var/www/index.html
> curl 127.0.0.1

```

#### 터미널 환경에서 확인 시 

```text
test1234 
```



#### 웹 브라우저에서 확인

![127.0.0.1&#xC5D0; &#xBD99;&#xC740;&#xAC78; &#xD655;&#xC778; &#xD560;&#xC218; &#xC788;&#xC74C;](../../.gitbook/assets/image%20%2830%29.png)

## Juypyter Lab 환경 구축

```text
mkdir ~/juypyternotebook
cd ~/jupyternotebook 
docker run --rm -p 8080:8888 -e JUPYTER_ENABLE_LAB=yes -v "$PWD":/home/jovyan/work:rw jupyter/datascience-notebook:9b06df75e445

# 출처: https://jupyter-docker-stacks.readthedocs.io/en/latest/
```

#### 주피터 랩 서버로 접속해서 새 노트북 생성 

"$PWD"는 호스트 경로에 해당해요.  이후 /home/jovyan/work는 컨테이너 경로에 해당하고요. 마지막으로 rw\(read and write\)는 권한을 부여한거에요./home/jovyan/work 사이사이마다 : \(콜론\)이 있어요. 

```text
<호스트 경로>:<컨테이너 내 경로 >:<권한>
```

#### 참고로, 만약 rw같은 권한을 주지 않으면 403 Error가 발생해요. 

> 403 Forbidden은 서버가 허용하지 않는 웹 페이지나 미디어를 사용자가 요청할 때 웹 서버가 반환 하는 HTTP 상태 코드이다. 클라이언트가 서버에 도달할 수 있어도 서버가 페이지 접근 허용을 거부했다는 것을 뜻한다.

출처: [https://m.blog.naver.com/PostView.nhn?blogId=rhkrehduq&logNo=221397786533&proxyReferer=https:%2F%2Fwww.google.com%2F](https://m.blog.naver.com/PostView.nhn?blogId=rhkrehduq&logNo=221397786533&proxyReferer=https:%2F%2Fwww.google.com%2F)



### 웹브라우저 접속 

위의의 마지막 run명령어로 jupyter lab이 정상 설치되었다면 파이어폭스  웹브라우저에가서 아래와 같은 주소를 주소창에 입력해주세요. 

> http://localhost:8080

 그럼 아래와 같은 token 번호요청 페이지가 나타나요. 

![jupyter &#xD1A0;&#xD070; &#xC785;&#xB825;&#xCC3D;](../../.gitbook/assets/image%20%28148%29.png)

#### 토큰 확인 방법 

![token &#xBC88;&#xD638;&#xB97C; &#xD655;&#xC778; &#xD558;&#xC138;&#xC694;. ](../../.gitbook/assets/image%20%2875%29.png)

####  주피터 접속 화면 

![&#xC8FC;&#xD53C;&#xD130; &#xC811;&#xC18D; &#xD654;&#xBA74; ](../../.gitbook/assets/image%20%2818%29.png)

파이썬3를 클릭해서 실행해볼게요. 

![](../../.gitbook/assets/image%20%2893%29.png)

403 접근제한 오류가 나타나요. 

#### 1.  rw 옵션 

2. docker가 사용자 권한으로 돌아가게되어 root 권한으로 만든 디렉토리에는 무엇인가를 쓸수가 없어요. 

> chmod 777 jupyternotebook/

위 명령어를 입력해주세요. 

![chmod 777 &#xB514;&#xB809;&#xD1A0;&#xB9AC;&#xBA85;](../../.gitbook/assets/image%20%2846%29.png)

  
chomd 777에 관한 부분은 리눅스에의 권한 설정에 대한 부분을 학습해야 해요.   
어쨋든 아래에 정상적으로 주피터 노트북을 쓸수 있게되었어요.   
  

![&#xAD6C;&#xCD95; &#xC644;&#xB8CC;](../../.gitbook/assets/image%20%2821%29.png)

![](../../.gitbook/assets/image%20%28165%29.png)

 참고로 pandas, numpy, seaborn 모듈은 이미 설치되어있지만 keras, tensorflow는 설치되어있지 않네요. 





