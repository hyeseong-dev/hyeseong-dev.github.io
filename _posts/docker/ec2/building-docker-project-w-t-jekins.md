# Building Docker Project w/t Jekins

## 이번에 배울건? 

젠킨스를 설치해서 도커 프로젝트를 빌드해 볼게요. 

젠킨스를 이용하면 배포 자동화가 가능해져요. 말그대로 소스크드만 올려서 깃허브에 Push하게되면 알아서 서버에 배포까지 완전히 맞춰주는 그런 작업이 가능하게되요. 

젠킨슨을 이용하면 그런 작업이 더욱 쉬워져요. 

## Step1 Jenkins img PULL & RUN

* 쥬피터 터미널을 열어주세요. 
* 현재 실행중인 컨테이너가 있다면 삭제해주세요. 
* ```text
  docker ps -a 
  docker rm -f 컨테이너ID
  ```
* 젠킨스 이미지 다운로드 

```text
docker pull jenkins
```

*  젠킨스를 다운 받는 이유는 젠큰슨 역시 컨테이너로 사용하기 위해서에요. PHP컨테이너를 이전에 띄웠던것처럼 말이지요.   이런 방식을 Dokcer in Docker라고 해요. 
* jenkins을 run 명령어로 실행 



```text
docker run -d -p 8080:8080 \
-v /home/jenkins:/var/jenkins_home \
-v /var/run/docker.sock:/var/run/docker.sock \
-u root jenkins
```

젠킨슨은 기본적으로 8080포트를 사용해요. 호스트의 8080과 젠킨슨의 8080포트를 이어 줄게요.   
2번째 줄은 EC2 서버의 home/jenkins 경로를 설정하고 이를 볼륨마운팅하건데요. 컨테이너 안의 var/jekins\_home 경로와 이어주는 작업을하고요. 

3번째 줄은 jenkins 컨테이너 안에서 새로운 php컨테이너를 실행 시키기 위해서 볼륨마운팅 작업을 하는거에요. 그래서 docker.sock파일을 마운팅해주는거에요. 

4번째 줄은 root계정으로 이 jenkins 계정을 실행해주면 되요. 

 실행후 긴 헤쉬값이 나오는데 jekins 관리자 비밀번호를 확인할수 있는 로그 값이 나와요.\(비밀번호가 아닌 비밀번호를 확인하는 열쉬라고 보면되요.\)

## Step2 Open EC2 firewall

* EC2 인스턴스 -&gt; 보안그룹 -&gt; 인바운드 규칙편집 -&gt; 8080포트를 설정
* 웹브라우저에 EC2IP:8080 접  -&gt; 관리자 비밀버호 입력화면이 나옴 
* 터미널로 돌아가서 docker logs 젠킨스컨테이너의 로그

```text
docker logs 9e3831a2e8ce102baa60dd8be61e5dac45ddce87ab3a6d1340b9335f68b1c208

*************************************************************
*************************************************************
*************************************************************

Jenkins initial setup is required. An admin user has been created and a password generated.
Please use the following password to proceed to installation:

183348509df04e05b73e3542f396643a

This may also be found at: /var/jenkins_home/secrets/initialAdminPassword

*************************************************************
*************************************************************
*************************************************************
```

* 중간에 1833 비밀번호가 보이조? 그대로 복사해서 웹브라우저에 입력해주세요.

### Step3 Installing Jenkins plugins 

 배포 자동화를 위한 젠킨스 플러그인 설치를 진행해 볼게요. 

* Install suggested plugins 클릭 
* 설치중 아래와 같은 오류가 발생하지만 continue를 눌러 넘어갈게요.

![](../../.gitbook/assets/image%20%28218%29.png)

*  계정명, 비밀번호, 이름을 입력하는 페이지를 작성 -&gt; Save & Finish
* Jenkins에 오신걸 환영합니다라는 문구가 나오면 성공! 

### Step4 Building A PHP Docker Project w/h Jenkins

실제로 PHP Docker Project를 빌드해서 젠킨스로 배포해보도록 해볼게요. 

* '시작하려면 새 작업을 만들어 주시기 바랍니다' 클릭
*  'Enter an item name'에 'Example'이라고 입력 
* Freestye project 선택 -&gt; OK버튼 클
* 아래 Build 탭 클릭 Excute shell의 Command창에 아래와 같은 명령문을 넣어주세요. \(이미 README.md파일에 작성했어요.

```text
docker pull hyeseong43/docker-practice
docker run -p 80:80 -v /home/Docker-Practice/Project:/var/www/html hyeseong43/docker-practice
```

* 저장 버튼 클릭 
* 왼쪽 사이드바, Build Now 버튼 클릭 
* Console Output 카테고리를 눌러 상세내역 확인 

> 만약 오류 발생시 '대시보드로 돌아가기'를 클릭 -&gt; '구성'클 -&gt; 오타가 없는지 빌드명령 재확인

> 오류 문구중에 docker : not found라고 뜬다면 jenkins컨테이너에 docker가 없다는 말이에요. 그럼 설치해야겠조?

### Step5 installing Docker in a Jenkins container

* 터미널에서 docker ps -a 명령어 실행 
* docker exec -it 젠킨스컨테이너ID /bin/bash
* curl -fsSLO https://get.docker.com/builds/linux/x86\_64/docker-17.04.0-ce.tgz
* tar xzvf docker-17.04.0-ce.tgz

```text
$ docker ps -a 
$ docker exec -it 컨테이너ID(젠킨스) /bin/bash
$ curl -fsSLO https://get.docker.com/builds/linux/x86_64/docker-17.04.0-ce.tgz
$ tar xzvf docker-17.04.0-ce.tgz
```

* bin 폴더로 도커의 실행 폴더를 이동시킬게요. 
*  디스크 용량을 줄이기 위해 기존 다운 받은 압축 파일은 삭제할게요. 
* 도커 로그인\(private repository 이용을위해\)
* index.php가 실행되도록 git clone 명령어를 진행할게요. 
* 젠킨스 컨테이너를 나와주세요.\(exit\)
* 다시 젠킨스 웹사이트로 가서 Build Now 버튼을 누르면 성공적으로 되는걸 확인 할수 있어요. 
* 실제 EC2IP 접속하면 PHP와 MySQL이 연동된걸 확인 할 수 있어요. 

```text
$ mv docker/docker /usr/local/bin
$ rm -f docker docker-17.04.0-ce.tgz
$ docker login 
$ git clone https://github.com/osori-magu/Docker-Practice
```

## 결론 

1. 젠킨스를 이용한 도커 이미지 배포 시행 
2. 하지만 아직까지 온저한 자동 배포가 아님  직접 젠킨스의 설정을 마쳐서 이미지 빌드를 진행하였기 때문.
3. 다음 시간에는 원격으로 젠킨슨 배포를 더 쉽게 진행한 방법에 대해 학습 해볼게요. 

* 즉 특정 서버에 앱을 배포하고 싶을때 원격지에서 서버의 빌드를 진행 할 수 있다는 말이에요.

