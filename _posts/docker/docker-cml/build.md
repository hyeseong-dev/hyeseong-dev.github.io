---
description: Dockerfile로 이미지를 생성하는 build 명령어
---

# Build

## 문법과 옵션 

{% tabs %}
{% tab title="syntax" %}
```text
docker build <옵션> <도커파일의 경로>
```

dockerfile 경로는 로컬경로와 URL을 사용할 수 있고, -를 설정하면 표준 입력으로 Dockerfile 내용을 받을 수 있어요. 
{% endtab %}
{% endtabs %}



1.--force-rm = false  
 이미지 생성에 실패했을 때도 임시 컨테이너를 삭제해요

2. --no-cache=false  
이전 빌드에서 생성된 캐시를 사용하지 않아요 Docker는 이미지 생성 시간을 줄이기 위해서 Dockerfile의 각 과정을 캐시하는데, 이 캐시를 사용하지 않고 처음부터 다시 이미지를 생성해요. 

3. -q, --quiet=false  
Dockerfile의 RUN이 실행할 출력 결과를 표시하지 않아요. 

4. --rm=true  
이미지 생성에 성공했을때 임시 컨테이너를 삭제합니다. 

5. -t, --tag=""  
저장소 이름, 이미지 이름, 태그를 설정해요. **&lt;저장소이름&gt;/&lt;이미지이름&gt;:&lt;태그&gt;**형식이에요.

* hello
* hello:0.1
* exampleuser/hello
* exampleuser/hello:0.1

## 실습

일반적으로 Dockerfile이 있는 경로에서 docker build 명령을 실행해요.   
**Dockerfile이 있는 특정 경로를 설정**할 수도 있어요.

```text
docker build -t hello . 
docker build -t hello /opt/hello
docker build -t hello ../../
```



#### Docker 파일의 URL을 사용하 이미지 생성 

```text
docker build -t hello https://raw.githubusercontent.com/kstaken/dockerfile-examples/master/apache/Dockerfile
```



다음은 Dockerfile 경로에 -를 설정하여 Dockerfile 내용을 표준 입력으로 받아요. 

```text
echo -e "FROM ubuntu:18.04\nRun apt-get update | sudo docker build -t hell0 -
cat Dockerfile | sudo docker build -t hello -
docker build -t hello - < Dockerfile
```

echo 명령으로 문자열을 직접 출력해도 되고, cat 명령으로 파일의 내용을 파이프로 보내도되요. 

