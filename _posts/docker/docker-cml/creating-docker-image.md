# Creating docker image

 Docker Container &lt;----------&gt; Docker image 서로가 생성할 수 있는 관계임. 

##  컨테이너로부터 이미지 생성

####  문법

> **docker container commit 옵션    컨테이너 식별자  이미지명:태그명**

 **옵션** 

* --author, -a       : 작성자를 지정한다.\(예. ASA SHIHO&lt;Shiho@asa.seoul&gt;\)
* --message, -m : 메시지를 지정
* change, -c    : 커밋 시 Dockerfile 명령을 지정
* --pause, -p    : 컨테이너를 일시 정지하고 커밋한다.

 독자적으로 작성한 이미지는 DOcker HUB 등에서 공개할 것도 고려하여 작성자나 커밋 메시지를 붙여두는 것이 좋습니다. 

###  컨테이너로부터 이미지 작성 

![](../../.gitbook/assets/image%20%28947%29.png)

 설정한 작성자 정보는 docker image inspect 명령으로 확인 가능해요. 

###  작성한 이미지 상세 정보 확인 

![](../../.gitbook/assets/image%20%28944%29.png)

##  컨테이너를 tar 파일로 출력

가동 중인 컨테이너의 디렉토리/파일들을 모아서 tar 파일을 만들 수 있습니다.   
이 tar 파일을 바탕으로 하여 다른 서버에서 컨테이너를 가동시킬 수 있습니다.   
tar 파일의 작성에는 docker container export 명령을 사용합니다. 이 명령의 구문은 다음과 같아요. 

####  문법 

> **docker container export &lt;컨테이너 식별자&gt;**

특정 컨테이너를 latest.tar라는 파일로 출력하는 경우는 아래와 같이 하면 되요. 

#### 1\) 파일출력 2\) 생성된 tar 파일 상세정보 확

![](../../.gitbook/assets/image%20%28955%29.png)

##  tar 파일 -&gt; 이미지 작성 

 docker image import 명령을 사용하면 Linux OS 이미지의 디렉토리/파일로부터 Docker 이미지를 만들 수 있어요. 

####  문법

> docker image import &lt;file or URL&gt;  \| - 이미지명:태그

 압축된 디렉토리나 파일도 취급할 수 있어요.   
하지만 docker image import 명령에서 지정할 수 있는 파일은 하나뿐이므로 tar 명령등으로 디렉토리나 파일을 모아 놓아야해요. 이때 root 권한으로 실행하지 않으면 엑세스 권한이 없는 파일이 포함되지 않는 경우가 발생합니다.   


 docker image import 명령으로 지정할 수 있는 아카이브 파일은 다음고 같아요. 

* tar
* tar.gz
* tgz
* bzip
* tar.xz
* txz

###  이미지 작성 & 확인

![](../../.gitbook/assets/image%20%28956%29.png)

##  이미지 저장 

docker image save 명령을 사용하면 image를 -&gt; tar파일로 저장 할 수 있어요. 

 **문법**

> **docker image save 옵션 &lt;저장 파일명&gt; \[이미지명\]**

###  이미지 저장 예시 

![](../../.gitbook/assets/image%20%28959%29.png)

## 이미지 읽어들이기

 **문법**

> docker image load &lt;option&gt;

**예. export.tar 라는 이름의 이미지를 읽어 들이려면 아래의 명령을 실행하는데요. 읽어 들일 파일명은 -i 옵션으로 지정합니다.** 

 ****

![](../../.gitbook/assets/image%20%28960%29.png)

##  불필요한 이미지/컨테이너 일괄 삭제 

docker system prune 명령을 사용하면 사용하지 않는 이미지, 컨테이너, 볼륨, 네트워크를 일괄적으로 삭제해요.   


####  문법

> docker system prune \[option\]

#### option

* --all, -a : 사용하지 않는 리소스를 모두 삭제한다. 
* --force, -f: 강제 삭제

###  불필요한 리소스 삭제 

![](../../.gitbook/assets/image%20%28958%29.png)

![](../../.gitbook/assets/image%20%28957%29.png)



