# \[부록\]Ubuntu에 Docker install 설치

 우분투에 도커를 설치하는 방법이 여러가지 있었네요.   
저는 그것도 모르고 그냥 설치했는데 다른 설치 방법도 알아볼게요.   


### **첫째, 자동설치 스크립트** 

```text
$ curl -s https://get.docker.com | sudo sh 
(또는) 
$ sudo wget -q0- https://get.docker.com | sh 
```

curl은 data transfer tool이에요 . 옵션은 -s가 붙어 있는데, 정숙 모드로 진행 내역이나 메시지등을 출력하지 않아요. 

  [Wget](http://www.incodom.kr/Linux/%EA%B8%B0%EB%B3%B8%EB%AA%85%EB%A0%B9%EC%96%B4/wget)의 약어로 웹 상의 파일을 다운로드 받을 때 사용하는 명령어에요.   
-q0-은 의미를 잘 모르겠네요. ㅠ.ㅠ 알게되면 다시 올릴게요.   


요약하자면  우분투에서 한번에 Docker를 설치 할 수 있게 스크립트를 구성하여 웹에 업로드한 페이지가 있습니다. [https://get.docker.com](https://get.docker.com/) 이라는 페이지에 우분투 사용자를 위한 설치 스크립트가 제공되어 해당 스크립트를 접근하여 바로 도커를 설치할 수 있습니다.  


---

### 둘째, 우분투 패키지 

```text
$ sudo apt-get update
$ sudo apt-get install docker.io
$ sudo ln -sf /usr/bin/docker.io /usr/local/bin/docker
```

ln은 link의 약어인데요. 연결 파일을 생성해줄때 사용해요.   
윈도우의 '바로가기'파일을 만들어준다는 개념만 알고가심되요. 하지만 완전히 일치된 개념은 아니에요.   
-sh 옵션은 심볼릭링크파일을 생성하는데 기존에 동일한 파일 이름이 존재하면 대상파일을 지우고 새로 생성하게 되요. 

즉, 마지막 줄 /usr/bin/docker.io 파일을 docker 라는 바이너리로 링크해서 사용하는 명령어에요.   
  
위 명령을 실행하면 도커 설치가 진행되며, 설치가 완료되면 다음 명령을 통해 도커 설치를 확인할 수 있어.

자세한 내용은 제 블로그의 'Linux Commnad' 카테고리에서 확인해주세요. 

```text
$ docker -v
Docker version 17.03.1-ce, build c6d412e
```

installed complete 되면 docker라는 유저 그룹이 만들어 져요! 

```text
$ cat /etc/group | grep docker
docker:x:999:
```

docker 그룹에 사용자가 추가되지 않았어요. 초기 설정으로 root유저이외에 docker를 사용할수 없어요. 일반 사용자에게 docker 사용 권한을 주고 싶으면 아래 명령어를 수행하면 된다고 해요. 



###  별첨 sudo 없이 사용 

```text
 sudo usermod -a -G docker <USER_ID>

$ sudo usermod -aG docker osori
```

```text
(방법1)
sudo systemctl reboot # 말그대로 시스템 다시 리부팅합니다.
(방법2)
sudo -su [현재사용자]
(방법3)
sudo service docker restart # 안될 확률이 높아요.
(방법4)
로그아웃(서버 나갔다가 다시 로그인 하세요.)
이후 sudo 명령어 없이 docker images, docker ps, docker ps -a 명령어 입력후 확인
```

기본적으로 docker를 수행하기 위해서 sudo를 붙여 실행하면 됩니다.

