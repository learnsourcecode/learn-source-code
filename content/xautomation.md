Title: Xautomation
Date: 2015-01-04 06:12
Modified: 2015-01-04 06:12
Category: Linux
Tags: linux
Slug: xautomation
Authors: Vengatesh.S
<!-- Summary: KeyBinding for linux destro -->

Xautomation is a set of command lines programs to control X Window. It allows to controll the mouse movement, clicking, buttons, keys etc.

####Installation
* Add `deb http://ftp.de.debian.org/debian sid main` in your /etc/apt/sources.list
```
$ sudo apt-get update
$ sudo apt-get install xautomation
```

####To Run:
Example 1:
```
$ xte "key a"
```
Example 2:
```
$ xte "keydown Alt_L" "key F4" "keyup Alt_L"
```

####For Reference
* <http://linux.die.net/man/7/xautomation>
* <http://hoopajoo.net/projects/xautomation.html>
* <https://packages.debian.org/search?keywords=xautomation>