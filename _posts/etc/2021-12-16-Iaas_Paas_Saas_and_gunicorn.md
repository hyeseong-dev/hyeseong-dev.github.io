---
layout: post
title: "Iaas, Paas, Saas, Queue"
date: 2021-12-16 22:38
category: etc
tags: [gunicorn, paas, saas, iaas]

---

# Iaas, Paas, Saas, Queue, Gunicorn

-  https://wnsgml972.github.io/network/2018/08/14/network_cloud-computing/

-  [프록시](https://brownbears.tistory.com/191)

-  [Apache vs Nginx](https://taes-k.github.io/2019/03/08/server-nginx-event-driven/)

-  wsgi

  - (WSGI는 python application(python script)이 Web Server와 통신하기 위한 표준 Interface이며 Python Framework입니다! (일종의 프로토콜이라고 생각하면 쉬울 것 같아요)

> HTTP requests -> Web Server -> WSGI Server(Middleware) -> Django(WSGI를 지원하는 Web Application)


- gunicorn : gunicorn은 Python WSGI HTTP Server입니다. gunicorn은 상대적으로 빠르고 가볍고 사용이 쉽다고 합니다.
  - 특징
    - WSGI, web2py, Django 그리고 Paster 를 지원
    - Automatic worker process management
    - 간단한 Python configuration
    - Multiple worker configurations
    - 확장성(extensibility)을 위한 다양한 Server hook들
    - python2.6+ 그리고 python3.2+ 과 호환 가능
 
Django에서는 wsgi.py에서 application = get_wsgi_application() 를 통해 wsgi handler를 가져옵니다. wsgi handler에서는 middleware등 을 처리하고, WSGI server에서는 설정을 읽어 application의 경로를 가져옵니다.

Django 기본 명령어인 runserver 명령은 WSGI_APPLICATION 설정에서 경로를 가져옵니다. 

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FQ00Ay%2FbtqGuqjD4JU%2FkvM3Jgdu77dBHqi6sqkfh1%2Fimg.png)
