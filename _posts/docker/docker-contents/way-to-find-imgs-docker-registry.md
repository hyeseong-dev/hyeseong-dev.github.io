---
description: 도커 레지스트리와 프라이빗 레지스트리(회원가입)
---

# Way To Find Images - Docker registry

![&#xB3C4;&#xCEE4; taxonomy\(&#xBD84;&#xB958;&#xCCB4;&#xACC4;\) ](../../.gitbook/assets/image%20%28117%29.png)

 이미지 출처: [https://github.com/dotnet-architecture/eShopModernizing/wiki/03.-Publishing-your-Windows-Container-images-into-a-Docker-Registry](https://github.com/dotnet-architecture/eShopModernizing/wiki/03.-Publishing-your-Windows-Container-images-into-a-Docker-Registry)



###  도커 레지스트리

 도커 이미지를 받는 방법과 찾는 방법에 대해 알아 볼게요.   
도커 레지스트리는 딱봐도 책꽃이처럼 보이조.   
여러분이 올린 레지스토리를 업로드하고 다운로드 할 수 있어요. 결국 static 이미지를 보관하는 장소가 registry에요. 

**Registry:**  결국 이 static 상태의 image들이 담긴 공간 

**Images** : 정적 상태로 컨테이너로 구성되어 있어요. 여러 App들이 담겨 있는 녀석이에요.   
그림에서 node js가 담겨있는 컨테이너도 보이조? 

그렇다면 이미지를 사용하기 위해선 어떻게 해야 할까요?  ****

**Container: 이미지를 실행시키기 위한 상태**   
 톰캣을 실행해서 웹페이지를 띄워 봤습니다. '도커 설치 및 구현'페이지 참고하세요.   
**사실 컨테이너가 웹페이지를 띄워준거에요.**  
  


### hub.docker.com 

더 간단하게 레지스트리를 확인할수 있는 페이지에요. 

####  1. CML으로 확인

> sudo docker search tomcat \# node 나 tomcat을 사용해 이미지를 확인할 수 있어요.

#### 2. web으로 확인 

>

![&#xB3C4;&#xCEE4;&#xD5C8;&#xBE0C;](../../.gitbook/assets/image%20%2842%29.png)

![&#xCC3E;&#xAE38; &#xC6D0;&#xD558;&#xB294; &#xC774;&#xBBF8;&#xC9C0; &#xAC80;&#xC0C9;](../../.gitbook/assets/image%20%2838%29.png)



![&#xC77C;&#xBC18; &#xC0AC;&#xC6A9;&#xC790;&#xAC00; &#xC62C;&#xB9B0; &#xC774;&#xBBF8;&#xC9C0; ](../../.gitbook/assets/image%20%28128%29.png)

 빈그림의 파일이 있거나, 결정적으로 경로가 있는 파일명은 일반 사용자가 올렸어요.  그리고 사용자의 아이디에 해당되기도해요.   
그 외에 OFFICIAL IMAGE라고 붙은 것들은 도커 허브 운영진들이 업로드 한거에요. 



### **프라이빗 레지스트리**

1.  도커 허브 가입해주세요. 
2. billing 페이지로 이동해주세요. 

![billing &#xD398;&#xC774;&#xC9C0; &#xC774;&#xB3D9;](../../.gitbook/assets/image%20%2868%29.png)

![billing &#xD654;&#xBA74; ](../../.gitbook/assets/image%20%289%29.png)

빌링 화면에  플랜을 선택할수 있어요.  **change plan**   
  


![](../../.gitbook/assets/image%20%28132%29.png)

 유료로 사용하면 무료로 1개만 사용하는 레포지토리를 pro로 바꾸면 더많은 레포지토리를 사용할 수 있어요.

물론 추후에 무료로 더 많은 레포지토리를 사용할 수 있지만 번거로운 과정이 있어요. 

본인만의 레포지토리를 구성해서 업로드하고 다운로드하고 여러사람과 공유하는 기능을 구축하거나 자신만 사용하기 위해 저장소를 관리하는 서비스를 사용하기 위해서 프라이빗 레지스트리는 필요한 부분이에요. 

 

