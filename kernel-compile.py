#!/usr/bin/python
from subprocess import *
from os import chdir
Popen("apt-get install git-core kernel-package fakeroot build-essential ncurses-dev python-pip wget",shell=True)
Popen("pip install feedparser",shell=True)
from functions.functions import *
BUILD_DIR="/usr/src"
kernel_version=GetStableVersion()
cpuCount=getCpuCount()
print("cpu count:%s\n" % cpuCount)
print("compiling kernel %s\n" % kernel_version)

chdir(BUILD_DIR)
Popen("wget --continue http://kernel.org/pub/linux/kernel/v3.x/linux-%s.tar.bz2" % kernel_version,shell=True)
#Popen("tar -jxf linux-$kernel_version.tar.bz2")
#chdir("linux-$kernel_version")
#Popen("cp /boot/config-`uname -r` ./.config")
#Popen("make menuconfig")
#Popen("make-kpkg clean")
#Popen("CONCURRENCY_LEVEL=$cpuCount fakeroot make-kpkg --initrd --append-to-version=-vanillaice kernel_image kernel_headers");
#Popen("make clean")
#Install(kernel_version)

