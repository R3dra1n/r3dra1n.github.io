---
layout: post
title: Streamlit 应用和Demo
date: 2024-12-12 15:22:52 +0800
description: Streamlit的代码和前端demo
categories: Streamlit 
tags: MacBook AppleM芯片 Streamlit 前端界面
---

# 一、背景

- 时间：2024.12.12
- 芯片：Apple M3
- MacOS：Sequoia 15.1



# 二、Streamlit的使用

Streamlit是一个简单实用的python库，可以简单的让py文件有前端界面可以展示。



## 2.1 运行

在终端或者命令行中运行已经写好的.py文件，

```bash
streamlit run demo.py
```



# 三、Streamlit的功能和代码

## 3.1 开始使用

``` bash
import streamlit as st

# 设置页面标题
st.title('Streamlit的功能和demo')

# 输出一行文字
st.write("欢迎使用Streamlit！")
```

![image-20241212193627795](/Users/william/myblog/assets/img/1.png)

## 3.2 文字的输入

``` bash
import streamlit as st

# 设置页面标题
st.title('Streamlit的功能和demo')

# 输出一行文字
st.write("欢迎使用Streamlit！")

name = st.text_input("输入名字：")
add = st.text_area("输入地址")
st.write(f"Hi {name}!, 您住的地方是{add}")
```

![image-20241212203130075](/Users/william/myblog/assets/img/2.png)





 















