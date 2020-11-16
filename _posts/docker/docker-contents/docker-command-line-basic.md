---
description: 기본 명령어
---

# Docker Command Line Basic

###  Docker workflow 

![&#xB3C4;&#xCEE4; &#xBA85;&#xB839; &#xC21C;&#xC11C;&#xB3C4;](../../.gitbook/assets/image%20%2887%29.png)

 docker workflow를 알아볼게요.  

A. 레지스트리를 원하는 이미지를 pull하게 되요.   
B. image에서 PUSH하게 되면 REGISTRY에 업로드하게 되는데요. \(반드시 권한설정을해주세요. \)  
C. PULLING한 IMAGE를 실행하기 위해선\(지금은STATIC 사용불가\) CONTAINER로 만들어야해요.   
D. CONTAINER 생성은 CREATE를 명령어를 통해 가능해요.  
F. CONTAINER \_\_실행\_\_\(메모리에 띄워 동작하게 만듬\)은 START명령어를 통해서 가능해요.   
G. **PULL-&gt; CREATE -&gt; START** 일련의 명령어를 **RUN이라는 명령어로 한방에** 가능해요. 

\_\_참고\_\_ **PULL된 IMAGE는 사실 RUN명령어를 이용하지 않아요.**  **대신 CREATE와 START**만 다시하게 되요.  
주의해서 봐야할 부분이 RUN 명령어는 CREATE START를 일련에 포함하는 과정이므로 **RUN명령어를 남발**해서 사용하면\(동일  APP을 여러번\) 컨테이너를 계속만들게되어 **자원낭비**가 발생해요. 

> 왠만해선 CREATE, START명령어를 각각 실행해주세요. RUN은 **가장 처음** CONTAINER를 CREATE + START 명령어를 한방에 하고 싶은 경우에만 해주세요.

H. 실행중인 컨테이너를 정**지하려할때는 STOP명령어를 사용하세요.   
I. CONTAINER를** 삭제하고싶은경우 RM을 쓰세요.   
 CONTAINER를  지운다고 IMAGE가 지워지지 않아요. 이미지를 지우기 위해선   
J. RIM를 사용해주세요. 

#### 1.  도커 이미지 다운로드와 삭제 

```text
sudo docker pull consol/tomcat-7.0
sudo docker rmi consol/tomcat-7.0 
```

#### 2. 톰캣 container 만들기 

```text
sudo docker run -d --name tc tomcat # 톰캣 생성및 실행 
# run 명령어를 지속적으로 사용할 경우 불필요하게 컨테이너를 사용하여 불필요한 자원을 생성시켜요.
```

-d 옵션은 백그라운드에서 run명령어를 실행하겠다는 표현이에요. --name을 같이 쓰게 되면 컨테이너의 이름을 지어주게 되요. 

---

### 컨테이너 실행 

> docker run\[OPTIONS\] IMAGE\[:TAG\|@DIGEST\] \[COMMAND\] \[ARG...\]

> | 옵션 | 설명 |
> | :--- | :--- |
> | -d | detached mode 흔히 말하는 백그라운드 모드 |
> | -p | 호스트와 컨테이너의 포트를 연결 \(포워딩\) |
> | -v | 호스트와 컨테이너의 디렉토리를 연결 \(마운트\) |
> | -e | 컨테이너 내에서 사용할 환경변수 설정 |
> | –name | 컨테이너 이름 설정 |
> | –rm | 프로세스 종료시 컨테이너 자동 제거 |
> | -it | -i와 -t를 동시에 사용한 것으로 터미널 입력을 위한 옵션 |
> | –link | 컨테이너 연결 \[컨테이너명:별칭\] |





--

#### 3. 현재 실행 중인 컨테이너 정보를 확인

 ps 옵션은 process의 약자인데요. 실행중인 프로세스만 확인시켜줘요. 

ID, IMAGE, COMMAND CREATED STATUS 정보 출

```text
sudo docker ps #톰캣 컨테이너 확인 

CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
f6e513b399a6        tomcat              "catalina.sh run"   27 seconds ago      Up 26 seconds       8080/tcp            tc 
```

#### 3.1 모든 컨테이너 확인 

```text
sudo docker ps -a # 모든 컨테이너의 정보를 확인
```

**프로세스가 실행중이지 않은경우** :   
-a 옵션은 all의 약자라는걸 직관적으로 알수 있어요. 

![ps &#xBA85;&#xB839;&#xC5B4; -a&#xC635;&#xC158; &#xC720;&#xBB34;](../../.gitbook/assets/image%20%28102%29.png)

 실행중인 프로세스의 경우는 정보가 출력되지만 실행중이지 않은 경우  위 사진 처럼 파란색 부분에 컬럼명 빼고는 정보가 출력되지 않아요. 이런경우 그냥 모든 컨테이너를 확인하고 싶으니 빨간색처럼 나오게 하기 위해서 옵션 -a를 넣어줘요. 



**프로세스\(컨테이너\)가 실행중인 경우 :** 

![](../../.gitbook/assets/image%20%2891%29.png)

nginx container가 실행중인 경우 UP으로 나타난걸 알수 있어요. 

#### 

####  nginx 실행해보기: 

 웹브라우저 주소창에 127.0.0.1을 실행해보면 아래와 같이 잘 실행된걸 볼 수 있어요. 

![](../../.gitbook/assets/image%20%2892%29.png)



#### ngnix container 추가 생성하기 : 

![&#xCEE8;&#xD14C;&#xC774;&#xB108; &#xC0DD;&#xC131;&#xC2DC; &#xC774;&#xB984;&#xACFC; &#xD3EC;&#xD2B8; &#xC8FC;&#xC18C;&#xB294; &#xB458;&#xB2E4; &#xAE30;&#xC874;&#xACFC; &#xB2EC;&#xB77C;&#xC57C;&#xD568;](../../.gitbook/assets/image%20%28138%29.png)

맨 위 docker run -d -p 80:80 --name **nx** nginx 의 경우 nx라는 이름을 이미 쓰고 있어서 오류가 떳어요.   
그래서 다음 코드에는 run -d -p 80:80 --name **nx2** nginx 라고 이름을 nx2라고 바꾸었지만 오류가 떳조?   
두번쨰 오류 원인은 포트가 기존 80:80 포트가 현재 할당되어 있기 때문에 그렇습니다.   
이를 해결하기 위해   
80:80 --&gt; 88:80 으로 바꾸어 주면 드디어 문제없이 컨테이너가 생성되요.   
  
위의 run 명령문을 왜 보여주냐고요? **메모리가 어떻게 낭비되는지 보여주려고 그렇습니다.**   
아래를 봐주세요. 

![&#xBA54;&#xBAA8;&#xB9AC;&#xAC00; &#xB0AD;&#xBE44;&#xB41C; &#xBAA8;&#xC2B5; ](../../.gitbook/assets/image%20%28157%29.png)

 일반적인 경우에 메모리를 굳이 낭비하면서 3개의 컨테이너를 사용해서 실행 시킬 필요가 없겠지요?

#### 4. 컨테이너 시작/재시작/정지/확인 

```text
docker start <container ID 또는 name>
docker restart <container ID 또는 name>
docker stop <container ID 또는 name>
sudo docker ps -a # 모든 컨테이너 확인 
```

![&#xCEE8;&#xD14C;&#xC774;&#xB108; &#xC815;&#xBCF4;](../../.gitbook/assets/image%20%28112%29.png)

#### 5. 컨테이너 중지 

```text
sudo docker stop f6e513b399a6 # 컨테이너 아이디를 stop 키워드 뒤에 넣어주세요. 
f6e513b399a6
```

#### 6. 컨테이너 삭제 

```text
sudo docker rm 
```

컨테이너가 실행중이라면 stop명령어를 써야 삭제 가능해요.    
컨테이너 삭제는 rm 이미지 삭제는 rmi 에요. 

```text
***
컨테이너가 떠있든 말든 그냥 이미지는 물론이거니와 다 날려버리고 싶은 경우 
docker rmi -f 이미지
```

###  이미지와 레이어

 레이어에 대해 배워 볼게요. 

![](../../.gitbook/assets/image%20%2867%29.png)

 왼쪽 오른쪽 구분이 되어있어요. 

왼쪽 부분:  이미지 A~B는 같은 공간에 있고 이미지 C~E 역시 별도의 공간에 함께 있어요.   
왼쪽에서 이미지A를 지운다고  해도 이미지B가 레이어 A,B,C를 사용해서 지워지지 않아요. 

오른쪽 부분: 이미 존재하는 레이어 A,B는 새로 다운 받을 필요가 없어요. 

#### 1. 이미지 정보 확인하기 

```text
sudo docker pull nginx
sudo docker inspect nginx
```

\_\_container 생성\_\_ 

> docker create -p 80:80 --name nx nginx
>
> container를 생성시 80번  포트를 이용해서 만들어져요. 이때 --name옵션을 이용해서 nx라는 이름을 지정해 줄수 있어요. 마지막 nginx는 해당 이미지를 기준으로 가공해준다는 의미에요.

#### 2. Image repository  path 확

```text
sudo docker info 
sudo -i 
cd /var/lib/docker/overlay2
```

#### 3. Layer repository path 확인 

```text
root@server1-VirtualBox:/var/lib/docker/overlay2# ls
0cc29ea5605872d9c8291673064e85b07160203fbf04b34eeeed899731361960 # 레이어 변경 사항 저장
615767e7221dbc99b8e441e35a88df5d74c911f2674ceaa28001388535e95be2 # 레이어 변경 사항 저장
9f3bb671f38d7f61f661af369d420cdedb195e4d623bdb6ba8e3b045f72e8d69 # 레이어 변경 사항 저장
l # 원본 레이어 저장
```

#### 4. Docker size 확인

```text
du -sh /var/lib/docker/ # docker 크기를 볼 수 있어요. 
2.0G	/var/lib/docker/

du -sh /var/lib/docker/image/ # 도커 이미지에 대한 정보 저장 디렉토리
2.7M	/var/lib/docker/image/

du -sh /var/lib/docker/overlay2/ # 도커 이미지의 파일 시스템이 사용되는 실제 디렉토리
2.0G	/var/lib/docker/overlay2/

du -sh /var/lib/docker/containers/ # 도커 컨테이너 정보 저장 디렉토리
136K	/var/lib/docker/containers/
```

#### 4. Docker 용량 

---

 여기서 \_\_du\_\_ 명령어는 \_\_disk usage\_\_의 약자인데요. 

> 현재 디렉토리 혹은 지정한 디렉토리의 사용량을 확인할때 사용해요.   
> du \[옵션\]  \# 문법은 왼쪽과 같아요.

결국 디스크 용량에 관한 정보를 어떻게 보여줄지 옵션을 정해서 보여줄건데요. 

-sh는 저의 추측이지만 옵션의 조합처럼 보여요.  --summarize  --humanreadable을 더해서   
용량표기를 인간이 읽을수 있게 간단하게 출력해준다는 의미의 결합된 옵션이라고 생각해봅니다.  


_\_\_\* 옵션_\_\_ 



<table>
  <thead>
    <tr>
      <th style="text-align:left">&#xC635;&#xC158;</th>
      <th style="text-align:left">Long&#xC635;&#xC158;</th>
      <th style="text-align:left">&#xC124;&#xBA85;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">-a</td>
      <td style="text-align:left">--all</td>
      <td style="text-align:left">&#xD604;&#xC7AC; &#xB514;&#xB809;&#xD1A0;&#xB9AC; &#xC544;&#xB798;&#xC758;
        &#xBAA8;&#xB4E0; &#xD30C;&#xC77C;&#xACFC; &#xB514;&#xB809;&#xD1A0;&#xB9AC;&#xC758;
        &#xC0AC;&#xC6A9; &#xC815;&#xBCF4;&#xB97C; &#xCD9C;&#xB825;</td>
    </tr>
    <tr>
      <td style="text-align:left">-B</td>
      <td style="text-align:left">--block-size=<b>SIZE</b>
      </td>
      <td style="text-align:left">&#xC9C0;&#xC815;&#xD55C; &#xBE14;&#xB85D; &#xD06C;&#xAE30;(<b>SIZE</b>)
        &#xB2E8;&#xC704;&#xB85C; &#xC6A9;&#xB7C9;&#xC744; &#xCD9C;&#xB825;</td>
    </tr>
    <tr>
      <td style="text-align:left">-b</td>
      <td style="text-align:left">--bytes</td>
      <td style="text-align:left">&#xBC14;&#xC774;&#xD2B8; &#xB2E8;&#xC704;&#xB85C; &#xCD9C;&#xB825;</td>
    </tr>
    <tr>
      <td style="text-align:left">-c</td>
      <td style="text-align:left">--total</td>
      <td style="text-align:left">
        <p>&#xBAA8;&#xB4E0; &#xD30C;&#xC77C;&#xC758; &#xB514;&#xC2A4;&#xD06C; &#xC0AC;&#xC6A9;
          &#xC815;&#xBCF4;&#xB97C; &#xCD9C;&#xB825;&#xD558;&#xACE0;, &#xCD9C;&#xB825;&#xB41C;
          &#xAC83;&#xB4E4;&#xC758; &#xBAA8;&#xB4E0; &#xD569;&#xACC4;&#xB97C; &#xCD9C;&#xB825;</p>
        <p>(&#xBCF4;&#xD1B5; &#xD574;&#xB2F9; &#xACBD;&#xB85C;&#xAC00; &#xC5BC;&#xB9C8;&#xB9CC;&#xD07C;&#xC758;
          &#xC6A9;&#xB7C9;&#xC744; &#xCC28;&#xC9C0;&#xD558;&#xB294;&#xC9C0; &#xD655;&#xC778;&#xD560;&#xB54C;
          &#xC0AC;&#xC6A9;)</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">-D</td>
      <td style="text-align:left">--dereference-args</td>
      <td style="text-align:left">&#xC9C0;&#xC815;&#xD55C; &#xD30C;&#xC77C;&#xC758; &#xACBD;&#xB85C;&#xAC00;
        &#xC2EC;&#xBCFC;&#xB9AD; &#xB9C1;&#xD06C; &#xD30C;&#xC77C;&#xC774;&#xBA74;
        &#xC6D0;&#xBCF8;&#xC758; &#xAC12;&#xC744; &#xCD9C;&#xB825;</td>
    </tr>
    <tr>
      <td style="text-align:left">-h</td>
      <td style="text-align:left">--human-readable</td>
      <td style="text-align:left">&#xD30C;&#xC77C; &#xC6A9;&#xB7C9;&#xC744; &#xC0AC;&#xB78C;&#xC774; &#xBCF4;&#xAE30;
        &#xC26C;&#xC6B4; &#xD615;&#xD0DC;&#xB85C; &#xCD9C;&#xB825;</td>
    </tr>
    <tr>
      <td style="text-align:left">-H</td>
      <td style="text-align:left">--si</td>
      <td style="text-align:left">-h&#xC640; &#xBE44;&#xC2B7;&#xD558;&#xC9C0;&#xB9CC; 1,024 &#xB2E8;&#xC704;&#xC758;
        &#xBE44;&#xC728;&#xB85C; &#xCD9C;&#xB825;</td>
    </tr>
    <tr>
      <td style="text-align:left">-k</td>
      <td style="text-align:left"></td>
      <td style="text-align:left">&#xCD9C;&#xB825; &#xB2E8;&#xC704;&#xB97C; 1KB &#xD615;&#xD0DC;&#xB85C;
        &#xC9C0;&#xC815;</td>
    </tr>
    <tr>
      <td style="text-align:left">-l</td>
      <td style="text-align:left">--count-links</td>
      <td style="text-align:left">&#xD558;&#xB4DC; &#xB9C1;&#xD06C;&#xB418;&#xC5B4; &#xC788;&#xB294; &#xD30C;&#xC77C;&#xB3C4;
        &#xC788;&#xB294; &#xADF8;&#xB300;&#xB85C; &#xCE74;&#xC6B4;&#xD2B8;</td>
    </tr>
    <tr>
      <td style="text-align:left">-L</td>
      <td style="text-align:left">--dereference</td>
      <td style="text-align:left">&#xBAA8;&#xB4E0; &#xC2EC;&#xBCFC;&#xB9AD; &#xB9C1;&#xD06C;&#xB97C; &#xB530;&#xB984;</td>
    </tr>
    <tr>
      <td style="text-align:left">-S</td>
      <td style="text-align:left">--separate-dirs</td>
      <td style="text-align:left">&#xB514;&#xB809;&#xD1A0;&#xB9AC;&#xC758; &#xCD1D; &#xC0AC;&#xC6A9;&#xB7C9;&#xC744;
        &#xCD9C;&#xB825;&#xD560;&#xB54C; &#xD558;&#xC704; &#xB514;&#xB809;&#xD1A0;&#xB9AC;&#xC758;
        &#xC0AC;&#xC6A9;&#xB7C9;&#xC740; &#xC81C;&#xC678;</td>
    </tr>
    <tr>
      <td style="text-align:left">-s</td>
      <td style="text-align:left">--summarize</td>
      <td style="text-align:left">&#xAC04;&#xB2E8;&#xD558;&#xAC8C; &#xCD1D; &#xC0AC;&#xC6A9;&#xB7C9;&#xB9CC;
        &#xC694;&#xC57D;&#xD558;&#xC5EC; &#xCD9C;&#xB825;</td>
    </tr>
    <tr>
      <td style="text-align:left">-x</td>
      <td style="text-align:left">--one-file-system</td>
      <td style="text-align:left">&#xD604;&#xC7AC; &#xD30C;&#xC77C; &#xC2DC;&#xC2A4;&#xD15C;&#xC758; &#xD30C;&#xC77C;
        &#xC0AC;&#xC6A9;&#xB7C9;&#xB9CC;&#xC744; &#xCD9C;&#xB825;</td>
    </tr>
    <tr>
      <td style="text-align:left">-X <b>file</b>
      </td>
      <td style="text-align:left">--exclude-from=<b>file</b>
      </td>
      <td style="text-align:left">&#xC9C0;&#xC815;&#xD55C; &#xD30C;&#xC77C;(<b>file</b>)&#xACFC; &#xC77C;&#xCE58;&#xD558;&#xB294;
        &#xD30C;&#xC77C;&#xC740; &#xC81C;&#xC678;</td>
    </tr>
    <tr>
      <td style="text-align:left">--help</td>
      <td style="text-align:left"></td>
      <td style="text-align:left">du &#xBA85;&#xB839;&#xC5B4;&#xC758; &#xC0AC;&#xC6A9;&#xBC95; &#xCD9C;&#xB825;</td>
    </tr>
    <tr>
      <td style="text-align:left">--version</td>
      <td style="text-align:left"></td>
      <td style="text-align:left">du&#xC758; &#xBC84;&#xC804; &#xC815;&#xBCF4; &#xCD9C;&#xB825;</td>
    </tr>
  </tbody>
</table>

---



