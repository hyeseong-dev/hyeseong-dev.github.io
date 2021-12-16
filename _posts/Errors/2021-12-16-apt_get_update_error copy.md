---
layout: post
title: "refusing to merge to unrelated histories on GIT"
date: 2021-12-16 23:09
category: Erros
tags: [apt-get]

---

<img src="https://trello.com/1/cards/60e3a2b6b3eebd856d7f1da8/attachments/60e3a35db4e04e0381bca4fa/previews/60e3a35db4e04e0381bca501/download/image.png" width=200 height=200>

pull 명령 실행시 이런 문구와 함께 진행되지 않는다면, 다음의 명령으로 실행한다.


> git pull origin 브런치명 --allow-unrelated-histories

`--allow-unrelated-histories`   이 명령 옵션은 이미 존재하는 두 프로젝트의 기록(history)을 저장하는 드문 상황에 사용된다고 한다. 즉, git에서는 서로 관련 기록이 없는 이질적인 두 프로젝트를 병합할 때 기본적으로 거부하는데, 이것을 허용해 주는 것이다.