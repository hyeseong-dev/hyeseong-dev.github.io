# RUN

> **docker container run**   
> 혹은  
> **docker run**

2가지 명령어를 통해서 컨테이너의 생성 및 시작을 진행합니다. 

구문

> **docker container run \[옵션\] 이미지명\[:태그명\]\[인수\]**

\*\*\*\*

## run 명령어 옵션

옵션에 값을 설정할 때 =와 “는 생략해도 됩니다.

* -a, --attach=\[\]: 컨테이너에 표준 입력\(stdin\), 표준 출력\(stdout\), 표준 에러\(stderr\)를 연결합니다.
  * _--attach=”stdin”_
* --add-host=\[\]: 컨테이너의 _/etc/hosts_에 호스트 이름과 IP 주소를 추가합니다.
  * _--add-host=hello:192.168.0.10_
* -c, --cpu-shares=0: CPU 자원 분배 설정입니다. 설정의 기본 값은 1024이며 각 값은 상대적으로 적용됩니다.
  * _--cpu-shares=2048_처럼 설정하면 기본 값 보다 두 배 많은 CPU 자원을 할당합니다.
  * 이 설정 값은 리눅스 커널의 cgroups에서 사용됩니다.
* --cap-add=\[\]: 컨테이너에서 cgroups의 특정 Capability를 사용합니다. ALL을 지정하면 모든 Capability를 사용합니다.
  * _--cap-add=”MKNOD” --cap-add=”NET\_ADMIN”_처럼 설정합니다. 모든 Capability 목록은 다음 링크를 참조하기 바랍니다. [http://linux.die.net/man/7/capabilities](http://linux.die.net/man/7/capabilities)
* --cap-drop=\[\]: 컨테이너에서 cgroups의 특정 Capability를 제외합니다.
* --cidfile=””: cid 파일 경로를 설정합니다. cid 파일에는 생성된 컨테이너의 ID가 저장됩니다.
* --cpuset=””: 멀티코어 CPU에서 컨테이너가 실행될 코어를 설정합니다.
  * _--cpuset=”0,1”_처럼 설정하면 첫 번째, 두 번째 CPU 코어를 사용합니다.
  * _--cpuset=”0-3”_처럼 설정하면 첫 번째 CPU 코어부터 네 번째까지 사용합니다.
* -d, --detach=false: Detached 모드입니다. 보통 데몬 모드라고 부르며 컨테이너가 백그라운드로 실행됩니다.
* --device=\[\]: 호스트의 장치를 컨테이너에서 사용할 수 있도록 연결합니다. `<호스트 장치>:<컨테이너 장치>` 형식입니다.
  * _--device=”/dev/sda1:/dev/sda1”_처럼 설정하면 호스트의 _/dev/sda1_ 블록 장치를 컨테이너에서도 사용할 수 있습니다.
* --dns=\[\]: 컨테이너에서 사용할 DNS 서버를 설정합니다.
  * _--dns=”8.8.8.8”_
* --dns-search=\[\]: 컨테이너에서 사용할 DNS 검색 도메인을 설정합니다.
  * _--dns-search=”example.com”_처럼 설정하면 DNS 서버에 _hello_를 질의할 때 _hello.example.com_을 먼저를 찾습니다.
* -e, --env=\[\]: 컨테이너에 환경 변수를 설정합니다. 보통 설정 값이나 비밀번호를 전달할 때 사용합니다.
  * _-e MYSQL\_ROOT\_PASSWORD=examplepassword_
* --entrypoint=””: Dockerfile의 ENTRYPOINT 설정을 무시하고 강제로 다른 값을 설정합니다.
  * _--entrypoint=”/bin/bash”_
* --env-file=\[\]: 컨테이너에 환경 변수가 설정된 파일을 적용합니다.
  * _--env-file=”/etc/environment”_
* --expose=\[\]: 컨테이너의 포트를 호스트와 연결만 하고 외부에는 노출하지 않습니다.
  * _--expose=”3306”_
* -h, --hostname=””: 컨테이너의 호스트 이름을 설정합니다.
* -i, --interactive=false: 표준 입력\(stdin\)을 활성화하며 컨테이너와 연결\(attach\)되어 있지 않더라도 표준 입력을 유지합니다. 보통 이 옵션을 사용하여 Bash에 명령을 입력합니다.
* --link=\[\]: 컨테이너끼리 연결합니다. `<컨테이너 이름>:<별칭>` 형식입니다.
  * _--link=”db:db”_
* --lxc-conf=\[\]: LXC 드라이버를 사용한다면 LXC 옵션을 설정할 수 있습니다.
  * _--lxc-conf=”lxc.cgroup.cpuset.cpus = 0,1”_
* -m, --memory=””: 메모리 한계를 설정합니다. `<숫자><단위>` 형식이며 단위는 b, k, m, g를 사용할 수 있습니다.
  * _--memory=”100000b”_
  * _--memory=”1000k”_
  * _--memory=”128m”_
  * _--memory=”1g”_
* --name=””: 컨테이너에 이름을 설정합니다.
* --net=”bridge”: 컨테이너의 네트워크 모드를 설정합니다.
  * bridge: Docker 네트워크 브리지에 새 네트워크를 생성합니다.
  * none: 네트워크를 사용하지 않습니다.
  * container:&lt;컨테이너 이름, ID&gt;: 다른 컨테이너의 네트워크를 함께 사용합니다.
  * host: 컨테이너 안에서 호스트의 네트워크를 그대로 사용합니다. 호스트 네트워크를 사용하면 D-Bus를 통하여 호스트의 모든 시스템 서비스에 접근할 수 있으므로 보안에 취약해집니다.
* -P, --publish-all=false: 호스트에 연결된 컨테이너의 모든 포트를 외부에 노출합니다.
* -p, --publish=\[\]: 호스트에 연결된 컨테이너의 특정 포트를 외부에 노출합니다. 보통 웹 서버의 포트를 노출할 때 주로 사용합니다.
  * `<호스트 포트>:<컨테이너 포트>` 예\) _-p 80:80_
  * `<IP 주소>:<호스트 포트>:<컨테이너 포트>` 호스트에 네트워크 인터페이스가 여러 개이거나 IP 주소가 여러 개 일 때 사용합니다. 예\) _-p 192.168.0.10:80:80_
  * `<IP 주소>::<컨테이너 포트>` 호스트 포트를 설정하지 않으면 호스트의 포트 번호가 무작위로 설정됩니다. 예\) _-p 192.168.0.10::80_
  * `<컨테이너 포트>` 컨테이너 포트만 설정하면 호스트의 포트 번호가 무작위로 설정됩니다. 예\) _-p 80_
