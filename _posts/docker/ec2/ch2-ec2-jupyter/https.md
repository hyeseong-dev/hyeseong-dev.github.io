# 주피터에서 HTTPS 적용

설치된 주피터 노트북에 \_\_HTTPS\_\_\( **H**yper**T**ext **T**ransfer **P**rotocol over **S**ecure Socket Layer\)를 적용하는 방법에 대해 알아볼게요.   
현재는 HTTP인데, 마지막에 S가 붙은 이유는  **S**ecure Socket Layer를 추가한다는 말이에요.   
---

우리가 일단 주피터에서 EC2서버를 이용해서 주피터 노트북에 접근하면 아래와같이 뜨는걸 확인 할 수 있어요.  
&gt;  접속 방법: 본인의 IP주소:8888 -&gt; 비밀번호입력   
문제는 아래 주의 요함이라는 부분이 떠요. 보안이 매우 취약하다는건데요. HTTP상태이기 때문에 나타납니다. 이를 HTTPS로 바꾸어 볼게요.   


![](../../../.gitbook/assets/image%20%2814%29.png)

#### 1단계. ssh로 접속해주세요.  

> ```text
> ssh -i "new_keypair.pem" ubuntu@ec2-18-191-177-247.us-east-2.compute.amazonaws.com
> ```

#### 2단계. 주피터 노트북을 종료해주세요.  

\_\_내 서버의 8888포트 확인하기\_\_

> netstat -nap \| grep 8888

network statistics을 어원으로 하는 netstat인데요.   
우리가 자주사용하는 유틸리티로 네트워트 게이트간의 연결, 라우팅 테이블 정보등을 표시해줘요.    
\[Netstat명령어파악\]\([https://m.blog.naver.com/PostView.nhn?blogId=ysw1130&logNo=220159168596&proxyReferer=https:%2F%2Fwww.google.com%2F](https://m.blog.naver.com/PostView.nhn?blogId=ysw1130&logNo=220159168596&proxyReferer=https:%2F%2Fwww.google.com%2F)\)  


![8888&#xD3EC;&#xD2B8; &#xD504;&#xB85C;&#xC138;&#xC2A4; &#xD655;&#xC778;](../../../.gitbook/assets/image%20%28152%29.png)

> sudo netstat -nap \| grep 8888

이 번에는 sudo 명령어를 입력해주세요. 참고로 sudo는 \(sbustitue user do\)라는 의미를 가지고 있어요.

![sudo &#xBA85;&#xB839;&#xC5B4; &#xC785;&#xB825;](../../../.gitbook/assets/image%20%28166%29.png)

 프로세스 ID가 우측 상단에 18317인거 보이조?   


2단계의 프로세스를 꺼버리는 명령어를 넣어볼게요.   
이떄는 sudo의 kill 을 사용해요.   


> sudo kill -9 18317

![&#xC11C;&#xBC84;&#xC5D0;&#xC11C; &#xC8FC;&#xD53C;&#xD130; &#xAEBC;&#xBC84;&#xB9AC;&#xAE30;](../../../.gitbook/assets/image%20%2897%29.png)

####  주피터 노트북 설정 파일 

config 파일에 HTTPS를 적용 해볼게요.   
/home/ubuntu 경로에 ssl 폴더를 만들고 ssl을 만들어 볼건데요. 다시한번 ssl에 대해 설명하면 \_\_통신 보안을 위한 도구\_\_라고 보면 되요.   
 더 자세한 사항은 \_\_공개키 구조\_\_ 에 대해 별도로 학습해주세요. 

![ssl &#xC778;&#xC99D;&#xC11C; &#xC0DD;&#xC131;](../../../.gitbook/assets/image%20%2835%29.png)

> pwd \# \(print working directory\)를 넣어주세요.  
> mkdir ssl   
> cd sslㅊ   
> sudo openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout "cert.key" -out "cert.pem" -batch

1번부터 4번까지 차례대로 입력해보세요. 3번까지는 문제없이 진행될텐대요.   
4번에서 openssl이 있는데 기본적으로우분투에에 설치되어 있어요.  이! \_\_openssl\_\_을 이용해서 자신만의 사설 인증서를 만들 수 있어요. 

cert.key라는 개인키와 cert.pem이라는 공개키가 각각 생성되었어요.   


```text
# 만약 위의 과정이 잘 안된다면 아래 과정을 참고해보세요. 

첫번째, AWS 인스턴스 연결 버튼 누르고 팝업창에 ssh 나왔던거 기억나시조 그거 그대로 복사해서 터미널창에 입력해주세요.

> ssh -i "new_keypair.pem" ubuntu@ec2-18-191-177-247.us-east-2.compute.amazonaws.com

두번째, ssl이라는 폴더에 공개키 파일과 개인키 파일을 만들어 볼게요. 
> mkdir ssl
> cd ssl 
> sudo openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout "cert.key" -out "cert.pem" -batch 
> dir(window) or ls(Linux) 

아래와 같이 결과가 출력되요. 
Generating a RSA private key
....................................................................+++++
.......................+++++
writing new private key to 'cert.key'
-----

```

> ls \# 현재폴더의 파일들을 확인해주세요.

![](../../../.gitbook/assets/image%20%28179%29.png)



> sudo vi /home/ubuntu/.jupyter/jupyter\_notebook\_config.py

위 명령어는 기본적으로 동일합니다. 그대로 복붙해서 주피터노트북의 설정파일을 실행해볼게요. 

![sudo vi /home/ubuntu/.jupyter/jupyter\_notebook\_config.py](../../../.gitbook/assets/image%20%28136%29.png)



개인키와 공개키의 위치를 넣어줄게요.  맨 마지막으로 커서를 쭉쭉 내려주세요. 

> c.NotebookApp.certfile = u'/home/ubuntu/ssl/cert.pem'

> c.NotebookApp.keyfile = u'/home/ubuntu/ssl/cert.key'

![](../../../.gitbook/assets/image%20%28161%29.png)

저장하고 vim에서 나와\(:wq\)주세요. 

> sudo jupyter-notebook --allow-root

![&#xC8FC;&#xD53C;&#xD130; &#xC2E4;&#xD589; ](../../../.gitbook/assets/image%20%2834%29.png)

https가 붙은거 보이조?    
서버가 background에서 잘 작동되도록 해볼게요. 

```text
디렉토리 설정부분, 오타, 잘 확인하시고 따라해보세요.
```

ctrl+z를 눌러서 나가 주시고 

> bg \# background 옵션을 넣어주세요.

> disown -h \# 소유권을 포기합니다.

이제 콘솔을 닫고 실행하면 이제 주피터 노트북이 실행중이다라는걸 알수 있어요. 

#### https://xx.xxx.xxx.xxx:8888 

![&#xC815;&#xC0C1;&#xC801;&#xC73C;&#xB85C; &#xC811;&#xC18D;&#xB41C;&#xAC70;&#xC785;&#xB2C8;&#xB2E4;. ](../../../.gitbook/assets/image%20%28145%29.png)

인증서를 통해 접속된걸 확인할수 있습니다. 다만 우리가 만든 인증서는 공인인증기관 \(**Comodo, Thawte, GeoTrust, DigiCert\)에서 돈주고 한게 아니라서 저렇게 웹브라우저가 위험하다는 느낌표를 보여주는거에요.** 

직접 만든 사설 인증페이지라서 위험하다고 나오는건데요. 고급에서 안전하지 않 링크를 눌러서 페이지를 이동하면 됩니다. 

