#!/usr/bin/php
<?
$KERNEL_URL='http://www.kernel.org/';
$BUILD_DIR="/usr/src";
include_once('./getKernelVersion.php');
include_once('./getCpuCount.php');

$kernel_version=GetStableVersion($KERNEL_URL);
$cpuCount=getCpuCount();
print("cpu count:$cpuCount\n");
print("compiling kernel $kernel_version\n");
passthru("apt-get install kernel-package git-core fakeroot ncurses-dev");
chdir($BUILD_DIR);
passthru("wget --continue http://kernel.org/pub/linux/kernel/v3.0/linux-$kernel_version.tar.bz2");
passthru("tar -jxf linux-$kernel_version.tar.bz2");
chdir("linux-$kernel_version");
passthru("cp /boot/config-`uname -r` ./.config");
passthru("make menuconfig");
passthru("make-kpkg clean");
passthru("CONCURRENCY_LEVEL=$cpuCount fakeroot make-kpkg --initrd --append-to-version=-vanillaice kernel_image kernel_headers");
passthru("make clean");
?>
