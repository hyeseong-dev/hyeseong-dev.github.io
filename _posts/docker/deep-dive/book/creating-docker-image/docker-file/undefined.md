# 이미지생성

상위 문서에서 dockerfile의 기본적 명령어를 이해했으면 Dockerfile을 빌드해볼게요. 

```text
docker build -t mybuild:0.0. ./
```

 **-t** : 이미지의 이름을 설정.  위 명령어 실행시 mybuild:0.0이라는 이름의 이미지가 생성되요. -t 옵션을 않넣으면 16진수 이름이 저장되요. 그러니 -t옵션 줘야 겠지요?   
  
**저장경로** 그리고 build 명령어 끝에는 Dockerfile이 저당된 경로를 입력하세요.   
참고로, 외부 URL로부터 Dockerfile의 내용을 가져와 빌드할 수 도 있어요.   
아래의 내용은 내부 빌드시 출력되는 화면이에요.  

![](../../../../../.gitbook/assets/image%20%2899%29.png)

최종적으로 mybuild:0.0 이라는 이름의 이미지가 생성되요.   
이 이미지에는 아파치 웹 서버가 설치되어있고, 컨테이너가 시작될 때 웹 서버를 실행하도록 CMD를 설정했기 때문에 별다른 설정 없이도 웹 서버가 실행되요. 



컨테이너를 실행해 볼게요. 

```text
docker run -d -P --name myserver mybuild:0.0
```

**-P 옵션** : 이미지에 설정된 EXPOSE의 모든 포트를 호스트에 연결하도록 설정해요. 위 Dockerfile에서 EXPOSE를 80번으로 설정했으며 이는 이미지에 '컨테이너의 80번 포트를 사용한다'는 것을 말해요. 

즉, 이미지를 생성하기 위한 Dockerfile을 작성하는   
  
**개발자로서**는 EXPOSE를 이용해 이미지가 실제로 사용될 때 어떤 포트가 사용돼야 하는지 명시할 수 있으며   
  
**이미지를 사용하는 입장**에서는 컨테이너의 애플리케이션이 컨테이너 내부에서 어떤 포트를 사용하는지 알 수 있게되요.   


docker ps  혹은 docker port 명령어로 컨테이너와 연결된 호스트의 포트를 확인할 수 있으며, 호스트의 IP와 이 포트로 컨테이너의 웹 서버에 접근 할 수 있어요.  
Dockerfile에서 ADD로 test.html 파일을, RUN으로 test2.html 파일을 웨베 서버 디렉토리인 /var/www/html에 추가했으므로 

**\[호스트IP\]:\[포트\]/test.html  혹은 test2.html로 접근해 각 파일의 내용을 학인할 수 있어요.** 

```text
docker port myserver 
80/tcp -> 0.0.0.0:32769
```

Docker에 이미지의 라벨을 purpose=practice로 설정했으므로 docker images 명령어의 필터에 이 라벨을 적용할수 있어요.   
아래의 명령어는 **--filter 옵션**을 통해 해당 라벨을 가지는 이미지, 즉 위에서 생성한 이미지만을 출력해요.

```text
docker images --filter "label=purpose=practice"

```

{% tabs %}
{% tab title="참고" %}
```text
라벨은 도커 이미지뿐만 아니라 컨테이너, 도커엔즌 등에 메타데이터를 
추가하는 유용한 방법이에요. 
컨테이너는 docker run 명령어에서 --label 옵션을 사용할 수 있으며
docker ps에서 --filter 옵션을 적용할수도 있어요. 

라벨은 부가적인 정보를 부여해서 원하는 조건의 컨테이너, 이미지 등을 쉽게 
찾을 수 있게 도와줘서 필히 기억해야해요.
```
{% endtab %}
{% endtabs %}

