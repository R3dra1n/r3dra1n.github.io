---

layout: post
title: Macbook 安装 Ruby
date:   2024-11-17 17:22:52 +0800
description: MacOS 已经有内建 Ruby，但是版本不够，需要额外安装新的版本。
categories: Apple MacBook 
tags: MacBook Ruby AppleM芯片 Blog

---

## 一、背景

- 时间：2024.11.17
- 芯片：Apple M3
- MacOS：Sequoia 15.1



## 二、问题

MacOS 已经有内建 Ruby，但是版本不够，需要额外安装新的版本。查看现有版本，在terminal输入：

```bash
#查看现有版本
ruby -v
ruby 2.6.10p210 (2022-04-12 revision 67958) [universal.arm64e-darwin24]
```



## 三、解决方法

使用 brew 安装 ruby

```bash
brew install ruby
==> Fetching dependencies for ruby: libyaml
==> Fetching libyaml
==> Downloading https://mirrors.ustc.edu.cn/homebrew-bottles/bottles/libyaml-0.2.5.arm64_sequoia.bottle.tar.gz
Already downloaded: /Users/william/Library/Caches/Homebrew/downloads/08f41e0727bddedfe3994d0d9db32b07a252ea3af3c4f4fa321d784ebf15cf84--libyaml-0.2.5.arm64_sequoia.bottle.tar.gz
==> Fetching ruby
==> Downloading https://mirrors.ustc.edu.cn/homebrew-bottles/bottles/ruby-3.3.6.arm64_sequoia.bottle.tar.gz
Already downloaded: /Users/william/Library/Caches/Homebrew/downloads/920ae03bfba71052a99f5b01a8d489245c23e2ca393e5d1ea263185fca9bebc9--ruby-3.3.6.arm64_sequoia.bottle.tar.gz
==> Installing dependencies for ruby: libyaml
==> Installing ruby dependency: libyaml
==> Pouring libyaml-0.2.5.arm64_sequoia.bottle.tar.gz
🍺  /opt/homebrew/Cellar/libyaml/0.2.5: 11 files, 354.5KB
==> Installing ruby
==> Pouring ruby-3.3.6.arm64_sequoia.bottle.tar.gz
==> Caveats
By default, binaries installed by gem will be placed into:
  /opt/homebrew/lib/ruby/gems/3.3.0/bin

You may want to add this to your PATH.

ruby is keg-only, which means it was not symlinked into /opt/homebrew,
because macOS already provides this software and installing another version in
parallel can cause all kinds of trouble.

If you need to have ruby first in your PATH, run:
  echo 'export PATH="/opt/homebrew/opt/ruby/bin:$PATH"' >> ~/.zshrc

For compilers to find ruby you may need to set:
  export LDFLAGS="-L/opt/homebrew/opt/ruby/lib"
  export CPPFLAGS="-I/opt/homebrew/opt/ruby/include"
==> Summary
🍺  /opt/homebrew/Cellar/ruby/3.3.6: 19,890 files, 51.7MB
==> Running `brew cleanup ruby`...
Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
==> Caveats
==> ruby
By default, binaries installed by gem will be placed into:
  /opt/homebrew/lib/ruby/gems/3.3.0/bin

You may want to add this to your PATH.

ruby is keg-only, which means it was not symlinked into /opt/homebrew,
because macOS already provides this software and installing another version in
parallel can cause all kinds of trouble.

If you need to have ruby first in your PATH, run:
  echo 'export PATH="/opt/homebrew/opt/ruby/bin:$PATH"' >> ~/.zshrc

For compilers to find ruby you may need to set:
  export LDFLAGS="-L/opt/homebrew/opt/ruby/lib"
  export CPPFLAGS="-I/opt/homebrew/opt/ruby/include"
```

安装以后，看到提示信息，需要调整path变量，先再看一下 ruby 版本

```bash
ruby -v
ruby 2.6.10p210 (2022-04-12 revision 67958) [universal.arm64e-darwin24]
```

会发现还是内建版本。因此在 terminal输入

```bash
echo 'export PATH="/opt/homebrew/opt/ruby/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

之后再看一次 ruby 版本

```bash
ruby -v
ruby 3.3.6 (2024-11-05 revision 75015d4c1f) [arm64-darwin24]
```

