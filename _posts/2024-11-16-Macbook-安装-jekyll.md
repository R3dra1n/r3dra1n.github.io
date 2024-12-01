---
layout: post
title: Macbook 安装 jekyll 
date:   2024-11-15 17:22:52 +0800
categories: MacBook 
Tags: Macbook jekyll AppleM芯片 Blog
---

# 背景

- 时间：2024.11.01
- 芯片：Apple M3
- MacOS：Sequoia 15.1

# 过程

根据 jekyll 官方的指示，直接使用命令安装

```bash
gem install jekyll
```



安装完之后，出现问题

```bash
jekyll -v
zsh: command not found: jekyll
```



解决方法

大概率是安装路径问题，而且应该是在Apple芯片的机型上，默认安装路径导致的问题，吉安装路径不在系统的PATH环境变量中。

1. 找到路径

	```bash
	#首先确认环境
	gem env
	```

	在输出的内容中找到 GEM PATHS 下的路径，显示如下

	```bash
   - GEM PATHS:
       - /opt/homebrew/lib/ruby/gems/3.3.0
       - /Users/william/.gem/ruby/3.3.0
       - /opt/homebrew/Cellar/ruby/3.3.6/lib/ruby/gems/3.3.0
   ```


2. 将路径添加到PATH


      1. 打开.zshrc
    
         ```bash
         open ~/.zshrc
         ```
    
      1. 在文件内添加以下。（路径名为步骤1找到的路径）
    
         ```bash
         export PATH="/opt/homebrew/lib/ruby/gems/3.3.0/bin:$PATH"
         ```
    
      3. 保存后退出

3. 重新加载 .zshrc

   ```bash
   source ~/.zshrc
   ```

   

3. 验证

   ```bash
   jekyll -v
   jekyll 4.3.4
   ```



成功了~！
