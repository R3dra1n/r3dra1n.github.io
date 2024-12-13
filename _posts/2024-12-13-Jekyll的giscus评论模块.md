---
layout: post
title: Jekyll的giscus评论模块
date: 2024-12-13 15:22:52 +0800
description: jekyll创建的blog，用giscus模块增加评论模块
categories: Blog
tags: MacBook AppleM芯片 Jekyll giscus
---

## 一、背景

- 时间：2024.12.13
- 芯片：Apple M3
- MacOS：Sequoia 15.1



## 二、giscus介绍

利用 [GitHub Discussions](https://docs.github.com/en/discussions) 实现的评论系统，让访客借助 GitHub 在你的网站上留下评论和反应！





## 三、giscus代码获取和jekyll配置

### 3.1 giscus代码获取

[官方网站](https://giscus.app/zh-TW) ，在网站中，根据相应的内容进行选择。

> 记得这三个一定要做，不然会失败
 {: .prompt-warning }

![image-20241213153510742](/assets/img/3.png)



> 第三个，启用之后，要到github页面上发个第一篇，好像才能work
>{: .prompt-tip}

前面全部填好之后，下面会自动生成好giscus的代码

```bash
<script src="https://giscus.app/client.js"
        data-repo="[在此输入仓库]"
        data-repo-id="[在此输入仓库 ID]"
        data-category="[在此输入分类名]"
        data-category-id="[在此输入分类 ID]"
        data-mapping="pathname"
        data-strict="0"
        data-reactions-enabled="1"
        data-emit-metadata="0"
        data-input-position="bottom"
        data-theme="preferred_color_scheme"
        data-lang="zh-CN"
        crossorigin="anonymous"
        async>
</script>
```



### 3.2 jekyll的giscus代码填入







 















