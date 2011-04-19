#!/usr/bin/php
<?
$KERNEL_URL='http://www.kernel.org/';
include_once('./getKernelVersion.php');
include_once('./getCpuCount.php');

$ReleaseCandidateVersion=GetReleaseCandidateVersion($KERNEL_URL);
$cpuCount=getCpuCount();
print("cpu count:$cpuCount\n");
print("compiling kernel $ReleaseCandidateVersion\n");

passthru("apt-get install kernel-package git-core fakeroot ncurses-dev");

chdir("/usr/src");
passthru("wget --continue http://www.kernel.org/pub/linux/kernel/v2.6/testing/linux-$ReleaseCandidateVersion.tar.bz2");

passthru("tar -jxf linux-$ReleaseCandidateVersion.tar.bz2");

chdir("linux-$ReleaseCandidateVersion");
passthru("cp /boot/config-`uname -r` ./.config");
passthru("make menuconfig");
passthru("make-kpkg clean");
passthru("CONCURRENCY_LEVEL=$cpuCount fakeroot make-kpkg --initrd --append-to-version=-vanillaice kernel_image kernel_headers");
?>
