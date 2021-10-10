---
layout: post
title: "Dockerizing-React"
date: 2021-10-09 14:22
category: Javascript/React
tags: ['Docker', 'Dockerfile', 'React']

---

# Dockerfile 작성

> $ vim Dockerfile

```yml
FROM node:16-alpine

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install and cache app dependencies
COPY package.json /app/package.json
RUN npm install --silent && \
    npm install react-scripts@4.0.3 -g --silent && \
    npm install -g serve && \
    npm run build

# start app
```

## docker-compose.yml 작성
```yml
version: '3.8'

services:
  frontend:
    container_name: react_app
    build:
      context: .
      dockerfile: Dockerfile
    volumes:
      - '.:/app'
      - '/app/node_modules'
    ports:
      - '8300:3000'
    environment:
      - NODE_ENV=development
      - CHOKIDAR_USEPOLLING=true
    command: sh -c "npx serve -l 3000 -s build"

```

## Build & Run

> $ docker-compose up -d --build


### npm start VS npx serve

npm과 npx 패키지 매니저를 사용하는 차이점은 둘째치고 중요한 것은 start명령어와 serve명령어의 차이점을 살펴볼건데요. 

start 명령어를 사용하면 serve 명령어보다 10배 이상 용량을 크게 가져옵니다. 
즉, create-react-app 라이브러리에서 개발시 필요한 것들을 모두 끌어다 사용하기 때문이조. 
그럼 배포시에는 npx serve 명령어를 이용하여 작은 용량으로 처리하면 됩니다. 

참고로 1.7MB vs 143kb의 차이를 보입니다.
 - 엄청난 용량 차이를 보임
 - build 하였을 경우에만 serve 명령어를 통해 변경된 코드가 반영되어 확인 할 수 있음.
