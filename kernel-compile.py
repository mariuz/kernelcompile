#!/usr/bin/python
from subprocess import *
import os
import sys, getopt
from os import chdir
from functions.functions import *

def validate_kernel_type(kernel_type):
  if(len(kernel_type) > 0):
    if ((kernel_type == "stable") or (kernel_type == "mainline") or (kernel_type == "lts")):
      return True
    else:
      return False
  else:
    return False

def main(argv):
  opts, args = getopt.getopt(argv,"ht:v:",["help","type=","version="])
  kernel_type = 'stable'
  for opt, arg in opts:
      #if opt == '-h':
      if opt in ("-h", "--help"):
         print 'kerenelcompile.py -type <stable|mainline|lts> -v <version>'
         sys.exit()
      elif opt in ("-t", "--type"):
         isValidKernelType = validate_kernel_type(arg)
         if(isValidKernelType == True):
             kernel_type = arg
         else:
             print("Invalid or No Kernel type entered")
             print("Valid options for the 'type' argument are : 'stable' or 'mainline' or 'lts'\n")
             sys.exit()
      elif opt in ("-v", "--version"):
         version = arg
  call("apt-get install git-core kernel-package fakeroot build-essential libncurses5-dev python-pip wget xz-utils",shell=True)
  call("pip install feedparser sh",shell=True)
  from sh import cp,make,uname
  BUILD_DIR="/usr/src"
  testing=''
  if kernel_type == 'mainline':
    kernel_version=GetReleaseCandidateVersion()
    rc = kernel_version.find('-rc')
    if rc>0:
      testing = '/testing'
  else:
    kernel_version=GetStableVersion()
  cpuCount=getCpuCount()
  print("cpu count:%s\n" % cpuCount)
  print("compiling kernel %s\n" % kernel_version)

  chdir(BUILD_DIR)
  call("wget --continue http://kernel.org/pub/linux/kernel/v3.x%s/linux-%s.tar.xz" % (testing,kernel_version),shell=True)
  call("tar -Jxf linux-%s.tar.xz" % kernel_version,shell=True)
  chdir("linux-%s" % kernel_version)
  current_kernel=uname("-r").rstrip('\n')
  cp("/boot/config-%s"%current_kernel,"./.config")
  call("make nconfig",shell=True)
  call("make-kpkg clean",shell=True)
  new_env = os.environ.copy()
  os.environ["CONCURENCY_LEVEL"] = "%s"% cpuCount
  call("fakeroot make-kpkg --initrd --append-to-version=-vanillaice kernel_image kernel_headers" ,shell=True)
  call("make clean",shell=True)
  Install(kernel_version)

if __name__ =="__main__":
  main(sys.argv[1:])
