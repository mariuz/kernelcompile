#!/usr/bin/python
from subprocess import *
import os
import sys, getopt
from os import chdir
from functions.functions import *

def main(argv):
  opts, args = getopt.getopt(argv,"ht:v:b:",["help","type=","version=","build_method="])
  kernel_type = 'stable'
  build_method = 'debian'
  for opt, arg in opts:
      if opt in ("-h", "--help"):
         print 'kerenelcompile.py [-type <stable|mainline|longterm>] [-v <version>] [-b <normal|debian>]'
         sys.exit()
      elif opt in ("-t", "--type"):
         isValidKernelType = validate_kernel_type(arg)
         if(isValidKernelType == True):
             kernel_type = arg
         else:
             print("Invalid or No Kernel type entered")
             print("Valid options for the 'type' argument are : 'stable' or 'mainline' or 'longterm'\n")
             sys.exit()
      elif opt in ("-v", "--version"):
         kernel_version = arg
      elif opt in ("-b", "--build_method"):
         isValidBuildMethod = validate_build_method(arg)
         if(isValidBuildMethod == True):
             build_method = arg
         else:
             print("Invalid build_method entered")
             print("Valid options for the 'build_method' argument are  : 'debian' or 'normal'\n")
             sys.exit()
  call("apt-get install git-core kernel-package fakeroot build-essential libncurses5-dev python-pip wget xz-utils",shell=True)
  call("pip install feedparser sh",shell=True)
  from sh import cp,make,uname
  BUILD_DIR="/usr/src"
  testing=''
  if kernel_type == 'mainline':
    if kernel_version == None: # no version was suplied as arg
    	kernel_version=GetReleaseCandidateVersion()
    rc = kernel_version.find('-rc')
    if rc>0:
      testing = '/testing'
  else:
    if kernel_version == None:
    	kernel_version=GetStableVersion()
  cpuCount=getCpuCount()
  print("cpu count:%s\n" % cpuCount)
  print("compiling kernel %s\n" % kernel_version)

  chdir(BUILD_DIR)
  call("wget --continue http://kernel.org/pub/linux/kernel/v3.x%s/linux-%s.tar.xz" % (testing,kernel_version),shell=True)
  call("tar -Jxf linux-%s.tar.xz" % kernel_version,shell=True)
  chdir("linux-%s" % kernel_version)
  current_kernel=uname("-r").rstrip('\n')
  print("current kernel version is : %s\n" % current_kernel)
  # Start by cleaning up
  call("make distclean; make mrproper", shell=True)
  cp("/boot/config-%s"%current_kernel,"./.config")
  call("make nconfig",shell=True)
  if(build_method == 'debian'):
    print("Building by the Debian method")
    call("make-kpkg clean",shell=True)
    new_env = os.environ.copy()
    os.environ["CONCURENCY_LEVEL"] = "%s"% cpuCount
    call("fakeroot make-kpkg --initrd --append-to-version=-vanillaice kernel_image kernel_headers" ,shell=True)
    call("make clean",shell=True)
    Install(kernel_version)
  else:
    print("Building by the Normal method")
    # The below commands can be merged into one
    call("make", shell=True)
    call("make modules_install", shell=True)
    call("make install", shell=True)
  print("Done installing the Kernel\n")

if __name__ =="__main__":
  main(sys.argv[1:])
