# MySQL 컨테이너 생성

도커를 이용해서 MySQL DB가 포함되어 있는 컨테이너를 만들어 볼게요 . 우선 실습을 위해 아래 3가지를 진행할게요.

*  도커 컨테이너 확인 
*  도커 컨테이너 전부 삭제 
*  도커 이미지 전부 삭제 
*  이미지 목록 호출로 지워졌는지 재확

```text
docker ps -a 
docker rm -f $(docker ps -a -q)
docker rmi -f $(docker images)
docker images
```

## MySQL 도커 컨테이너 구동 

### 포트 포워딩 및 환경변수 설정

MySQL의 경우 도커 허브에 존재하는 이미지이기 때문에 별도의 과정없이, 즉시 다운받아서 이용할 수 있어요. 

```text
docker run -d -p 9876:3306 -e MYSQL_ROOT_PASSWORD=password mysql:5.6
```

우리서버의 9876포트를 열어서 MySQL의 기본포트인 3306포트와 연결하도록 할게요. 



-e MYSQL\_ROOT\_PASSWORD=password 경우 -e는 환경변수를 의미하고요. 해당 환경변, " MYSQL\_ROOT\_PASSWORD " 에 password라는 값을 기입했어요. 추후에 인증할때 사용되요. 

```text
docker ps 
```

0.0.0.0:9876-&gt;3306/tcp 라는 부분이 나온다면 본인의 9876포트가 MySQL의 기본포트인 3306과 잘 연결된걸 확인한거에요.



### exec 명령어 이용 

> docker exec -it 컨테이너ID /bin/bash

```text
root@ip-172-31-35-20:/# docker exec -it 9ec /bin/bash
root@9ecd9942b0ee:/#
```

bash 명령을 실행해서 해당 컨테이너에 접속한것과 같은 효과를 만들어 내볼게요. 

root@9ecd9942b0ee:/\# 이렇게 바뀐 부분은 bash 상태로 바뀐걸 의미해요. 

### MySQL 접속 

 이어서 MySQL에 접속해 볼텐데요. 

```text
root@9ecd9942b0ee:/# mysql -u root -p
Enter password:
```

* -u : user
* -p : password 

앞서 비밀번호는 환경변수에 기입한 비밀번호를 입력할게요.   
그럼 아래와 같이 Welcome이라는 인사말과 함께 마지막 부분에 mysql&gt; 이라는 부분 역시 확인 될거에요. 성공! 

> Welcome to the MySQL monitor. Commands end with ; or \g. Your MySQL connection id is 2 Server version: 5.6.48 MySQL Community Server \(GPL\)
>
> Copyright \(c\) 2000, 2020, Oracle and/or its affiliates. All rights reserved.
>
> Oracle is a registered trademark of Oracle Corporation and/or its affiliates. Other names may be trademarks of their respective owners.
>
> Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
>
> mysql&gt;

### DB생성 

데이터 베이스를 생성해볼게요. 

```text
mysql> create database test;
Query OK, 1 row affected (0.00 sec)
```

데이터 베이스 목록을 확인해보면 아래와 같이 test 부분이 보이조?  
exit 명령어로 mysql bash 모드에서 나가주세요. 

```text
mysql> show databases; 
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| test               |
+--------------------+
4 rows in set (0.01 sec)
mysql> exit
```

### 컨테이너 내부 MySQL 접속 

우선 도커 컨테이너의 IP 주소를 확인해 볼게요. 

```text
docker inspect 컨테이너ID or 컨테이너
```

 쭉 아래에서 조금 올라거서 보면 IPAddress를 확인할 수 있어요.

