---
layout: post
title: "Dockerizing-React"
date: 2021-10-09 14:22
category: Windows
tags: ['Docker', 'Dockerfile', 'React']

---

# Dockerfile 작성

> $ vim Dockerfile

```yml
# base image
FROM node:16-alpine

# set working directory
WORKDIR /app

# `/app/node_modules/.bin`을 $PATH 에 추가
ENV PATH /app/node_modules/.bin:$PATH

# app dependencies, install 및 caching
COPY package.json /app/package.json
RUN npm install
RUN npm install react-scripts@4.0.3 -g

# 앱 실행
CMD ["npm", "start"]
```

## docker-compose.yml 작성
```yml
version: '3.8'

services:
    react:
        container_name: react_app
        build:
            context: .
            dockerfile: Dockerfile
        volumes:
            - '.:/app'
            - '/app/node_moduels'
        ports:
            - '8300:3000'
        environment:
            - NODE_ENV=development
            - CHOKIDAR_USEPOLLING=true
```

## Build & Run

> $ docker-compose up -d --build


