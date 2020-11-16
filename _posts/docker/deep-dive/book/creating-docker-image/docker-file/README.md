# Docker File

### 이미지를 생성하는 방

개발한 애플리케이션을 컨테이너화할 때 가장 먼저 생각나는 방법은 아래와 같아요.

* 아무것도 존재하지 않는 이미지\(우분투, CentosOS 등\)로 컨테이너를 생성
* 애플리케이션을 위한 환경을 설치하고 소스코드 등을 복사해 잘 동작하는 것을 확인
* 컨테이너를 이미지로 commit 



 그림1 

이 방법을 사용하면 애플리케이션이 동작하는 환경을 구성하기 위해 일일이 수작업으로 패키지를 설치하고 소스코드를 깃에서 복제하거나 호스트에서 복해야해요. 당근 직접 컨테이너에서 application을 실행해서 이미지로 commit도해서 image의 동작을 보장하는 장점도 있어요. 

 그림2

첫번째 이미지를 더욱더 손쉽게 하는 명령어가 **build 명령어**에요.  
완성된 이미지를 생성하기 위해 컨테이너에 설치해야 하는 **패키지**, 추가해야하는 **소스코드**, 실행해야하는 **명령어**와 **shell script** 등을 **하나의 파일에 기록**해 두면 도커는 이 파일을 읽어 --&gt; **컨테이너에서 작업**을 수행한 뒤 --&gt; **이미지로 만들어**내야해요. 

1. 패키지, 소스코드, 실행할 명령어, shell script등을 한 파일에 기록  --&gt; 여기서 말하는 파일이 **Dockerfile**
2.  **Build 명령어\(read dockerfile\)로 Image를 생성**  

**Dockerfile 작성 목적**

1. 이미지 자체를 배포하는 대신, 이미지를 생성하는 방법을 기록해둔 Dockerfile을 배포할 수도 있어요. 
2. 만약 배포된 이미지를 신뢰할 수 없거나 직접이미지를 생성해서 사용하고 싶으면 도커 허브에 올려진 Dockerfile로 build할 수도 있어요. 

* Dockerhub의 대부분의 이미지는 Dockerfile을 함께 제공하고 있어요. 

### Dockerfile 작성

Dockerfile에는 Container에서 수행해야할 작업을 명시합니다.   
그 작업을 위한 명령어를 알아둘 필요가 있어요. 

#### 실습 

웹 서버 이미지를 생성하는 예를 살펴볼게요. 

1. 디렉토리 생성 
2. 해당 디렉토리에 HTML 작성

{% tabs %}
{% tab title="" %}
```text
# mkdir dockerfile && cd dockerfile 
# echo test >> test.html 

# ls 
test
```
{% endtab %}
{% endtabs %}

**bash 명령어**

1. && : 한 줄에서 명령을 여러 개 실행합니다. 단 앞에 있는 명령이 error 없이 실행되어야 뒤에 오는 명령이 실행되요. 
2.  &gt;&gt; : 명령 실행의 표준 출력\(stdout\)을 파일에 추가해요. 이미 있는 파일에 내용을 덮어 쓰지만  &gt;&gt; 는 파일 뒷 부분에 내용을 추가합니다. 

 

새롭게 생성한 디렉토리 내부에서 아래의 내용으로 Dockerfile이라는 이름의 파일을 저장해요. 아래의 Dockerfile은 이미지에 아파치 웹 서버를 설치한 뒤, 로컬에 있는 test.html 파일을 웹 서버로 접근 할 수 있는 컨테이너의 디렉토리인 /var/www/html에 복사합니다.

아래 소스 코드는 아파치 웹 서버가 설치된 이미지를 빌드하는 Dockerfile

{% code title="Dockerfile" %}
```text
# vi Dockerfile 

From ubuntu: 14.04
MAINTAINER alicek106
LABEL "purpose"="practice"
RUN apt-get update
RUN apt-get install apache2 -y
ADD test.html /var/www/html
WORKDIR /var/www/html 
RUN ["/bin/bash", "-c", "echo hello >> test2.html"]
EXPOSE 80
CMD apachectl -DFOREGROUND
```
{% endcode %}

{% tabs %}
{% tab title="참고" %}
```text
Dockerfile이라고 이름을 짓는 이유는 Docker는 기본적으로 현재 디렉토리에 있는 Dockerfksms 
이름을 가진 파일을 선택해요. 그래서 Dockerfile이라는 파일을 저장했어요. 

```
{% endtab %}
{% endtabs %}

