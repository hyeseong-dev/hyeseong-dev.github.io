# docker-compose

##  삭제 방법 

 도화지 상태에서 최신 버전과 매칭하기 위해서 일단 삭제 명령어를 실행합니다. 

```text
sudo apt remove docker-compose
```

## 설치 방법 

```text
sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

##  버전확인 

```text
sudo docker-compose -v
```

## docker-compose.yml 작성과 활용 

디렉토리를 만들고 docker-compose.yml 파일을 작성해볼게요.   
vi or nano 에디터로 만들면 노가다이니, jupyter notebook 이용하면 복붙하면 금방이겠조?  
  
파일 내용을 살펴보면, 워드프레스에서 사용할 MySQL와 워드프레스를 설치하고 MySQL 도커 컨테이너와 연결하게 되요. 

{% code title="docker-compose.yml" %}
```text
version: '3.3'
services:
   db:
     image: mysql:5.7
     volumes:
       - db_data:/var/lib/mysql
     ports:
       - "3306:3306"
     restart: always
     environment:
       MYSQL_ROOT_PASSWORD: somewordpress
       MYSQL_DATABASE: wordpress
       MYSQL_USER: wordpress
       MYSQL_PASSWORD: wordpress
   wordpress:
     depends_on:
       - db
     image: wordpress:latest
     ports:
       - "8000:80"
     restart: always
     environment:
       WORDPRESS_DB_HOST: db:3306
       WORDPRESS_DB_USER: wordpress
       WORDPRESS_DB_PASSWORD: wordpress
       WORDPRESS_DB_NAME: wordpress
volumes:
    db_data: {}
```
{% endcode %}

## Docker-compose 실행 

```text
sudo docker-compose up -d
docker ps
```

위 명령어를 실행하면 아래와 같이 컨테이너 2개가 잘 생성 된걸 확인 할수 있어요.

![](../.gitbook/assets/image%20%28231%29.png)

##  WORDPRESS 사용  

### 8000번 포트로 접속

![install img](https://www.popit.kr/wp-content/uploads/2020/01/image-20200114-214105-600x393.png)

위와 같이 인스톨 화면이 잘 나타나와. 어렵지 않아요. 한글 설정하시고, 처음 이용하시는 분들이라면 가입과정을 거치면 되요.   


###  설정 

1.   ![image-20200114-214259](https://www.popit.kr/wp-content/uploads/2020/01/image-20200114-214259-600x395.png)

2.   ![image-20200120-215147](https://www.popit.kr/wp-content/uploads/2020/01/image-20200120-215147-1024x674.png)

3.   ![image-20200120-215231](https://www.popit.kr/wp-content/uploads/2020/01/image-20200120-215231-1024x674.png)

4.   ![image-20200120-220219](https://www.popit.kr/wp-content/uploads/2020/01/image-20200120-220219-1024x674.png)

## 외부 공개 

워드프레스는 호스트 서버의 8000 포트를 사용하고 있다고 하네요. 웹 브라우저는 HTTP 프로토콜을 사용하는 경우 80포트로 접속하게되. 따라서 8000 포트를  80 포트로 변경이 필요하.

워드프레스 도커 이미지에는 워드프레스 전용 웹서버가 포함되게 되요. 하지만 여러 서비스를 사용하기 위해서는 호스트 서버의 요청을 받아 분기 시켜주는 웹서버가 앞단에 하나 더 필요하다. [NGINX 웹서버](https://www.nginx.com/)를 도커가 아닌 호스트 서버에 설치하여 80 포트에 연결하고 서비스별로 라우팅 시키는 방법 찾아 볼게요.

![&#xD750;&#xB984;&#xB3C4;](https://www.popit.kr/wp-content/uploads/2020/01/image-20200130-011513-1024x707.png)

### Ngnix 설치 

```text
sudo apt install nginx-core
```

### Ngnix 실행 

```text
sudo service nginx start
```

### nginx 설정 파일 변경 

설정 파일 이름은 nginx.conf이에요. 확장자 이름이 conf인데요.   
일반적으로 conf는 configure, configuration의 설정이라는 의미의 줄임말이에요.   
설정파일에 들어가서 작업에 들어갈거에요.\(vi, nano, jupyter-notebook으로 편집\)

```text
sudo find / -name nginx.conf 
/etc/nginx/nginx.conf
```

```text
server {
   listen       80;
   // ...
   location / {
                proxy_pass http://127.0.0.1:8000;
                proxy_set_header Host $http_host;
                proxy_set_header X-Forwarded-Host $http_host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
   }
}
```

