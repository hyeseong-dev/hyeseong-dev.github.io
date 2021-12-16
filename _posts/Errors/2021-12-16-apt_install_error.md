---
layout: post
title: "Database Update Error To Change Status Field "
date: 2021-12-16 23:01
category: Erros
tags: [error]

---



## 방법 1

Unable to correct problems, you have held broken packages.

만약 이러한 오류가 뜬다면 가장 추천하고 싶은 방법은 패키지 업데이트 리스트를 새로 받는 것이다.

```sh
$ cd /var/lib/apt
$ sudo mv lists lists.old
$ sudo mkdir -p lists/partial
$ sudo apt-get update
```

위 방법을 수행하면 패키지 업데이트 목록을 백업 후 다시 받는 것이다.

## 방법 2
1번 방법이 해결되지 않을 경우
`sudo apt-get -f dist-upgrade`