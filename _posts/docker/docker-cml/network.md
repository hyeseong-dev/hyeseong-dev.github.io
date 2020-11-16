# NETWORK

### 도커 컨테이너 네트워크 <a id="&#xB3C4;&#xCEE4;-&#xCEE8;&#xD14C;&#xC774;&#xB108;-&#xB124;&#xD2B8;&#xC6CC;&#xD06C;"></a>

* Docker 컨테이너끼리 통신할 때는 Docker 네트워크를 통해 수행
* Docker는 기본 네트워크 값으로 bridge, hosts, none 세 개의 네트워크를 만듦

### Docker 네트워크 목록 표시 <a id="docker-&#xB124;&#xD2B8;&#xC6CC;&#xD06C;-&#xBAA9;&#xB85D;-&#xD45C;&#xC2DC;"></a>

* Docker network ls \[옵션\]
* 주요 옵션
  * -f, –filter=\[\] : 출력을 필터링
  * --no-trunc : 상세 정보를 출력
  * -q, –quiet : 네트워크 ID만 표시

**네트워크 목록 표시 \(예제\)**

```text
$ sudo docker network ls
NETWORK ID          NAME                DRIVER              SCOPE
914f387eab6b        bridge              bridge              local
c8fa1e69139e        host                host                local
478c12382ce4        none                null                local
```

* 따로 추가한게 없으므로 기본 네트워크 세 개가 추가됨
* 표시할 네트워크의 상세 정보 확인 : –no-trunc 옵션
* 네트워크 ID만 확인할 경우 : -q 또는 –quiet 옵션
* 필터링을 하고 싶을 때 : -f 또는 –filter 옵션
  * 필터링시 key=value 형태로 지정

