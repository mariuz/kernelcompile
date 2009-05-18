#!/usr/bin/php
<?
DEFINE(KERNEL_URL,'http://www.kernel.org/');
include_once('./getKernelVersion.php');
$kernel_version=GetStableVersion(KERNEL_URL);
print ("installing kernel $kernel_version");
passthru("apt-get install kernel-package git-core fakeroot ncurses-dev");
chdir("/usr/src");
passthru("wget --continue http://kernel.org/pub/linux/kernel/v2.6/linux-$kernel_version.tar.bz2");
passthru("tar -jxf linux-$kernel_version.tar.bz2");
chdir("linux-$kernel_version");
passthru("cp /boot/config-`uname -r` ./.config");
passthru("make menuconfig");
passthru("make-kpkg clean");
passthru("fakeroot make-kpkg --initrd --append-to-version=-vanillaice kernel_image kernel_headers");
?>
