# EC2 Jupyter로  서버관리

앞서서 우리는 아마존 EC2에서 우분투 리눅스 서버를 활용 봤습니다. 하지만 문제점이 발생했습니다.   
  
키페어로 매번 일일히 접근하는게 정말 번거로웠습니다.   
  
오늘은 이를 해결해볼게요.   
어떻게?! Jupyeter Notebook을 이용해 볼게요. 

참고로 우분투 리눅스 서버에는 python3가 설치되어 있어요. 그러니 주피터 사용에 문제가 없다라는거~  


\_\_주피터노트북\_\_  웹사이트를 웹서버에서 실행해\(외부에서 해당웹사이트로 접속하여\) 웹환경에서 서버관리를 가능하게 하는 tool입니다. 

### apt-get 업데이트 

이 파이썬 패키지파일인 주피터 노트북은 기본적으로 pip를 통해서 설치 가능해요.   
  
하지만 만약 그 pip라는 놈이 노쇠하고 old한 녀석이면 안되겠조? brand new한 녀석으로 가져와서 jupyter를 설치해야해요. 

> sudo apt-get update \# apt-get이라는 녀석을 update해줘야해요.

![sudo apt-get update ](../../../.gitbook/assets/image%20%2817%29.png)

 기본적으로 우분투 18.04 버전에는 파이썬 3까 설치 되어 있어요. 

![](../../../.gitbook/assets/image%20%2828%29.png)

###  파이썬 3 파이프 설치

* 목적: pip를 설치이후 jupyter notebook을 설치하기 위함 
* 방법: 아래 명령어를 입력하세요. 



* 첫번째, sudo apt-get install python3-pip 

![](../../../.gitbook/assets/image%20%2823%29.png)

* 두번째, sudo pip3 install notebook

![](../../../.gitbook/assets/image%20%288%29.png)

### 주피터 노트북 비밀번호 설정 

하는이유: 내가 만든 웹서버의 주피터노트북에 아무나 들어 오면 안되겠조?

#### 방법 :

> python3

파이썬3 터미널화면으로 전환되요. 

> from notebook.auth import passwd   
> passwd\(\)  
> \# 비밀번호 입력하라고 떠요.   
> Enter password:        \(비밀번호 입력해도 원래 화면변화 없어요\)     
> Veryfy password:   
> 'sha1: asdgjlajkldfjklajsdfklsjad;fjksdfjsdklfjdsklfjdsklfjsdklgh123u812'\(본인꺼 넣으세요\)  
> exit\(\)

![](../../../.gitbook/assets/image%20%2852%29.png)

> jupyter notebook --generate-config

주피터 노트북 환경설정 파일을 만드는게 위 명령어에요. 비밀번호 설정하려면 환경설정파일에서 하거든요. 

![](../../../.gitbook/assets/image%20%28170%29.png)

#### vi 에디터에서 환경설정 파일 수정 

> sudo jupyter noteboook --generate-config

![](../../../.gitbook/assets/image%20%28170%29.png)

위 명령어로 환경 설정 파일을 생성하게 되요. 그리고 생성된 환경설정파일의 경로를 아래줄에 출력해서 보여줘요. 

> .jupyter폴더에 jupyter\_notebook\_config.py라는 파일이 생성되었는데 열어 볼거에요.

> vi /root/.jupyter/jupyternotebook\_config.py

\(참고로 윈도우, 리눅스, 관라자 계정, 일반사용자 계정에 따라 디렉토리의 위치들이 제가 알려드리는것과 달라질수 있어요.\)

![](../../../.gitbook/assets/image%20%28126%29.png)

 밑에서 두번째 줄은 아까 본인이 주피터노트북의 비밀전호인거 기억하시요?   
그대로 복사 붙여넣기 해주세요.   
\(윈도우면 Ctrl C, Ctrl V / Linux면 Ctrl Insert, Shift Insert\)   
  
vi 에디터 사용법은\(현재 보이는 애플리케이션\)  
1. 입력  a를 입력해주세요.   
2. 나가는 방법은 esc --&gt; :wq \(키 3개 각각 눌러주세요.\)   


####  주피터 노트북 실행 

> jupyter notebook --allow-root

 아래 스샷, 밑에서 3번째줄 확인하면 본인 해당 IP주소가 8888 번 포트에 열린게 확인되요. 

![](../../../.gitbook/assets/image%20%28191%29.png)

###  AWS 방황벽 설정 - 8888번 포트 열어놓기 

 다시 AWS console management 웹페이지로 가주세요. 



![](../../../.gitbook/assets/image%20%28106%29.png)

보안그룹의 인바운드로 가볼게요. 

 아래와 같이 화면이 바뀔거에요. 

![&#xC778;&#xBC14;&#xC6B4;&#xB4DC; &#xADDC;&#xCE59;](../../../.gitbook/assets/image%20%2859%29.png)

![&#xC778;&#xBC14;&#xC6B4;&#xB4DC; &#xADDC;&#xCE59; &#xD3B8;&#xC9D1;](../../../.gitbook/assets/image%20%28144%29.png)

![&#xC0AC;&#xC6A9;&#xC790;&#xC9C0;&#xC815;TCP - TCP - 8888 - &#xC0AC;&#xC6A9;&#xC790;&#xC9C0;&#xC815; - 0.0.0.0/0](../../../.gitbook/assets/image%20%28196%29.png)

### 주피터 접속 

> 대시보드의 IP주소를 복사해주세요.

![&#xBCF8;&#xC778; IP &#xB300;&#xC2DC;&#xBCF4;&#xB4DC;&#xC5D0;&#xC11C; &#xD655;&#xC778; ](../../../.gitbook/assets/image%20%2881%29.png)

![&#xBE44;&#xBC00;&#xBC88;&#xD638;&#xB97C; &#xC785;&#xB825;&#xD574;&#xC8FC;&#xC138;&#xC694;. &#xD30C;&#xC774;&#xC36C;3 &#xD130;&#xBBF8;&#xB110;&#xC5D0;&#xC11C; &#xC124;&#xC815;&#xD588;&#xB358;&#xAC70; &#xC785;&#xB825;&#xD558;&#xBA74; &#xB418;&#xC694;. ](../../../.gitbook/assets/image%20%28194%29.png)

####  매번 이렇게 터미널 열고sudo jupyter-notebook --allow-root입력하고 웹브라우저에 IP주소:8888입력 해야하나요?

당연히 아닙니다. 터미널 환경으로 접속하지 않는 방법 알려드릴게요. 

### 주피터 터미널에서 소유권 포기 



> Ctrl + Z  
> bg  
> sudo jupyter-notebook --allow-root &   
> disown -h

![](../../../.gitbook/assets/image%20%2812%29.png)

bg는 background 모드로 주피터 노트북 터미널 환경에서 나오게되요.  
다음 sudo jupyter-notebook --allow-root &   
쥬피터 노트북을 실행하게 됩니다.   
**disown -h 소유권을 포기한다는 명령어에요.   
이제** 주피터 노트북이 항상 실행중인 상태가 되요. 

누구의 컴퓨터든\(서버만돌아가면\) 본인 IP주소:8888\(터미널에 명시된 포트번호\)를 넣으면 쥬피터 노트북은 실행가능한 상태가 되요.  

