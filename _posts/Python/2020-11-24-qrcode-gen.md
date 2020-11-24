---
layout: post
title: "[Python] QR Code Generator"
date: 2020-11-24 23:11
category: Python
tags: [python,]

---
# QR CODE GENERATOR

![QR CODE Gen](https://www.codesnail.com/wp-content/uploads/2020/07/qr-code-generator-in-python-768x432.png)

# 테스트 환경
- 운영체제 : Windows 10
- 파이썬 버전 : 3.8.6
- 필요 라이브러리 : pillow + qrcode


# 다운로드 
```
pip install qrcode[pil]
pip install image
```
# Source Code

## 방법1

```
import qrcode

qr = qrcode.make('hello world')
qr.save('myQR.png')


```

## 방법2

```
qr = qrcode.QRCode(
    version=1, # very smallest size
    box_size=15,
    border=5 
)

data = r'https://hyeseong-dev.github.io/'
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('My-Blog-QR-Code.png')

# the version parameter takes an integer from 1~40 to controls the size of the QR Code. 
# The smaller the numer the smaller the QR code size is going to be

'''
# The Following 4 constants are made available on the qrcode package:
# ERROR_CORRECT_L
#   About 7% or less errors can be corrected.
# 
# ERROR_CORRECT_M(default) 
#   About 15% or less ...

# ERROR_CORRECT_Q(default) 
#   About 25% or less ...

# ERROR_CORRECT_H(default) 
#   About 35% or less ...
```