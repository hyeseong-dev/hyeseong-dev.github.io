---
layout: post
title: "테스트 종류"
date: 2021-12-16 22:38
category: etc
tags: [test]

---

# Gunicorn & Nginx

- [gunicorn은 대체 뭐하는 놈일까 (부제: CGI, WSGI는 대체 뭐냐)](https://this-programmer.tistory.com/entry/gunicorn%EC%9D%80-%EB%8C%80%EC%B2%B4-%EB%AD%90%ED%95%98%EB%8A%94-%EB%86%88%EC%9D%BC%EA%B9%8C-%EB%B6%80%EC%A0%9C-CGI-WSGI%EB%8A%94-%EB%8C%80%EC%B2%B4-%EB%AD%90%EB%83%90)

- [Python WAS 구축하기 ( Django, Nginx, Gunicorn )](http://dveamer.github.io/backend/PythonWAS.html)
- [zlib-devel](http://ftp.riken.jp/Linux/cern/centos/7/updates/x86_64/repoview/zlib-devel.html#:~:text=Description%3A,zlib%20compression%20and%20decompression%20library.) : zlib-devel - Header files and libraries for Zlib development
- [zlib](https://www.gpgstudy.com/forum/viewtopic.php?t=14816) : zlib 는 그냥 데이터를 압축하는 라이브러리
  - zip 는 zlib 를 이용해서 파일들을 패킹하는 포멧
  - gzip 는 zlib 를 이용해서 파일을 압축하긴 하지만, 단일 파일만 되구
  - 보통 파일을 tar 란 놈으로 묶어서 그것을 압축합니다. (예. tar.gz)
- [OpenSSL인증서](https://brownbears.tistory.com/232) : 웹브라우저와 서버 간의 통신을 암호화하는 오픈소스 라이브러리라고 보면 된다.한 마디로 Openssl을 웹서버(Apache,Nginx)에서 자유롭게 사용할 수 있다.Openssl 사용현황은 대부분의 사이트가 2/3가 Openssl을 채용했다고 보면된다.이 Openssl이 최근에 Heart bleed(심장에 출혈나다?) 버그로 이슈화가 되었다.

- [SSL](https://blog.naver.com/ysw1130/120211395594) : Secure Socket Layer로 월드 와이드 웹 브라우저와 웹 서버 간에 데이터를 안전하게 주고받기 위한 업계 표준 프로토콜을 의미한다

- [-devel 패키지](https://pythonq.com/so/c/1904039) : `*-devel 패키지 (일반적으로 데비안 기반 배포판에서 *-dev라고 함)는 일반적으로 주어진 라이브러리에 대해 코드를 컴파일하는 데 필요한 모든 파일입니다.`