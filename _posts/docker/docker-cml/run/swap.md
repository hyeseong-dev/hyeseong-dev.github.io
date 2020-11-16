# swap 메모리 제한 설정

#### [4.1.](https://www.joinc.co.kr/w/man/12/docker/limits#toc) 물리 메모리와 스왑 메모리 제한

memory와 memory-swap를 이용해서, 물리메모리와 스왑메모리에 대한 제한을 걸 수 있다.

* --memory : 물리적인 메모리의 크기
* --memory-swap : 스왑메모리 + 물리메모리의 크기 즉, 전체 메모리의 크기다.

물리 메모리 200M, 스왑 메모리 300M를 가지는 컨테이너를 실행 했다.

```text
# docker run -m=200m --memory-swap=500m -it ubuntu /bin/bash
WARNING: Your kernel does not support swap limit capabilities, memory limited without swap.
```

커널 설정의 문제로 swap에 대한 제한을 지원하지 않는다는 경고문구가 뜬다. 지금 사용하는 리눅스 커널은 swap limit capabilities를 지원한다. grub 설정을 바꾸고 재시작하자.

```text
# /etc/default/grub
...
...GRUB_CMDLINE_LINUX_DEFAULT="cgroup_enable=memory swapaccount=1"
# update-grub 
# reboot 
```

경고 메시지 없이 도커가 실행된다.

```text
# docker run -m=200m --memory-swap=500m -it ubuntu /bin/bash
# root@3b8fe21aa4c4:/# 
```

free 명령을 이용해서 컨테이너의 메모리 상태를 확인해보자.

```text
root@3b8fe21aa4c4:/# free
             total       used       free     shared    buffers     cached
Mem:       1016804     275248     741556       5120      14920     140872
-/+ buffers/cache:     119456     897348
Swap:       520188          0     520188
```

예상과 달리, 제한했던 메모리 정보가 아닌 전체 시스템의 메모리 정보가 출력된다. 실제 컨테이너에 할당된 메모리 정보는 cgroup을 확인해야 한다.

```text
# cd /sys/fs/cgroup/memory/system.slice/docker-<dockerid>.scope
# cat memory.stat
cache 4325376
rss 487424
rss_huge 0
mapped_file 2809856
writeback 0
swap 0
pgpgin 3105
pgpgout 1930
pgfault 3212
pgmajfault 37
inactive_anon 4096
active_anon 512000
inactive_file 843776
active_file 3452928
unevictable 0
hierarchical_memory_limit 209715200
hierarchical_memsw_limit 524288000
...
```

메모리 제한이 적용된 걸 확인 할 수 있다.

