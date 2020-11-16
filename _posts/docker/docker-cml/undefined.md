# 도커 대시보드

##  docker version 

docker version 확인 명령어

INPUT

```text
docker version
```

OUTPUT

```text
Client:
 Version:           19.03.8
 API version:       1.40
 Go version:        go1.13.8
 Git commit:        afacb8b7f0
 Built:             Wed Oct 14 19:43:43 2020
 OS/Arch:           linux/amd64
 Experimental:      false

Server:
 Engine:
  Version:          19.03.8
  API version:      1.40 (minimum version 1.12)
  Go version:       go1.13.8
  Git commit:       afacb8b7f0
  Built:            Wed Oct 14 16:41:21 2020
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          1.3.3-0ubuntu2
  GitCommit:        
 runc:
  Version:          spec: 1.0.1-dev
  GitCommit:        
 docker-init:
  Version:          0.18.0
  GitCommit:
```



## docker system info 

 도커 실행 환경의 설정이 표시됩니다. 

INPUT

```text
docker info
```

OUTPUT

```text
Client:
 Debug Mode: false

Server:
 Containers: 2
  Running: 2
  Paused: 0
  Stopped: 0
 Images: 1
 Server Version: 19.03.8
 Storage Driver: overlay2
  Backing Filesystem: <unknown>
  Supports d_type: true
  Native Overlay Diff: true
 Logging Driver: json-file
 Cgroup Driver: cgroupfs
 Plugins:
  Volume: local
  Network: bridge host ipvlan macvlan null overlay
  Log: awslogs fluentd gcplogs gelf journald json-file local logentries splunk syslog
 Swarm: inactive
 Runtimes: runc
 Default Runtime: runc
 Init Binary: docker-init
 containerd version: 
 runc version: 
 init version: 
 Security Options:
  apparmor
  seccomp
   Profile: default
 Kernel Version: 5.4.0-52-generic
 Operating System: Ubuntu 20.04.1 LTS
 OSType: linux
 Architecture: x86_64
 CPUs: 2
 Total Memory: 1.914GiB
 Name: ubuntu
 ID: SPE4:FS6V:AIFW:RU5N:W3OD:46F2:OOWL:G5H5:XUTR:Q5C2:YRBL:MKVW
 Docker Root Dir: /var/lib/docker
 Debug Mode: false
 Registry: https://index.docker.io/v1/
 Labels:
 Experimental: false
 Insecure Registries:
  127.0.0.0/8
 Live Restore Enabled: false

WARNING: No swap limit support
```

## docker 디스크 이용 상황

  디스크의 이용상황이 표시됩니다. 

INPUT

```text
docker system df
```

OUTPUT

```text
TYPE                TOTAL               ACTIVE              SIZE                RECLAIMABLE
Images              1                   1                   215.1MB             0B (0%)
Containers          2                   2                   5B                  0B (0%)
Local Volumes       1                   0                   180.2MB             180.2MB (100%)
Build Cache         0                   0                   0B                  0B

```



## 컨테이너 이용상황 확인



INPUT

```text
docker  stats webserver
```

OUTPUT

```text
CONTAINER ID        NAME                CPU %               MEM USAGE / LIMIT     MEM %               NET I/O             BLOCK I/O           PIDS
0b10e29a88a9        modest_hellman      0.00%               2.176MiB / 1.914GiB   0.11%               4.41kB / 0B         0B / 0B             1
```



