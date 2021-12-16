---
layout: post
title: "Database Update Error To Change Status Field "
date: 2021-12-16 23:01
category: Erros
tags: [error]

---

# Terms Of IPCC
### 발생시간 : 2021-07-07 오전 중 여러 차례 발생
###  PC 스펙 : 
  1 삼성 노트북, 모델 550XDA, 11th Gen Intel(R) Core I7-1165G7, 2.80GHz
  2 메모리 16.0GB, 64비트 운영 체제, x64 기반 프로세서
  3 Hyper-V를 이용한 WSL2 Ubuntu 백엔드 개발 환경 구성

### 오류 개요 : 고객 통화 종료 후 실시간 상담 모니터링 화면에서 여전히 통화중 상태로 남아있음.
### 오류 원인 추정: 
1. django db 연결 default 방식은 request시 Open하며 이후 닫아 버리는 statless 특성을 갖고 있어
여러 요청 및 시그널을 받다가 DB Data Update시 요청을 이행하지 못하여 수정하지 못하는 현상 발생

### 제안 되는 방식 : 
1. 프런트 단에서 불필요한 요청수 최소화 및 개선(예. 다른 끊어진 통화 번호를 요청하는 경우. 특히 대화창 클릭시 그때 부터 통화가 끊어지고 나서도 요청하여 Bad Request를 발생시켜 DB 접속 시도가 잦아짐)
2. NoSQL의 일종인 in memory저장소 이용(1. 디스크를 거치지 않아 빠름. 2. 만료일을 지정하여 자동으로 데이터가 삭제시킴 3. 저장소 메모리 재사용)
3. Asyncio 로직으로 재구성함
4. DB CONN_MAX_AGE를 None으로 변경

### 선택한 방식 : 
4번으로 선택
 - 1번의 경우 현재 바로 바로 개선하기에 무리가 있음
 - 담장자인 이미경 매니저님이 춘계학술대회로 인하여 외근중
 - 2번과 3번의 경우 새로운 기술스택이므로 이로인한 러닝 커브가 존재하여 바로 적용하기에 무리가 있음

###

###   참고자료 : 
  1 https://americanopeople.tistory.com/260
  2 https://github.com/benoitc/gunicorn/issues/996
  3 https://stackoverflow.com/questions/53618764/how-to-use-persistance-db-connection-in-django