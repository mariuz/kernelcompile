<?php
function getCpuCount()
{
  exec("grep -c  processor /proc/cpuinfo",&$out);
  return $out[0];

}
?>