> ```text
>         생략 
>         "SandboxKey": "/var/run/docker/netns/fd5e90569bba",
>         "SecondaryIPAddresses": null,
>         "SecondaryIPv6Addresses": null,
>         "EndpointID": "0f071711f82bcee7404c0fdfbb64b34e8c67eabdecc72df3ca65130072798325",
>         "Gateway": "172.17.0.1",
>         "GlobalIPv6Address": "",
>         "GlobalIPv6PrefixLen": 0,
>         "IPAddress": "172.17.0.2",
>         "IPPrefixLen": 16,
>         "IPv6Gateway": "",
>         "MacAddress": "02:42:ac:11:00:02",
>         "Networks": {
>             "bridge": {
>                 "IPAMConfig": null,
>                 "Links": null,
>                 "Aliases": null,
>                 "NetworkID": "b1e6fbe9a02391cbf00c718247e85c6c8331f377e01f6fa80b4f150fe2aeccf0",
>                 "EndpointID": "0f071711f82bcee7404c0fdfbb64b34e8c67eabdecc72df3ca65130072798325",
>                 "Gateway": "172.17.0.1",
>                 "IPAddress": "172.17.0.2",
>                 "IPPrefixLen": 16,
>                 "IPv6Gateway": "",
>                 "GlobalIPv6Address": "",
>                 "GlobalIPv6PrefixLen": 0,
>                 "MacAddress": "02:42:ac:11:00:02",
>                 "DriverOpts": null
> ```

이번엔 해당 IP주소로 접속해볼게요. 

**그 전에 AWS EC2에 MySQL 설치를 해주셔야해요. 아래 명령어로 mysql을 설치후 진행하면 되요.** 

```text
sudo apt install mysql-client-core-5.7
```

ㅡ

```text
mysql -u root -p --host 172.17.0.2 --port 3306
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 3
Server version: 5.6.48 MySQL Community Server (GPL)

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statemen

mysql> 
```

 비밀번호까지 입력하면 성공적으로 접속한걸 확인 할 수 있어요. 

```text
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| test               |
+--------------------+
4 rows in set (0.01 sec)

mysql> 
```

 이전 시간에 만든 테스트 데이터베이스까지 확인 할 수 있네요. 

####  다른 방법으로 Container내부에서 MySQL 접속하기 

```text
mysql -u root -p --host 127.0.0.1 --port 9876
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 4
Server version: 5.6.48 MySQL Community Server (GPL)

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```

문제없이 잘 접속 된걸 확인 할 수 있어요. 



####  하지만 알아 두어야 할 점이 일반적으로 쉽게 삭제 될 수 있는 도커 컨테이너를 MySQL DB로 이용하지는 않아요. 일반적으로 고객 데이터를 영구적으로 기록해둬야하는데 일시적인 컨테이너 공간 이용은 매우 위험한 상황을 초래하조.

#### 일반적으로 AWS RDS 의 DB기능을 많이 이용해요. 어쨋든 AWS RDS는 추후에 언급할게요. 

관리자 역할을 하는 유저를 만들어 볼게요. 

MySQL 유저 생성 및 권한 부여 

```text
create user 'test'@'%' identified by 'password';
```

####  생성된 유저에게 권한 부여 

```text
grant all privileges on *.* to 'test'@'%';
fluh privileges;
exit
docker restart 컨테이너ID 
```

 외부에서 도커 컨테이너에 접속 할 수 있도록 9876 포트를 열어줄수 있도록 인바운드 규칙 편집을 AWS EC2에서 하도록 할게요. 

![](../../.gitbook/assets/image%20%28203%29.png)

#### 외부에서 MySQL에 접속 

 하이디SQL에서 접속해볼거에요. 

1. Docker Test로 세션 이름을 지어볼게요. 
2. EC2 서버의 아이피를 입력하세요. 
3. 아까 mysql에서 create user 명령어로 test입력했조?
4. 비밀번호 역시 이전 mysql의 계정 만들때 사용했던 password\(혹은 본인이 입력했던\)를 입력하세요. 
5. 포트는 우리가 열어둔 9876포트를 입력해주세요. 

![](../../.gitbook/assets/image%20%28207%29.png)

자! 그럼 아래와 같이 화면이 나타나요. 

![](../../.gitbook/assets/image%20%28208%29.png)



 **요약:  이번 시간은 컨테이너를 이용해 MySQL서버를 이용해봤어요.**