### Dockerfile 명령어 

1. 기본 FROM, RUN, ADD 
2. 한줄이 하나의 명령어 
3. &lt; 명령어 + 옵션&gt;  구조
4. 명령어는 소문자, 대문자로 표현함\(일반적으로 대문자 표기 \) 
5. 위에서 아래로 한줄 한줄씩 명령어를 실행함

> **FROM**  
> 생성할 이미지의 베이스가 될 이미지를 뜻해요. FROM 명령어는 한번이상입력하고, 이미지 이름은 처음 docker run\(docker pull\)에서 이미지 이름을 사용할때와 동일해요. 만약 이미지가 도커에 없으면 자동으로 pull하게되요.

> **MAINTAINER  
> 개발자의 이메일 정보.   
> 요새는 MAINTAINER는 더이상 사용하지 않는다고 하네요. 대신 아래와 같이 쓴다고 해요.**

```text
LABEL maintainer "osori1123 <osori1123@gmail.com>"
```

> **LABEL  
> 이미지에 메타데이터를 추가해요. 메타데이터는 '키:값'의 형태로 저장되며, 여러 개의 메타데이터가 저장될 수 있어요. 추가된 메타데이터는 docker inspect 명령어로 이미지의 정보를 확인 할 수 있어요.**

\*\*\*\*

> RUN  
> 컨테이너 내부 실행 명령어.   
> apt-get update와 apt-get install apache2 명령어를 실행하기 때문에 아파치 웹 서버가 설치된 이미지가 생성되요.   
> **단, Dockerfile을 이미지로 빌드화 하는 과정에서는 별도의 입력이 불가능하기 때문에 apt-get install apache2 명령어에서 설치할 것일지를 선택하는 Y/N를 YES로 설정해야해요.** 이미지를 빌드할 시 별도의 입력을 받아야하는 RUN이 있다면 build 명령어는 이를 오류로 간주하고 빌드를 종료해요.

{% tabs %}
{% tab title="참고 " %}
```text
RUN 명령어에 RUN ["/bin/bash", "-c", "echo hello >> test2.html"]과 같이 입력하면 /bin/bash 셸을 이용해 'echo hello >> test2.html'을 싱행합니다. 
Dockerfile의 일부 명령어는 이처럼 배열의 형태로 사용할 수 있습니다. 

RUN의 경우에는 아래와 같은 형태로 사용되요. 

RUN ["실행 가능한 파일", "명령줄 인자 1", "명령줄 인자 2, ...]

이는 JSON 배열의 입력 형식을 따르기 때문에 JSON 형식과 일치해야 해요. 단, JSON 배열 형태로 Dockerfile의 
명령어를 사용하면 셸을 실행하지 않아요. 

예를 들어, ["echo", "$MY_ENV"]는 $MY_ENV 환경변수를 사용하지 않아요. 
이 형태로 셸을 사용하려면 ["SH", "-c", "echo $MY_ENV"]와 같이 사용하는 것이 좋아요. 
```
{% endtab %}
{% endtabs %}

> **ADD  
> 파일을 이미지에 추가하는 명령어.**   
> 여기서 추가하는 파일은 Dockerfile이 위치한 디렉토리인 컨텐스트에서 가져와요**. Dockerfile이 위치한 디렉토리에서 파일을 가져오게 되요.**
>
> **ADD명령어는 JSON 배열 형태로 \["추가할 파일 이름", ... "컨테이너에 추가될 위치"\]와 같이 사용할 수 있어요. 추가할 파일명은 여러개를 지정할 수 있으며 배열의 마지막 원소가 컨테이너에 추가될 위치에요**

> WORKDIR  
> 명령어를 실행할 디렉토리를 나타내요. 배시 셸에서 CD 명령어를 입력하는 것과 같은 기능을 해요.   
> 예를들면,   
> WORKDIR /var/www/html이 실행되고 나서 RUN touch test를 실행하면   
> /var/www/html 디렉토리에 test파일이 생성되요.

{% tabs %}
{% tab title="참고" %}
```text
WORKDIR 명령어를 여러 번 사용하면 cd 명령어를 여러번 사용하는 것과 동일해요. 

WORKDIR /var
WORKDIR /www/html
```
{% endtab %}
{% endtabs %}

