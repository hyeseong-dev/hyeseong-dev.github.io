---
description: 이미지와 레이어에 대한 기초 개념
---

# Image & Layer

### Docker 정보를 확인 

```text
docker info 
```

![docker info &#xAC00; &#xCD9C;&#xB825;&#xB41C; &#xD654;&#xBA74;](../../.gitbook/assets/image%20%2888%29.png)

 맨 아래 부분을 먼저 보면  **docker 디렉토리**의 **절대 경로**를 보여줘요.    
그리고 다음 Storage Driver를 보게되면 **overlay2** 보이나요?  
실제 레이어가 관리되는 디렉토리에요. 

![container, image, overlay2 &#xB514;&#xB809;&#xD1A0;&#xB9AC;](../../.gitbook/assets/image%20%28188%29.png)

- **containers** : 컨테이너가 생성되면 보관하고 관리하는 폴더  
- **image** : image들을 **run 또는 pull** 명령어로 다운받으면 관리되는 폴더  
- **overlay2** : 실제적인 데이터인 레이어들이 보관 관리되는   




####  디스크 크기 확인 명령어 

#### 방법1: du -sh 디렉토리명

#### 방법2:  du -sh \*

![&#xBC29;&#xBC95;1](../../.gitbook/assets/image%20%28189%29.png)

![&#xBC29;&#xBC95;2](../../.gitbook/assets/image%20%2871%29.png)

### 이미지 레이어 정보 확인 

 **inspect** 명령어를 통해서 해당 이미지의 레이어 정보를 확인 할 수 있어요. 

```text
docker inspect 이미지명 
```

 많은 정보들이 출력되는데 필요한 부분만 볼게요.   
우선 첫번째로 **Id**값 보이나요?

![id, repotags, created, hotname, exposedports](../../.gitbook/assets/image%20%2845%29.png)

 **Id :** sha256이라는 알고리즘을 돌려서 헤쉬값으로 돌려줬어요.   
**RepoTags :** 다운 받을시 별도로 지정하지 않았다면 latest로 잡아서 최근 버전을 다운로드 해와요.   
**Created** : 만들어진 시간   
**Hostname : ~~  
ExposedPorts: 서비스가 실행되는 포트 번호에요.**

  


![Env, Cmd](../../.gitbook/assets/image%20%28111%29.png)

 **-** **Env**: 환경 변수가 등록된 부분이에요.   
 **- Cmd**: 컨테이너로 바꾸어서 실행하였을 경우 어떤 프로세스를 실행할지를 결정해줘요.   
"/bin/sh"에 "-c"옵션을 줘서 실행되요. "CMD \[\"nginx\" \"-g\" \"daemon off;\"\]" nginx를 실행하고 -g daemon off라는 옵션을 준다는 말이에요.   


![RootFS](../../.gitbook/assets/image%20%2855%29.png)

* **RootFS :** 파일 시스템을 구성해주는 부분. 아래에 헤쉬값으로 된 레이어 3개가 있어요.  pull하게되면 이 3개를 다운로드 받게되는거에요.  반대로 rmi 명령어를 넣으면 이 3가지가 삭제되요. 





#### 이미지에 대한 구성 방법 

![image, overlay2 diretory](../../.gitbook/assets/image%20%2866%29.png)

이미지들은 이미지 디렉토리에 저장되어 관리되요.   
하지만 이미지에 있는 데이터들의 실제적인 정보는 overlay2에 있어요.   


![overlay2](../../.gitbook/assets/image%20%28175%29.png)

 docker/image/overlay2에 가면 **imagedb**와 **layerdb** 보이조?  
 이 둘을 파헤쳐 볼게요.   
****

![ls -R imagedb ](../../.gitbook/assets/image%20%28141%29.png)

 **ls -R imagedb명령문** 실행하게 되면, 회귀\(Recursive\)해서 아래 디렉토리에 무엇이 들어 있는지 보여주게되요.   
 sha256의 헤쉬값이 들어있어요.   
이 점을 머릿속에 두고 layerdb로 가볼게요.   


![](../../.gitbook/assets/image%20%28130%29.png)

![](../../.gitbook/assets/image%20%2813%29.png)

 여기서 중요한건 sha256의 헤쉬값이 imagedb 디렉토리와 layerdb에 있는것이 다르다는 것이에요.   
   


![](../../.gitbook/assets/image%20%28174%29.png)

 정리하면 image -&gt; overlay -&gt; imagedb, layerdb, 이미지폴더안에는 imagedb와 layerdb에 관한 정보가 있어요.   
하늘색으로 그어진 layerdb에 관한 정보는 결국 overlay2에서 가지고 있어요.    
그래서 **실제 데이터가 들어있는 부분은 docker 디렉토리안의 overlay2 디렉토리에요.**   
  


![](../../.gitbook/assets/image%20%2844%29.png)

 overlay2 디렉토리로 가면 여러 디렉토리가 있어요. 맨 아래 l\(알파벳 소문자 L\)을 제외하고 나머지는 변경사항들을 저장하고 있고요. L디렉토리로 가면 실제 파일시스템이 들어 있어요.

![&#xC694;&#xC57D;&#xB3C4;](../../.gitbook/assets/image%20%2865%29.png)

L\(소문자\)이라는 녀석에 실제적인 layer 파일시스템이 있어요.   
그래서 run으로 실행시켜 create  명령어까지 포함하면 overlay2디렉토리크기가 커져 메모리 낭비가 발생하게 되는거에요. 

방금 말한 부분을 보여드릴게요.   
이해를 쉽게 하기 위해서 기존에 있던 이미지와 컨테이너를 다 싹지워버렸어요.   
**참고로: 이미지 컨테이너 지우는 명령어는 아래와 같아요.** 

> docker system prune -a -f

![&#xB3C4;&#xCEE4;&#xC548;&#xC758; &#xBAA8;&#xB4E0; &#xC774;&#xBBF8;&#xC9C0;&#xC544; &#xCEE8;&#xD14C;&#xC774;&#xB108; &#xC0AD;&#xC81C;](../../.gitbook/assets/image%20%28143%29.png)

 **overlay2** 디렉토리의 용량이 8.0k가 된거 보이시조

> docker run -d -p 8080:8080 consol/tomcat-7.0
>
> run 명령어로 로컬에서 이미지를 찾고 없을 경우 다운받고 있으면 그대로 쓰고  컨테이너 생성과 실행을 한방에 해봤습니다.

![](../../.gitbook/assets/image%20%28168%29.png)

 56K  containers/  
 2.6M  image  
 1.4G   overlay2/  
 1.4G   /var/lib/docker   
  
**결론적으로 overlay2가 docker 용량을 책임지는 곳입니다.** 

\*\*\*\*

**run 명령어로 컨테이너를 추가로 생성시켜볼게요.**   


![&#xCEE8;&#xD14C;&#xC774;&#xB108; 3&#xAC1C; &#xC0DD;&#xC131; ](../../.gitbook/assets/image%20%28167%29.png)

 컨테이너 3개를 만들었으니 디스크 크기 변화 확인을 해볼게요.

![](../../.gitbook/assets/image%20%28153%29.png)

1.4G 였는대 --&gt; 2.5G로 용량이 증가된걸 볼겁니다.   
그렇다면 핵심은 쓸떼없는 container create생성을 최소화 해야하는데 그 핵심이 run으로 불필요하게 자동으로 container 생성을 하지 말자는 말이에요.   
단순한 container 실행은 start 명령어로 실행해주는거에요.

\*\*\*\*

\*\*\*\*

