<?
exec("grep -c  processor /proc/cpuinfo",&$out);
print $out[0]
?>
