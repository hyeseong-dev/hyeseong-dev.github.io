# 애플리케이션구축

##  컨테이너 애플리케이션 구축 

![App&#xC744; &#xD558;&#xB098; &#xB610;&#xB294; &#xBD84;&#xB9AC;&#xB41C; Container&#xB85C; &#xAD6C;&#xC131;](../../.gitbook/assets/image%20%2822%29.png)

왼쪽처럼 데이터베이스와 웹 서버를 컨테이너 하나에 설치할 수 있어요.   
그러나 오른쪽과 같이 데이터베이스와 웹 서버 컨테이너를 구분하는  쪽이 도커 이미지를 관리하고 컴포넌트의 독립성성을 유지하기 easy하죠.   
사실 많은 사람들이 분리된 어플리케이션 컨테이너 구조를 추천하고 잇어요.   
**도커는 한 컨테이너에 프로세스 하나만 실행하는 것이 도커의 철학이기도 해요.**

### 

### 실습

> 참고로 가독성을 위해 \ 를 이용해 각 설정 옵션을 구분했어요. 그러니   
> 실제는 \ 없이 입력해도 상관 없어요.

{% tabs %}
{% tab title="MYSQL 이미지 이용 데이터베이스 컨테이너" %}
```text
docker run -d --name wordpressdb -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=wordpress mysql:5.7 
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="워드프레스 웹 서버 컨테이너" %}
```text
docker run -d -e WORDPRESS_DB_PASSWORD=password --name wordpress --link wordpressdb:mysql -p 80 wordpress
```
{% endtab %}
{% endtabs %}

첫 번째 명령어는 mysql 이미지를 사용해 데이터베이스 컨테이너를, 두 번쨰 명어는 미리 준비된 워드프레스 이미지를 이용해 워드 프레스 웹 서버 컨테이너를 생성해요.   


```text
docker ps 
CONTAINER        IMAGE        COMMAND         CREATED    STATUS    PORTS                    NAMES
47553801a162     wordpress    "/entrypoint.sh   ...        ...     0.0.0.0:32769->80/tcp    wordpress    
```

호스트와 바인딩된 port만 확인 하려면 docker port 명령어를 사용하세요.   
아래는 wordpress 컨테이너가 사용중인 호스트의 port가 출력된거에요.   


```text
docker port wordpress
80/tcp -> 0.0.0.0.:32769

# 0.0.0.0.:32769 -->80/tcp에서 0.0.0.0은 호스트의 활용 가능한 
모든 네트워크 인터페이스에 바인딩한다는 말이에요.d
```

호스트의 32769번 포트와 연결되었어요. 결국 호스트의 IP와 32769번 포트로 워드프레스 웹 서버에 접근 할 수 있어요. 웹브라우저에서 호스트 IP:32769로 접속 하였는 경우 성공적으로 아래와 같이 나와요. 

![&#xD30C;&#xC774;&#xC5B4; &#xD3ED;&#xC2A4;&#xC5D0;&#xC11C; &#xC811;&#xC18D;&#xD55C; &#xBAA8;&#xC2B5;](../../.gitbook/assets/image%20%28113%29.png)

#### 옵션 

-d : -it\(-i -t\)가 컨테이너 내부로 진입하도록 attach가 가능한 상태로 설정하면 -d\(Detached\)모드로 컨테이너를 실행해요. 백그라운드에서 동작하는 애플리케이션으로써 실행하도록 설정한다는 말이에요. 

**-d 옵션 실습**

```text
docker run -d --name detach_test ubuntu:14.04
```

컨테이너가 생성되었어도 바로 종료되서. docker ps명령어로 확인 할 수 없어요.   
docker ps -a 명령어를 입력하면 되요.   
  


![](../../.gitbook/assets/image%20%2861%29.png)

docker start로 컨테이너를 시작해도 컨테이너 내부에 터미널을 차지하는 foreground로써 동작하는 프로그램이 없으므로 컨테이너는 시작되지 않아요.   
그럼 반대로 mysql 컨테이너를 **-i -t 옵션으로 실행**하면 어떻게 될까요? 

```text
docker run  -i -t \ 
--name mysql_attach_test \
-e MYSQL_ROOT_PASSWORD=password \
-e MYSQL_DATABASE=wordpress \
mysql:5.7

initialzing database
```

 mysql이 포그라운드로 실행된 로그\(기록\)들이 출력되요. MYSQL 이미지는 컨테이너 실행시 mysqld가 실행되도록 설정되어있어요. 이 상태에서는 상호 입출력이 불가능하고 **단순히 프로그램이 포그라운드로 동작하는 모습만 관찰할 뿐**이에요.   


**그래서 -d 옵션을 설정해 컨테이너를 백그라운드로 돌리는 이유에요.** 

**-e** : 내부 환경 변수를 설정해주는 옵션이에요. 자주 사용하니 꼭 알아두세요. 

```text
... -e MYSQL_ROOT_PASSWORD=password ...
```

컨테이너의 MYSQL\_ROOT\_PASSWORD 환경변수의 값을 PASSWORD로 설정한다는 의미에요.   
확인해 볼려면 아래 명령어를 입력해주세요. 

```text
echo ${ENVIRONMENT_NAME}
```

컨테이너 내부에서 echo로 환경변수를 출력하면 -e 옵션에 입력된 대로 값이 설정돼 있음을 확인 할 수 있어요. 

```text
echo $MYSQL_ROOT_PASSWORD
password
```

그러나 echo 명령어를 사용하려면 입출력이 가능한 bash shell을 사용할 수 있는 환경이 필요해요. shell 환경을 사용하려면 docker attach 명령어로 컨테이너 내부로 들어가야 하지만 위에서 생성한 mysql container는 -d 옵션으로 생성되었으므로 attach 명령어는 의미가 사실상 없어요. attach를 쓰면 컨테이너에서 실행중인 프로그램의 로그 출력을 보게 될 뿐이에요. 

그러나 exec 명령어를 이용하면 컨테이너 내부의 shell을 사용할 수 있어요. 다음 명령어를 입력하면 mysql 컨테이너 내부에 bin/bash 프로세스를 실행하고, -i -t 옵션을 이용해 bash shell을 쓸 수 있게 해줘요. 

```text
> docker exec -it wordpressdb /bin/bash
> echo $MYSQL_ROOT_PASSWORD
password
```

 exec 명령어를 사용하면 컨테이너 내부에서 명령어를 실행한 뒤 그 결과괎을 반환받을수 있어요. 그러나 여기서 -it 옵션을 넣어 /bin/bash를 입출력이 가능한 형태로 exec 명령어를 사용했어요.  만약 -it 옵션을 넣어주지 않고 단순히 exec 명령어를 쓰면 컨테이너 내부에서 실행한 명령어에 대한 결과만 돌려줘요. 

```text
docker exec wordpressdb ls 
bin 
boot
dev
docker-entrypoint-initdb.d
... 
```

 설정된 환경변수가 실제로 MySQL에 사용되었는지 확인하려면 컨테이너 내부에서 mysql -u root -p를 입력한뒤 password를 입력하게되요. 

```text
> mysql -u root -p
Enter password: 
Welcome to the MySQL monitor. Commands end with ; or\g. 
Your MySQL connection id is 3 
Server version: 5.7.17 MySQL Community Server(GPL)
...
```

컨테이너에서 나올려면 Ctrl + P, Q를 입력하세요. 혹은 /bin/bash 를 종료하려면 exit를 입력하세요.   
exec로 mysql 컨테이너에 들어왔을때는 exit를 써도 컨테이너가 종료되지 않아요. 왜냐하면 mysqld 프로세스가 컨테이너 안에서 여전히 프그라운드 모드로 동작하고 있기 떄문이에요. 

```text
참고로 비밀번호를 내부의 환경변수로 설정하는것은 좋은 사례가 아니에요. 이런 경우에는 도커 스웜모드의 secret 혹은
쿠버네티스의 secret과 같은 기능을 활용해 안전하게 비밀번호를 전달하는것이 좋아요. 
```

--link  : A컨테이너 --&gt; B컨테이너로 access하는 방법중 simple한것은 NAT로 할당받은 내부 IP를 쓰는거에요. B 컨테이너의 IP가 172.17.0.3이라면 A컨테이너는 이 IP를 써서 B 컨테이너에 접근 할 수 있습니다. 그러나 도커엔진은 컨테이너에게 내부 IP를 172.17.0.2. 3,4...와 같이 순차적으로 할당되요.   
이건 컨테이너를 식잘할때 마다 재할당하는 것이라서 매변 변경되는 컨테이너의 IP로 접근하기는 어려워요. 

 사실 link 옵션은 내부 IP를 알 필요 없이 항상 컨테이너에 alias\(별명\)으로 접근하도록 설정해요.   
위에서 생성한 워드프로세스 웹 서버 컨테이너는 --link 옵션의 값에서 wordpressdb 컨테이너를 mysql라는 이름으로 설정했어요. 

```text
... --link wordpressdb:mysql ...
```

결국, 워드 프레스 웹 서버 컨테이너는 wordpressdb의 IP를 몰라도 mysql이라는 호스트명으로 접근할 수 있게 되었어요. 워드프레스 웹 서버 컨테이너에서 mysql이라는 호스트 이름으로 요청을 전송하면 wordpressdb 컨테이너의 내부 IP로 접근하는 것을 확인 할 수 있어요. 

```text
docker exec wordpress curl mysql:3306 --silent
rl&mysql_native_password Got packets out of order
```

--link 옵션을 쓸때 유의할 점은 --link에 입력된 컨테이너가 실행중이지 않거나 존재하지 않는다면 --link

