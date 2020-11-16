---
description: 'VM, 리눅스, 도커, 아파치 톰캣 설치 및 실습'
---

# Docker Installation & Building

### 

### 1. 파일 다운로드

실습 파일 \(docker\)ubuntu-18.04.2-desktop-amd64.ova 다운로드

* [https://drive.google.com/open?id=1JMs6Iw1\_Ke7lz4g5tNqNE6ybA57CPVsD](https://drive.google.com/open?id=1JMs6Iw1_Ke7lz4g5tNqNE6ybA57CPVsD)
* ID:PW// server1 : test1234
* 관리자 전환: sudo -i

버츄얼 박스 다운로드

* [https://www.virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads)

\[출처:재즐보프\]\([https://www.notion.so/b67ed727aea4467cbc3226bb0c8e8336](https://www.notion.so/b67ed727aea4467cbc3226bb0c8e8336)\)

### Virtualbox에 리눅스 세팅하기

> 파일-&gt; 가상 시스템 가져오기 \# OVA파일을 가져오기를 실행해요.

전문가 모드를 열어주시면 

![&#xC804;&#xBB38;&#xAC00;&#xBAA8;&#xB4DC; ](../../../.gitbook/assets/image%20%2848%29.png)

## apt로 docker install 

바탕화면에 우클릭하면 터미널로 갈 수 있습니다. 

![&#xD130;&#xBBF8;&#xB110; &#xC5F4;&#xAE30; ](../../../.gitbook/assets/image%20%2877%29.png)

### 우분투 패키지로 도커 설치 

```text
> sudo -i # 관리자 권한으로 접
server1의 암호: <패스워드 입력 test1234>
> reboot # 재부팅해주세요. 
> sudo -i # 다시 관리자 권한으로 접속해주세요.
server1의 암호: <패스워드 입력 test1234>
> apt install docker.io

> sudo apt-get upgrade # apt 패키지를 업그레이드합니다.

```

### ~~도~~커 명령어로 검색 

```text
sudo docker search tomcat 
```

{% tabs %}
{% tab title="참고" %}
앞으로 sudo\(super user do or root user\) 명령어를 일반 user 계정에서는 매번 타이핑해야하는 번거로움이 있어요. 

이를 해결하기 위해서\(sudo 빼고 실행하려면\) 아래 명령어를 입력하고 엔터를 눌러주세요. 그리고 다시 로그아웃해주셔야 적용되요.

> sudo usermod -aG docker 사용자명

명령어 해설: usermod 사용자 계정 속성 변경을 위한CML이고요 거기 옵션이 -a \(add\) -G\(사용자 계정 2차 그룹의 GID 지정\) 
{% endtab %}
{% endtabs %}



### 

### docker에서 tomcat 다운로드 

```text
docker run -d -p 8080:8080 --name tc consol/tomcat-7.0 #생성 및 실행
# 방법1 위의 명령문
sudo docker pull tomcat # 다른방법 
```

### 로컬 도커 이미지 확인

```text
sudo docker image
```

 아래와 같이 

> REPOSITORY             TAG     IMAGE ID           CREATED      SIZE   
> consol/tomcat-7.0    latest  7c34bafd1150  4 years ago 601MB

## Docker Work Flow 

![&#xB3C4;&#xCEE4;&#xC758; &#xD750;&#xB984;&#xB3C4;](../../../.gitbook/assets/image%20%28185%29.png)

### 설치중 발생한 오류와 해결책  \(동인한 원인이라도 해결책이 다르거나 다양하다는점 명심하세요. \)

#### 1. Virtual로 리눅스 실행 :

* 원인: 사용방법 미숙지
* 해결법: 유투브 참고
* 참고 유투브 url: [https://www.notion.so/b67ed727aea4467cbc3226bb0c8e8336](https://www.notion.so/b67ed727aea4467cbc3226bb0c8e8336)



#### 2. 리눅스에서 Busybox로 빠져 나오지 못함 :

* 원인 1. 리눅스 사용중 강제 종료를 해버림.\(원인은 여러가지일 수 있어요.\)
* 해결책 : 구글링 url [https://qastack.kr/ubuntu/741109/ubuntu-15-10-busybox-built-in-shell-initramfs-on-every-boot](https://qastack.kr/ubuntu/741109/ubuntu-15-10-busybox-built-in-shell-initramfs-on-every-boot)
* 해결 코드 : 

  \`\`\`

  > \(initramfs\) exit 
  >
  > initramfs\) fsck /dev/sda1



