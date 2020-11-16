# Dockhub & Github 연동

##  왜? 연동해야하나요? 

Dockerhub & Github 연동법에 대해 알아 볼게요.   


연동하면 어떻게 되냐고요?  깃허브의 특정 레포지토리에 있는 Dockerfile을   
Dockerhub에서 자동으로 build를 수행해 이미지를 생성해줘요.   
  
즉, Github에 소스코드만 upload 해주면 Dockhub측이 알아서 이미지를 생성해준다는 말이에요. 결국 서버를 만들고 실행하는게 매우매우 쉬워진다는 말이에요. 



### 준비물 

1. Dockerhub & Github 계정과 Repository 



###  Dockerhub 계정 설정

 Github 연동을 위한 설정 작업이 필요해요. 

* 우측 상단의 본인ID를 클릭 -&gt;
* "Account Settings"클릭 -&gt;
* 화면 좌측 사이드 메뉴바에 "Linked Accounts" 클릭 -&gt;
* Github라고 쓰여진 곳 우측에  "disconnect"를 클릭하고 인증절차 수행.

##  Step1 도커허브 저장소 생성  

* 맨 위 메뉴바 Repositories라고 쓰여진 곳 클릭 
* "Create Repository" 버튼 클릭\(우측 상단\)
* Name에 Repository 이름 작성\(docker-practice라고 작성\)
* Visibility -&gt; Private 선택 
* Build Settings\(optional\) -&gt; github 클릭해서 Connected 상태변환
  * "Select organization"  -&gt; Github username 선택 
  * "Select repository" -&gt; "Docker-Practice" 저장소 선택
* 'Create & Build" 버튼 클릭 
* 본인이 만든 Dockerhub 저장소로 화면 전환
* **"Builds" 카테고리 클**
* **"Configure Automated Builds" 클릭**
* SOURCE REPOSITORY 

  * 본인 github 유저네임 선택 
  * Dockerfile이 있는 저장소 선택\(Docker-Practice\)

* Save & Build 클릭

 여기 까지 했다면 거의 완료된거나 다름 없어요.   
본인 저장소의 Builds 페이지로 바뀌고 Pending이라는 글자가 반짝이는게 보일거에요. 자동으로 이미지 빌드중이에요 \(약 5~10분 소요\)  
성공적으로 빌드가 되면 Pending --&gt; Success라고 바껴요.

## Step2 빌드된 이미지 확인 

Builds 화면 페이지\(Pending -&gt; Success라는 글자가 나타난 페이지\)에서   
Recent Builds라는 곳 보이조?   
Build in 'master'\(숫자와알파벳\) 클릭   
BUILD LOGS, DOCKERFILE, READEME 이렇게 또 글자들이 보일거에요. 

* BUILD LOGS는 이미지 빌드시 수행된 기록들을 말하고요.
* DOCKERFILE은 이전 시간에 우리가 작성한 DOCKER FILE 작성 명령어들이 쓰여져 있어요. 
* README는 지시서라고 보면 될거에요. 해당 이미지를빌드하기위한 절차들을 나열하거나 주의사항들을 기입하는건데 이부분은 조금있다 작성해볼게요. 

## Step3 README 파일작성 

* github 저장소\(Docker-Practice\)로 이동
* 우측하단에 "Add a README"버튼 클릭

  * 이미 README.md 파일이 있다면, 선택 후 편집 \(연필모양 그림 클릭\)

* Dockerfile 내용을 근거로 작성
* 스크롤 내려서 Commit new file이라는 부분 아래에 Create README.md라고 쓰고 "Commit new file" 클릭

 아래 내용은 해당 이미지를 다운 받을때 수행해야하는 단계별 명령어를 아래와 같이 수행하라는 지침서 역할을 하는거에요. 

```text
# Docker-Practice
## Installation 
<pre>
cd /home
git clone https://github.com/osori-magu/Docker-Practice
cd Docker-Practice
</pre>

### Run
<pre>
# Login For Private Docker Repository
docker login 
docker pull hyeseong43/docker-practice
docker run -p 80:80 -v /home/Docker-Practice/Project:/var/www/html hyeseong43/docker-practice
</pre>

```

README.md 파일이 작성이 github에서 완료되었다면 Dockerhub에서도 동일하게 이 파일이 작성한 내용들을 볼 수 있어요. Step2 빌드된 이미지 확인 부분에서 README 부분이 동일하게 보여질거에요. 

## Step4 README 파일실습 

 누군가가 이제 우리가 작성한 README파일을 보고 따라한다면 저희가 그 밑작업을 해줘야 하는 부분이 있어요. 바로 이미지 파일이 온전하도록 디렉토리 구성을 해줘야하는대요. 

 특히 README 파일 14번째 줄에 호스트 경로와 Project폴더에 index.php파일을 완전히 구성하여 만들기 위해서에요. 

일단 아래처럼 디렉토리 구성과 파일이동을 시키고 git작업을 할게요. 

* 터미널을 열어주세요. 

{% tabs %}
{% tab title="Plain Text" %}
```text
$ docker images # 이미지 파일이 다 삭제되었는지 확인해주세요. 
$ cd /home/ubuntu # 디렉토리 이동
$ ls
Docker-Practice  example  ssl # ls 명령어로 하위 파일과폴더확인
$ cd Docker-Practice # 디렉토리 이동 
$ mkdir Project # 서브 디렉토리 생성
$ mv index.php ./Project # index.php 파일 서브 디렉토리로 이동
$ cd Project 
$ ls 
index.php
$ cd ..         # .git폴더가 있는 Docker-Practice폴더로이동
$ git add . 
$ git git commit -m 'change index.php path' # 커밋메시지
$ git pull # push 작업하면 충돌의 우려가 있어요. + login 작
$ git push # git push 완료. 


```
{% endtab %}

{% tab title="디렉토리 구조" %}
```
home
├── Docker-Practice
│   ├── Dockerfile
│   ├── Project
│   │   └── index.php
│   └── README.md
```
{% endtab %}
{% endtabs %}

 여기 까지 했다면 이제 작업을 다시 시작해볼게요.   
다른 사용자가 나의 이미지를 설치를 위해 README를 보고 따라한다고 생각하고 실습하는거에요.

```text
rm -rf Docker-Practice 

cd /home
git clone https://github.com/osori-magu/Docker-Practice
cd Docker-Practice

docker login 
docker pull hyeseong43/docker-practice
docker run -p 80:80 -v /home/Docker-Practice/Project:/var/www/html hyeseong43/docker-practice
```



##  결론 

1. github에 commit, push 과정만으로 이미지가 자동 빌드되게 만들 수 있음. 
2. 
![](../../.gitbook/assets/image%20%28219%29.png)







  




 











