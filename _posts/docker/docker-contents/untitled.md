---
description: 도커 이미지 빌드하기
---

# Builing A Docker Image

## 이미지 빌드 

```text
import socket 

with socket.socket() as s : 
    s.bind('0.0.0.0', 12345))
    s.listen()
    print('server is started')
    conn, addr = s.accept()
    # conn 클라이언트와 통신할 소켓 
    # addr 클라이언트의 정보가 들어있음
    with conn: 
        print('Connected by', addr) 
        while True:
             data = conn.recv(1024)
             if not data: break
             conn.sendall(data) 
```

3번째 줄에서 socket.socket\(\)로 소켓을 열게되요. s.bind\(\)메소드의 12345포트를 이용할거고요. 그리고 클라이언트에게 접속하게 되면 누구에게 접속 되었는 7번째줄의 addr에 저장되게되요.  이후 12번째 줄에서 while문을 통해서 loop하게되는데요. 

반복되는 내용은 conn.recv\(1024\)에 1024바이트 인자값을 받아서 data에 저장해요. 그리고 14번째줄의 if not data: break 구문이 보이는데, data변수가 0이면 break하고 만약 0이아니면 계속 while문이 돌가가게 되는 구조에요. 그리고 conn.sendall\(data\)는 인자로 받은 data내용을 다시 돌려주는 구조에요. 

아래 nc는 socket이 통신 가능한 상태인지 확인해 보는 프로그램이에요.   
즉, 포트까지 접속해서 데이터를 보내는 프로그램이에요.

```text
nc 127.0.0.1 12345
```

##  도커 파일 생성 

별도의 디렉토리를 생성하고 dockfile과 위에서 생성한 python파일을 새 디렉토리에 배치해요.  

아래 명령문들은 도커 파일을 이미지 빌드화 하는 과정이에요.   
그러기 위해선 우선 별도의 디렉토리, my\_first\_project를 만들어요. 그리고 기존에 생성했던 test\_server.py 파일을 ./my\_first\_project/디렉토리로 이동시켜줘요. 이후 생성했던 디렉토리로 cd명령어를 이용해서 이동하고요. gedit dockerfile을 이미지 빌드화 명령어를 실행시켜줘요.  

####  참고로 my\_first\_project 디렉토리에는 오직 dockderfile과 test\_server.py파일 2개만 있어줘야해요. 아니면 쓰레기 파일들이 같이 끼게되요.\(별도의 디렉토리를 만든이유가 관련없는 파일들과 분리시키기 위함이에요.\) 

{% tabs %}
{% tab title="도커파일생성 명령어" %}
```text
mkdir my_first_project 
mv test_server.py ./my_first_project/
cd my_first_project/
gedit dockerfile 
```
{% endtab %}
{% endtabs %}

{% code title="dockerfile" %}
```text
from python:3.7
run mkdir /echo 
copy test_server.py /echo

cmd ['python', '/echo/test_server.py']

```
{% endcode %}

도커 파일을 살펴보면 첫번째에 python:3.7이 있는데 python이 이미지 이름이에요. 그리고 :\(콜론\)뒤의 3.7은 버전이름이조?!  
2번째 run 명령어는 python:3.7이미지를 이용해서 echo라는 디렉토리를 만들어라'라는 의미에요. 

3번째 줄에서 copy는 test\_server.py 파일을 echo라는 폴더 안으로 기존의 파일을 복사해서 붙여 넣기 하겠다라는 의미에요.  그리고 CMD라는 명령어도 보이는데요. 

여기서 CMD와 RUN의 차이점을 살펴보면요.   
**RUN명령어**는 **이미지를 빌드할 때** 실행되고요.   
**CMD명령어**는 **컨테이너가 실행될 때** 사용되는 명령어에요.   
결국 사용 시점의 차이가 다르다는 말이에요. 

###  빌드 후 테스트 

```text
ls 
dockerfile test_server.py 

docker build -t echo_test .
docker images
docker run -d -p 12345:12345 --name echo_test echo_test
```



 





