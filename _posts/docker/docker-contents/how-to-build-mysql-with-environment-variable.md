---
description: 환경변수로 Mysql 구축하기
---

# How To Build Mysql with Environment Variable

Mysql 서비스를 구축해볼게요.  
그냥 설치해서 깔면 되지 왜 굳이 다루냐고요?   
**환경변수를 이용해서 설치**하고 서비스를 이용 가능한 상태로 만들어야해요.

## MySQL 설치 명령

![Dockerhub - Mysql](../../.gitbook/assets/image%20%28156%29.png)

 Mysql은 아이디와 패스워드를 전달 받아야 사용할 수 있느 서비스입니다. 페이지를 아래로 내려 보세요.   
아래 사진을 확대해서 보세요.   


![MySQL &#xC778;&#xC2A4;&#xD134;&#xC2A4; &#xC2E4;&#xD589;&#xBC29;&#xBC95;](../../.gitbook/assets/image%20%2829%29.png)

```text
$ docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:tag
```

**--name** 이라는 옵션뒤에 컨테이너의 이름을 만들어 주세요.  
여기선 some-mysql로 지었네요.    


-**e** : e는 환경변수를 의미해요. MYSQL\_ROOT\_PASSWORD=my-secret-pw 를 보면 우항이 비밀번호이고요 좌항이 환경변수의 변수명입니다.   
사실 환경변수를 넣지 않고 고정으로 컨테이너에 박아 넣으면 되지 않냐? 라고 의문을 가질수 있어요.   
그 경우 **초기화된 비밀번호**를 그냥 사용할 경우 해킹의 우려가 매우 높아요.

**즉, 이번 시간에 환경 변수를 어떻게 사용하는지에 대해 알아볼게요.**

**-d** : 백그라운드 실행 명령어에요.   
mysql을 실행하는데, **: 콜론**을 줘서 콜론뒤에 특정 버전을 입력해야해요

##  환경 변수를 사용해 데이터 전달 

```text
$ docker run -d --name nx -e env_name=test1234 nginx
$ docker exec -it nx bash 
$ printenv
$ printenv env_name
```

첫 줄의 명령어에 대해서는 앞서서 말했어요.  
   
두 번째 줄을 볼게요. exec 실행해라는 명령어에요.   
옵션으로 -it\(input terminal\)을 주고 nx\(컨테이너 이름\) bash app 을 실행하여라, 라는 말이겠조?  
  
세 번째 명령문은 **printenv**  
 환경변수를 출력하여라, 라는 명령문이에요. HOSTNAME ~ NGINX\_VERSION까지 여러 변수들이 나타나요.   
실행시 아래와 같아요.   


![printenv &#xBA85;&#xB839;&#xC5B4; &#xC2E4;&#xD589;&#xACB0;&#xACFC;](../../.gitbook/assets/image%20%28139%29.png)

네 번째 명령문은 특정 환경변수를 보고 싶을때 사용해요.

> printenv env\_name

![&#xD2B9;&#xC815; &#xD658;&#xACBD;&#xBCC0;&#xC218; &#xCD9C;&#xB825;](../../.gitbook/assets/image%20%28164%29.png)

## echo 명령어로 특정 환경수 출력 

```text
echo $env_name
```



### MySQL 구축 및 실행 

```text
$ docker run --name ms -e MYSQL_ROOT_PASSWORD='!qhdkscjf@' -d --rm mysql
```

> **반드시 docker환경에서 실행해야해요.  
> 저의 경우  nginx의 bash앱에서 명령어 돌리는 삽질을 해버렸어요. ㅜ.ㅜ**

 다시 돌아와서 run명령어를 이용해서 pull + create + start까지 한방에 했는데요. 그 결과는 ps -a 명령어로 확인가능해요. 

![mysql &#xC774;&#xBBF8;&#xC9C0;&#xB97C; &#xCEE8;&#xD14C;&#xC774;&#xB108;&#xB85C; &#xB9CC;&#xB4E0; &#xBAA8;&#xC2B5; ](../../.gitbook/assets/image%20%28177%29.png)

3306포트에 붙어있는걸 확인했어요. 



MySQL 안에 들어가서 실행해 볼게요. 이를 위해선 아래 명령문을 실행해주세요. -u\(user\), -p\(password\)

```text
$ docker exec -it ms mysql -u root -p
Enter password: 
```

![mysql&#xC774; &#xC2E4;&#xD589;&#xB41C; &#xBAA8;&#xC2B5; ](../../.gitbook/assets/image%20%2898%29.png)



#### DB 내용 확인 명령어 

> show databases

![](../../.gitbook/assets/image%20%28187%29.png)



