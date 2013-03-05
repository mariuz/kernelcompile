#!/usr/bin/python
from subprocess import *
Popen("apt-get install git-core kernel-package fakeroot build-essential ncurses-dev python-pip wget",shell=True)
Popen("pip install feedparser",shell=True)
from functions.functions import *
BUILD_DIR="/usr/src"
kernel_version=GetStableVersion()
print(kernel_version)
cpuCount=getCpuCount()
print("cpu count:$cpuCount\n")
print("compiling kernel $kernel_version\n")

#chdir(BUILD_DIR)
#Popen("wget --continue http://kernel.org/pub/linux/kernel/v3.x/linux-$kernel_version.tar.bz2",shell=True)
#Popen("tar -jxf linux-$kernel_version.tar.bz2")
#chdir("linux-$kernel_version")
#Popen("cp /boot/config-`uname -r` ./.config")
#Popen("make menuconfig")
#Popen("make-kpkg clean")
#Popen("CONCURRENCY_LEVEL=$cpuCount fakeroot make-kpkg --initrd --append-to-version=-vanillaice kernel_image kernel_headers");
#Popen("make clean")
#Install(kernel_version)

