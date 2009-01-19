#!/usr/bin/php
<?
$kernel_version = "2.6.28";
$RcKernelVersion = "2.6.29-rc2";

chdir("/usr/src");
passthru("wget --continue http://kernel.org/pub/linux/kernel/v2.6/linux-$kernel_version.tar.bz2");
passthru("wget --continue http://www.kernel.org/pub/linux/kernel/v2.6/testing/patch-$RcKernelVersion.bz2");

passthru("tar -jxf linux-$kernel_version.tar.bz2");
passthru("bunzip2 patch-$RcKernelVersion.bz2");

chdir("linux-$kernel_version");
passthru("patch -p1 < ../patch-$RcKernelVersion");
chdir("..");

passthru("mv linux-$kernel_version linux-$RcKernelVersion");
chdir("linux-$RcKernelVersion");
passthru("cp /boot/config-`uname -r` ./.config");
passthru("make menuconfig");
passthru("make-kpkg clean");
passthru("fakeroot make-kpkg --initrd --append-to-version=-vanillaice kernel_image kernel_headers");
?>