* --privileged=false: 컨테이너 안에서 호스트의 리눅스 커널 기능\(Capability\)을 모두 사용합니다.
* --restart=””: 컨테이너 안의 프로세스 종료 시 재시작 정책을 설정합니다.
  * no: 프로세스가 종료되더라도 컨테이너를 재시작하지 않습니다. 예\) _--restart=”no”_
  * on-failure: 프로세스의 Exit Code가 0이 아닐 때만 재시작합니다. 재시도 횟수를 지정할 수 있습니다. 횟수를 지정하지 않으면 계속 재시작합니다. 예\) _--restart=”on-failure:10”_
  * always: 프로세스의 Exit Code와 상관없이 재시작합니다. 예\) _--restart=”always”_
* --rm=false: 컨테이너 안의 프로세스가 종료되면 컨테이너를 자동으로 삭제합니다. `-d` 옵션과 함께 사용할 수 없습니다.
* --security-opt=\[\]: SELinux, AppArmor 옵션을 설정합니다.
  * _--security-opt=”label:level:TopSecret”_
* --sig-proxy=true: 모든 시그널을 프로세스에 전달합니다\(TTY 모드가 아닐 때도\). 단 SIGCHLD, SIGKILL, SIGSTOP 시그널은 전달하지 않습니다.
* -t, --tty=false: TTY 모드\(pseudo-TTY\)를 사용합니다. Bash를 사용하려면 이 옵션을 설정해야 합니다. 이 옵션을 설정하지 않으면 명령을 입력할 수는 있지만 셸이 표시되지 않습니다.
* -u, --user=””: 컨테이너가 실행될 리눅스 사용자 계정 이름 또는 UID를 설정합니다.
* -v, --volume=\[\]: 데이터 볼륨을 설정입니다. 호스트와 공유할 디렉터리를 설정하여 파일을 컨테이너에 저장하지 않고 호스트에 바로 저장합니다. 호스트 디렉터리 뒤에 **:ro**, **:rw**를 붙여서 읽기 쓰기 설정을 할 수 있으며 기본 값은 **:rw**입니다. 자세한 내용은 [‘6.4 Docker 데이터 볼륨 사용하기’](http://pyrasis.com/book/DockerForTheReallyImpatient/Chapter06/04)를 참조하기 바랍니다.
  * `<컨테이너 디렉터리>` 예\) _-v /data_
  * `<호스트 디렉터리>:<컨테이너 디렉터리>` 예\) _-v /data:/data_
  * `<호스트 디렉터리>:<컨테이너 디렉터리>:<ro, rw>` 예\) _-v /data:/data:ro_
  * `<호스트 파일>:<컨테이너 파일>` 예\) _-v /var/run/docker.sock:/var/run/docker.sock_
