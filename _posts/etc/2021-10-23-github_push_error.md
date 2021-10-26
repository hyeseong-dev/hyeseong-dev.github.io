---
layout: post
title: "github push error"
date: 2021-10-21 
category: etc
tags: [github, git]

---

# GITHUB PUSH ERROR

## 상황 요약 : 
 - 작성한 소스 코드를 원격 레포에 업로드 시 발생

## 원인 : 
 - 프라이빗 키가 말 그대로 UNPROTECTED가 되어 발생

## 추정 : 
 - 이전 id_rsa파일이 permission denied가 떠서 700으로 chmod 명령을 날린적 있음

## 오류 로그

```sh
venv) ➜  fastapi-demo-11 git:(main) git push origin main
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions 0755 for '/home/usr/.ssh/id_rsa' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.
Load key "/home/usr/.ssh/id_rsa": bad permissions
git@github.com: Permission denied (publickey).
fatal: 리모트 저장소에서 읽을 수 없습니다
```

## 해결

> chmod 400 id_rsa

참고, https://www.deok.me/entry/SSH-%ED%82%A4-%EC%9D%B4%EC%9A%A9-%EC%8B%9C-bad-permissions-ignore-key-%EC%97%90%EB%9F%AC%EA%B0%80-%EB%B0%9C%EC%83%9D%ED%95%A0-%EA%B2%BD%EC%9A%B0