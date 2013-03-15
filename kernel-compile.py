#!/usr/bin/python
from subprocess import *
from os import chdir
from sh import cp,make,uname
call("apt-get install git-core kernel-package fakeroot build-essential libncurses5-dev python-pip wget",shell=True)
call("pip install feedparser",shell=True)
from functions.functions import *
BUILD_DIR="/usr/src"
kernel_version=GetStableVersion()
cpuCount=getCpuCount()
print("cpu count:%s\n" % cpuCount)
print("compiling kernel %s\n" % kernel_version)

chdir(BUILD_DIR)
call("wget --continue http://kernel.org/pub/linux/kernel/v3.x/linux-%s.tar.bz2" % kernel_version,shell=True)
call("tar -jxf linux-%s.tar.bz2" % kernel_version,shell=True)
chdir("linux-%s" % kernel_version)
current_kernel=uname("-r").rstrip('\n')
cp("/boot/config-%s"%current_kernel,"./.config")
call("make nconfig",shell=True)
call("make-kpkg clean",shell=True)
call("CONCURRENCY_LEVEL=%s fakeroot make-kpkg --initrd --append-to-version=-vanillaice kernel_image kernel_headers" % cpuCount,shell=True)
call("make clean",shell=True)
Install(kernel_version)