| 필터링값 | 설명 |
| :--- | :--- |
| driver | 드라이버 지정 |
| id | 네트워크 ID |
| label | 네트워크에 설정된 라벨\(label=&lt;Key&gt; 또는 &lt;Key&gt;=&lt;value&gt;로 지정 |
| name | 네트워크명 |
| scope | 네트워크의 스코프\(swarm/global/local |
| type | 네트워크의 타입\(사용자 정의 및 네트워크 custom/정의 완료 네트워크 builtin\) |

**네트워크 목록 표시의 필터링 \(예제\)**

```text
$ sudo docker network ls -q --filter driver=bridge
914f387eab6b
```

* 브리지 네트워크의 네트워크 ID만을 목록으로 표시

**컨테이너 시작 및 네트워크 확인 - 기본값 \(예제\)**

* 네트워크를 명시적으로 지정하지 않고 Docker 컨테이너를 시작하면 기본값인 ‘bridge” 네트워크로 Docker 컨테이너를 시작
* 네트워크 미지정으로 컨테이너 시작

```text
$ sudo docker container run -itd --name=sample ubuntu:latest
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
7ddbc47eeb70: Pull complete
c1bbdc448b72: Pull complete
8c3b70e39044: Pull complete
45d437916d57: Pull complete
Digest: sha256:6e9f67fa63b0323e9a1e587fd71c561ba48a034504fb804fd26fd8800039835d
Status: Downloaded newer image for ubuntu:latest
6f5f6f2977d0396a055bb56de9483230600e67259f638b2933c73878a2cfb096
```

* 네트워크 확인
  * NetworkID : 브릿지 네트워크 914f387eab6b로 컨테이너가 시작하는 것을 볼 수 있음

```text
$ sudo docker container inspect sample | grep -A 20 'Networks"'
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": "914f387eab6bad21aa135f72502af7712546bb9e18171053620452e1024a5e7b",
                    "EndpointID": "87327fa279458f5d54052b24118294689ca46daa621a6e10651479b0d627fe97",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.3",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:11:00:03",
                    "DriverOpts": null
                }
            }
        }
    }
]
```

### 네트워크 작성 <a id="&#xB124;&#xD2B8;&#xC6CC;&#xD06C;-&#xC791;&#xC131;"></a>

* docker network create \[옵션\] 네트워크
* 주요 옵션

  * --driver, -d : 네트워크 브리지 또는 오버레이\(overlay\) & 커스텀 네트워크 , 기본값은 bridge

  > 오버레이 네트워크 : 여러 개의 호스트에 걸쳐있는 네트워크

  * --ip-range : 컨테이너에 할당하는 IP 주소의 범위 지정
  * --subnet : 서브넷을 CIDR 형식으로 지정
  * --ipv6 : ipv6 네트워크를 유효화할지 말지\(true/false\)
  * -label : 네트워크에 설정하는 라벨

**브리지 네트워크 작성 \(예제\)**

* web-network라는 이름의 브리지 네트워크를 작성

 참고로 --driver 옵션에서 지정할수 있는 네트워크 드라이버 키값은 'bridge' 또는 'overlay'입니다. 또한 커스텀 네트워크 드라이버도 사용할 수 있습니다. **오버레이 네트워크는 여러개의 호스트에 걸쳐있는 네트워크를 말합니다.**

```text
$ sudo docker network create --driver=bridge web-network
ff20a5e471efedc350cf63c0bbcd4619afa8cd969993aa9686a8fdf3c70624d1
```

* 작성한 네트워크 확인

```text
$ sudo docker network ls
NETWORK ID          NAME                DRIVER              SCOPE
914f387eab6b        bridge              bridge              local
c8fa1e69139e        host                host                local
478c12382ce4        none                null                local
ff20a5e471ef        web-network         bridge              local
```

* 사용자가 생성한 네트워크는 기본 브리지 네트워크와 이름 해결 구조가 다름
  * 사용자 정의 네트워크를 사용하는 편이 보다 유연하고 쉽게 네트워크 구성 관리를 할 수 있음
  * 기본 브리지 네트워크 사용 : link 기능과 같이 /etc/hosts 파일에 의존적
  * 사용자 정의 네트워크 : 내장된 DNS 서버에 의해 이름 해결

### 네트워크 연결 <a id="&#xB124;&#xD2B8;&#xC6CC;&#xD06C;-&#xC5F0;&#xACB0;"></a>

####  문법

> **docker network connect \[옵션\] 네트워크 컨테이너**

* Docker 컨테이너를 Docker 네트워크에 연결

> **docker network disconnect \[옵션\] 네트워크 컨테이너**

* 네트워크에서 연결을 해제할 때

#### network connect 명령어 주요 옵션 

* --ip : IPv4 주소
* --ip6 : IPv6 주소
* --alias : 별칭명
* --link : 다른 컨테이너에 의한 링크

**네트워크에 대한 연결 \(예제\)**

* 네트워크에 대한 연결
  * sample 컨테이너를 web-network 네트워크에 연결
  * 연결하고나면 동일 네트워크상 다른 컨테이너와 통신 가능
  * 연결은 IP 주소 뿐만 아니라 컨테이너명 혹은 컨테이너 ID도 그대로 사용할 수 있음

```text
$ sudo docker network connect web-network sample
```

* 컨테이너 네트워크 확인

```text
$ sudo docker container inspect sample | grep -A 20 'web-'
                "web-network": {
                    "IPAMConfig": {},
                    "Links": null,
                    "Aliases": [
                        "6f5f6f2977d0"
                    ],
                    "NetworkID": "ff20a5e471efedc350cf63c0bbcd4619afa8cd969993aa9686a8fdf3c70624d1",
                    "EndpointID": "43556adf01f64c1b39b25dc9ec662b3a981d47dd7e6c52eba2f98aa0c4a81a29",
                    "Gateway": "172.19.0.1",
                    "IPAddress": "172.19.0.2",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:13:00:02",
                    "DriverOpts": {}
                }
            }
        }
    }
]
```

**네트워크를 지정한 컨테이너 시작 \(예제\)**

```text
$ sudo docker container run -itd --name sample2 --net=web-network nginx
9d4977cbb33a4e50bd00169a702b019f79e8cbfbbff469c123bf50e73a9de8f3
```

* 컨테이너 시작 시 네트워크 연결하기

**네트워크에 대한 연결 해제 \(예제\)**

```text
$ sudo docker network disconnect web-network sample
$ docker container inspect sample | grep -A 20 'web-'
```

* 네트워크 연결 해제

### 네트워크 상세 정보 확인 <a id="&#xB124;&#xD2B8;&#xC6CC;&#xD06C;-&#xC0C1;&#xC138;-&#xC815;&#xBCF4;-&#xD655;&#xC778;"></a>

* docker network inspect \[옵션\] 네트워크

**네트워크 상세 정보 표시 \(예제\)**

* web-network 이름의 네트워크 상세 정보 표시
  * 서브넷 : 172.19.0.0/16
  * 게이트웨이 : 172.19.0.1
  * 1개의 컨테이너 가동중 - sample2\(172.19.0.3\)

```text
$ sudo docker network inspect web-network
[
    {
        "Name": "web-network",
        "Id": "ff20a5e471efedc350cf63c0bbcd4619afa8cd969993aa9686a8fdf3c70624d1",
        "Created": "2019-10-21T05:54:45.972527483+09:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": {},
            "Config": [
                {
                    "Subnet": "172.19.0.0/16",
                    "Gateway": "172.19.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {
            "9d4977cbb33a4e50bd00169a702b019f79e8cbfbbff469c123bf50e73a9de8f3": {
                "Name": "sample2",
                "EndpointID": "7400c7ae460f5d11058a322388f60da77210d6b112f0f150847615d8b36429a5",
                "MacAddress": "02:42:ac:13:00:03",
                "IPv4Address": "172.19.0.3/16",
                "IPv6Address": ""
            }
        },
        "Options": {},
        "Labels": {}
    }
]
```

### 네트워크 삭제 <a id="&#xB124;&#xD2B8;&#xC6CC;&#xD06C;-&#xC0AD;&#xC81C;"></a>

* docker network rm \[옵션\] 네트워크

**네트워크 삭제 \(예제\)**

* 선작업\) docker network disconnect 명령을 이용하여 연결 중인 모든 컨테이너와 연결을 해제

```text
// 사용중인 건이 있을 경우 다음과 같이 에러가 발생함
$ sudo docker network rm web-network
Error response from daemon: error while removing network: network web-network id ff20a5e471efedc350cf63c0bbcd4619afa8cd969993aa9686a8fdf3c70624d1 has active endpoints

// 연결해제
$ sudo docker network disconnect web-network 9d4977cbb33a
```

* 네트워크 삭제

```text
$ sudo docker network rm web-network
web-network
```

