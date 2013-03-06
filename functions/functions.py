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
    Popen("dpkg -i /usr/src/linux-image-kernel_version-vanillaice_kernel_version-vanillaice-10.00.Custom_amd64.deb", shell=True)
    Popen("dpkg -i /usr/src/linux-headers-kernel_version-vanillaice_kernel_version-vanillaice-10.00.Custom_amd64.deb",shell=True)
