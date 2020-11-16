# Builing Server Program w/t Jekins 2

이번에는 jekins를 이용해서 원격에서 server program build를 해볼게요.

## Step1 준비 

* Jenkins 웹페이에서 빌드 실행상태에서 돌아가는 서버를 꺼주세요. X버튼 눌러주시면 되요. 
* php 컨테이너도 삭제해주세요. 

```text
docker ps -a # jenkis 컨테이너 빼고 다 지워버리세요.
docker rm -f php컨테이너ID
```

* jenkins 웹사이트의 구성 -&gt; build 명령어 변경 

{% tabs %}
{% tab title="구성/빌드환경 /Build" %}
```text
cd /home/Docker-Pracktice
git pull
docker rm -f php || true
docker pull hyeseong43/docker-practice
docker run -p 80:
```
{% endtab %}
{% endtabs %}

현재 수정중...

