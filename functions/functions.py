from feedparser import *
from subprocess import *
def GetStableVersion():
    feed = parse('https://www.kernel.org/feeds/kdist.xml')
    for item in feed.entries:           
        if (item.title.count('stable')==1):        
        	kernel_version=item.title.split(':')[0]        	         	
        	return kernel_version

def GetReleaseCandidateVersion():
    feed = parse('https://www.kernel.org/feeds/kdist.xml')
    for item in feed.entries:           
        if (item.title.count('mainline')==1):        
            kernel_version=item.title.split(':')[0]                         
            return kernel_version

def getCpuCount():
    out=check_output("grep -c  processor /proc/cpuinfo",shell=True)
    return out

def Install(kernel_version):
    sub="."
    count_dots=kernel_version.count(sub,0,len(kernel_version))
    if count_dots==1:
        kernel_version=kernel_version+".0"
    call("dpkg -i /usr/src/linux-image-%s-vanillaice_%s-vanillaice-10.00.Custom_amd64.deb" % (kernel_version,kernel_version), shell=True)
    call("dpkg -i /usr/src/linux-headers-%s-vanillaice_%s-vanillaice-10.00.Custom_amd64.deb" % (kernel_version,kernel_version), shell=True)
