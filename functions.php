<?php
include_once('./simplehtmldom/simple_html_dom.php');
function GetStableVersion()
{
// create HTML DOM
    $html = file_get_html('http://www.kernel.org/kdist/version.shtml');
    foreach($html->find('tr') as $row) {
      foreach($row->find('td') as $td)
       {
        if ($td->innertext=='stable:')
        {
        	$kernel_version=$row->find('strong', 0)->innertext;
        	$ret = $kernel_version;
         	// clean up memory
        	$html->clear();
        	unset($html);
        	return $ret;
        }
        }
       }

}
function GetReleaseCandidateVersion()
{
  $html = file_get_html('http://www.kernel.org/kdist/version.shtml');
    foreach($html->find('tr') as $row) {
      foreach($row->find('td') as $td)
       {
        if ($td->innertext=='mainline:')
        {
        $kernel_version=$row->find('strong', 0)->innertext;
        $ret = $kernel_version;
         // clean up memory
        $html->clear();
        unset($html);
        return $ret;
        }
        }
       }

}
function getCpuCount()
{
  exec("grep -c  processor /proc/cpuinfo",$out);
  return $out[0];

}
?>
