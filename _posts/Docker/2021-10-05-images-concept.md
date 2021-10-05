---
layout: post
title: "[docker] Differences of Docker Images"
date: 2020-11-19 22:00
category: docker
tags: [docker,container]
image: 'images/posts/linux.png'
---
# stretch/buster/jessie

Images tagged with stretch, buster, or jessie are codenames for different Debian releases. At the time of this writing, the stable Debian release is 10.4, and its codename is “Buster.” “Stretch” was the codename for all version 9 variations, and “Jessie” was the codename for all version 8 variations.

Future versions in development, but not yet stable, are “Bullseye” and “Bookworm.” You may start seeing these tags in the list of image versions on DockerHub.

Choose one of these images if your code is compatible with a specific version of the Debian operating system. You rarely will need to use older versions of Debian when starting a new project.

## -slim

The slim image is a paired down version of the full image. This image generally only installs the minimal packages needed to run your particular tool. In the case of python, that’s the minimum packages to run python and the same for node.js.

By leaving out lesser-used tools, the image is smaller. Use this image if you have space constraints and do not need the full version.

But be sure to test thoroughly when using this image! If you run into unexplained errors, try switching to the full image and see if that resolves it.

## -alpine

Alpine images are based on the Alpine Linux Project, which is an operating system that was built specifically for use inside of containers. For a long time, these were the most popular image variations due to their tiny size.

However, some teams are moving away from alpine because these images can cause compatibility issues that are hard to debug. Specifically, if using python images, some wheels are built to be compatible with Debian and will need to be recompiled to work with an Apline-based image.

The main reason to use an Alpine image is to make your resulting image as small as possible. The base image will be smaller than 5MB. The python base image (adding python to the base alpine image) is currently 78.9MB. That’s still very small.

This image is the most highly recommended if space is a concern.

The disadvantage is that it does not contain some packages that you might need. Mainly, it uses a slimmer musl lib instead of glibc. You may run into issues if your application has specific libc requirements.

If you find the Alpine image is lacking in something you need, you can always install it directly in your Dockerfile. This keeps the image to only what you need. Be aware that your Dockerfile will change if you are installing external packages. The main difference is that you will use apk instead of apt-get to install packages.

There have been concerns regarding -alpine images, so you need to be aware of them. Read about some of them here and here and do your own research. Again, if you are experiencing an unexplained issue in building your Dockerfile, try switching to the full image to see if that cures it.

## -windowsservercore
I rarely use windows, I am firmly in the Mac / Linux camp now, but if your application runs only on Windows or Windows Server, this is the image for you.

## But this still doesn’t help me. Which one do I choose?
Here are some general guidelines I use:

- If I need to get something up and running quickly, have no space constraints, and don’t have time to test much, I start with the de-facto image. My main concern here is that the image has everything I need to work out of the box, and I don’t have to worry much. This image, however, will be the largest.

- If space is a concern and I know I need only the minimal packages for running a particular language like python, I go with -slim.

- For some projects that I have time to test thoroughly, and have extreme space constraints, I will use the Alpine images. But be aware that this can lead to longer build times and obscure bugs. If you are having trouble porting your docker containers to new environments, or something breaks as you add new packages, it may be because of the Alpine image.

- Lastly, always scroll to the bottom of the DockerHub page for a particular image and read about suggestions for choosing an image.

## Comparing docker image sizes
If you want to inspect docker images yourself and compare, try this.

```sh
docker pull --quiet python:3.8
docker pull --quiet python:3.8.3
docker pull --quiet python:3.8.3-slim
docker pull --quiet python:3.8.3-alpine
docker images
```

You will see there are vast differences between de-facto images and -slim and -alpine versions.

![docker-ps](https://miro.medium.com/max/700/1*_G4THS8_oj2ogauQ_kzPnA.png)

## A note on versions
Don’t ever use <image>:latest in a production Dockerfile. Doing this will always pull the latest image, and your application’s dependencies may not be compatible with future versions.

When starting a new project, I generally start with the most recent tagged version, test thoroughly and then upgrade as needed and test thoroughly before pushing to production.

