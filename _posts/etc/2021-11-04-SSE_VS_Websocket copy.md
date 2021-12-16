---
layout: post
title: "Websocket vs SSE"
date: 2021-11-04 17:18
category: etc
tags: [oauth2]

---

# Websocket vs SSE

## 공통점 : 
- http 연결을 통해 작동
- 서버 푸쉬 프로세스


## 차이점
### I. 통신 - 둘다 케바케
  1. W : 양방향 통신
  2. S : 단방향(only 서버만 푸쉬) 클라이언트는 받기만 가능


###  II. 독특한 기능  - 둘다 삐까삐까
  1. S : 자동재연결, 추사 이벤트 전달 능력, event IDs
  2. W: 끊긴 클라이언트 감지 능력 

###  III. 브라우저 호환성 - Websocket
  1. 실제 SSE보다 websocket에 더 많은 브라우저 호환이 가능
  2. Wsocket > SSE에 더 많은 기술자료 및 구글링 가능

###  IV. 연결 사이즈 - Websocket
 1. 브라우저당 6개의 연결 제한 
  2. 소켓( X)

###  V. 전송 데이터 유형(Transmission data types)  - Websocket
  1. W : binary and UTF-8 전송 가능
  2. S : Only UTF-8

###  VI. 확장성 - Websocket
  1. Websocket 복잡하고 설정 작업이 까다로움
  2. SSE 간단하고 빠름. But 확정하기 매우 까다로움

### VII. UseCases
  1. 실시간 채팅앱, 미디어 플레이어
  2. data 상태 업데이트, push notification, 뉴스레터, 뉴스피드

결론 : 
1. 케바케, 사용하려는 목적에 맞춰 진행함.   
2. STT 운영 관리페이지에서 실시간 소통에서 프런트에서 서버로 푸쉬하는 기능이 없거나 많지 않을 가능성이 높음   
   STT서버에서 생산된 데이터가 백엔드를 거쳐서 프런트로 도달하는 과정만큼은 명확함.(중간에 다른 매개채를 MQ?를 통할지 확인 필요)    
3. 결론적으로 SSE에 높은 비중 하지만 연결사이즈 및 몇몇 브라우저에서 SSE를 지원하지 않는 케이스가 있는 만큼 신중한 선택이 필요   