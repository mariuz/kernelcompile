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
Popen("tar -jxf linux-%s.tar.bz2" % kernel_version,shell=True)
chdir("linux-%s" % kernel_version,shell=True)
Popen("cp /boot/config-`uname -r` ./.config",shell=True)
Popen("make menuconfig",shell=True)
Popen("make-kpkg clean",shell=True)
Popen("CONCURRENCY_LEVEL=%s fakeroot make-kpkg --initrd --append-to-version=-vanillaice kernel_image kernel_headers" % cpuCount,shell=True)
Popen("make clean",shell=True)
#Install(kernel_version)

