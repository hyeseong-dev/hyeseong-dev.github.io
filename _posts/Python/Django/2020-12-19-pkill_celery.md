---
layout: post
title: "[Django] Conversion Of Datetime Format"
date: 2020-11-26 22:22
category: Python
tags: [Python,Paypal,Django]

---

<img src="https://trello.com/1/cards/61b017f7dfabd36fb851f37e/attachments/61b018695259f54f0e4a3a1b/previews/61b0186a5259f54f0e4a3a29/download/image.png" width=400 height=400>


- 결론 : 
  - pkilll -f `"문자처리" 즉 따옴표 사용해야함`
  - celery 옵션중 -Q 옵션은 사용 가능함. 
- 담당자 : 이혜성 연구원 
- 발생(목격) 일시 : 2021-12-08 오전 11시
- 해결 일시: 2021-12-08 오전 11시30분
- 상황 : `celery worker auto reload를 사용하던중 pkill과 celery -Q 옵션 오류`
- 원인 : 
  - pkill의 경우 -f 의 파라미터 값으로 문자를 넣어줘야 하는데 이때 따옴표 처리를 하지 않아서 발생
  - celery -Q옵션의 경우 -Q 옵션 이후 모든 인자들을 띄우지 않고(심지어 콤마 역시도 모두 붙임) 입력해야함
- 해결 방안 : 상기 원인에 밝힘
- 참고 : https://testdriven.io/courses/django-celery/multiple-queues/