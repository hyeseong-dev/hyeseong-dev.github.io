# SCP사용법

## \[Linux\] scp를 이용해 로컬과 원격에 파일 전송하기

> 업데이트\(2018.03.16\) : 옵션 및 설명 추가

> Linux 기반 운영체제에서 scp 명령어를 사용해서 로컬-원격 사이에 파일을 주고 받아보자.

### 환경 및 선수조건 <a id="&#xD658;&#xACBD;-&#xBC0F;-&#xC120;&#xC218;&#xC870;&#xAC74;"></a>

* Linux
* Bash shell\(/bin/bash\)

### scp 명령어 <a id="scp-&#xBA85;&#xB839;&#xC5B4;"></a>

#### 기본 <a id="&#xAE30;&#xBCF8;"></a>

* `scp` : secure copy \(remote file copy program\)의 줄임말로 `ssh`를 이용해 네트워크로 연결된 호스트간에 파일을 주고 받는 명령어입니다.
* `로컬 -> 리모트 (보내기)`, `리모트 -> 로컬 (가져오기)`와 `리모트 -> 리모트 (다른 호스트끼리 전송)` 로 복사가 모두 가능합니다.
* `ssh`를 이용하기 때문에 password를 입력하거나 ssh 키파일과 같은 identity file을 이용해 파일 송수신이 가능합니다.

#### 기본 사용 문법 <a id="&#xAE30;&#xBCF8;-&#xC0AC;&#xC6A9;-&#xBB38;&#xBC95;"></a>

* manual page에 있는 자료

```text
scp [options ...] [source] [target]
```

* 기본 형태

```text
# Local -> Remote
scp 목적파일명(경로) 유저명@IP주소:목적디렉토리
```

```text
# Remote -> Local
scp 유저명@IP주소:파일디렉토리 목적파일명(경로)
```

```text
# Remote(source) -> Remote(target)
scp 유저명@IP주소:파일디렉토리 유저명@IP주소:파일디렉토리
```

#### 옵션 <a id="&#xC635;&#xC158;"></a>

* `-r` : 재귀적으로 모든 폴더들을 복사합니다. 폴더를 복사할 때 사용하는 옵션으로 이때 전송하고자 하는 대상은 폴더로 지정하면 됩니다. 아래에 예제를 참고하시면 됩니다. symbolic link가 있는 경우에는 target에 symbolic link를 생성하지 않고 symbolic link가 가리키는 파일 혹은 폴더를 복사합니다.
* `-P` : ssh 포트를 지정하는 옵션
* `-i` : ssh 키파일과 같은 identity file의 경로를 지정하는 옵션
* `-v` : verbose 모드로 상세내용을 보며 디버깅을 할 때 사용합니다.
* `-p` : 파일의 수정 시간과 권한을 유지합니다.

### 예제 <a id="&#xC608;&#xC81C;"></a>

#### 로컬 -&gt; 리모트 <a id="&#xB85C;&#xCEEC;---&#xB9AC;&#xBAA8;&#xD2B8;"></a>

* 패스워드 사용하는 경우

```text
scp ~/test.txt twpower@[IP주소]:/home/twpower
```

* `-i` 옵션
* identity file을 지정해서 사용할 때

```text
scp -i ~/.ssh/twpower-private-server ~/test.txt twpower@[IP주소]:/home/twpower
```

* `-r` 옵션
* 폴더를 복사하는 경우

```text
scp -r ~/test_folder/ twpower@[IP주소]:/home/twpower
```

* `-P` 옵션

```text
scp -P 22 ~/test.txt twpower@[IP주소]:/home/twpower
```

#### 리모트 -&gt; 로컬 <a id="&#xB9AC;&#xBAA8;&#xD2B8;---&#xB85C;&#xCEEC;"></a>

* 패스워드 사용하는 경우

```text
scp twpower@[IP주소]:/home/twpower/test.txt /Users/taewoo
```

* `-i` 옵션
* identity file을 지정해서 사용할 때

```text
scp -i ~/.ssh/twpower-private-server twpower@[IP주소]:/home/twpower/test.txt /Users/taewoo
```

* `-r` 옵션
* 폴더를 복사하는 경우

```text
scp -r twpower@[IP주소]:/home/twpower/test_folder /Users/taewoo
```

* `-P` 옵션

```text
scp -P 22 twpower@[IP주소]:/home/twpower/test.txt /Users/taewoo
```

### 참고자료 <a id="&#xCC38;&#xACE0;&#xC790;&#xB8CC;"></a>

* [https://linux.die.net/man/1/scp](https://linux.die.net/man/1/scp)
* [https://zetawiki.com/wiki/%EB%A6%AC%EB%88%85%EC%8A%A4_scp_%EC%82%AC%EC%9A%A9%EB%B2%95](https://zetawiki.com/wiki/%EB%A6%AC%EB%88%85%EC%8A%A4_scp_%EC%82%AC%EC%9A%A9%EB%B2%95)

[OS](https://twpower.github.io/tags#OS)[LINUX](https://twpower.github.io/tags#Linux)[SCP](https://twpower.github.io/tags#scp)