* --volumes-from=\[\]: 데이터 볼륨 컨테이너를 연결하며 `<컨테이너 이름, ID>:<ro, rw>` 형식으로 설정합니다. 기본적으로 읽기 쓰기 설정은 `-v` 옵션의 설정을 따릅니다. 자세한 내용은 [‘6.5 Docker 데이터 볼륨 컨테이너 사용하기’](http://pyrasis.com/book/DockerForTheReallyImpatient/Chapter06/05)를 참조하기 바랍니다.
  * _--volumes-from=”hello”_
  * _--volumes-from=”hello:ro”_처럼 설정하면 데이터 볼륨을 읽기 전용으로 사용합니다.
  * _--volumes-from=”hello:rw”_처럼 설정하면 데이터 볼륨에 읽기 쓰기 모두 할 수 있습니다.
* -w, --workdir=””: 컨테이너 안의 프로세스가 실행될 디렉터리를 설정합니다.
  * _--workdir=”/var/www”_

###  백그라운드 실행 -d 옵션 

#### 예시

> **docker run -d centos /bin/ping localhost**

위 예시 설명:

* docker run은 커넽이너를 생성 및 실행
* -d 백그라운드에서 실행하는 옵션
* centos\(혹은 이미지명\)
* /bin/ping localhost는 컨테이너에서 실행할 명령어 

백그라운드에서 실행되고 있는지 아닌지를 확인할 때는 docker logs명령을 사용합니다. docker container logs 명령은 컨테이너의 로그를 확인하는 명령입니다. 로그를 확인하고 싶은 컨테이너 식별자를 지정하여 실행합니다. 아래 예시를 확인해주세요.   
참고로 -t 옵션은 타임스탬프를 표시하는 것입니다.

![](../../.gitbook/assets/image%20%28935%29.png)

명령을 실행한 후에도 컨테이너는 남습니다. 실행 후의 컨테이너를 자동으로 삭제하고 싶을 때는 --rm 옵션을 지저압니다.   
  
명령의 실행 결과에 따라 컨테이너를 재시작할 때는 --restart 옵션을 지정합니다. 

### --restart 옵션 

* no                                    : 재시작하지 않는다
* on-failure                       : 종료 스테이터스가 0이 아닐 떄 재시작한다. 
* on-failure:횟수 n          :   종료 스테이터스가 0이 아닐때 n번 재시작한다.
* always                           :  항상 재시작 한다. 
* unless-stopped            :  최근 컨테이너가 정지 상태가 아니라면 항상 재시작한다.

 아래에서 --restart옵션 always값을 사용하고여 exit 명령어로 나와도 계속 컨테이너가 실행한 모습을 확인 할 수 있습니다.

![](../../.gitbook/assets/image%20%28934%29.png)

> 참고! --rm 옵션과 --restart 옵션은 동시에 사용할 수 없으므로 주의하기 바랍니다.

##  컨테이너의 네트워크 설정 

> **docker run 네트워크옵션     이미지명:태그명     인수**

**--add-host= 호스트명:ip주소                                     : 컨테이너의 /etc/hosts에 호스트명과 IP정의  
--dns=IP주소                                                                : 컨테이너용 DNS 서버의 IP 주소 지  
--expose                                                                        : 지정한 범위의 포트 번호를 할당  
--mac-address=MAC주소                                          : 컨테이너의 MAC주소 지정  
--net=\[bridge \| none \| container&lt;name \| id&gt; \|host \|NETWORK : 컨테이너의 네트워크를 지정   
--hostname, -h                                                             : 컨테이너 자신의 호스트명을 지정  
--publish, -p호스트의 포트번호: 컨테이너의 포트번호     : 호스트와 컨테이너의 포트 매핑  
--publish-all, -P\(대문자\)                                                         : 호스트에 임의의 포트를 컨테이너에 지정** 

 **컨테이너를 시작할 떄 네트워크에 관한 설정을 할 수 있습니다.   
컨테이너의 포트 번호와 호스트 OS의 포트번호를 매핑할 떄느 아래와 같은 명령을 실행합니다.** 

```text
$ docker run -d -p 8080:80 nginx
```



DNS 서버를 설정 할때는 아래 명령을 실행합니다. 

```text
$ docker run -d --dns 192.168.1.1 nginx
```

MAC 주소를 지정할 때는 

```text
$ docker run -d --mac-address="92:d0:c6:0a:29:33" centos

$ docker container inspect --format="{{ .Config.MacAddress }}"
```

