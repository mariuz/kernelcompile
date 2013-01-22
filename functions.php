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
function Install($kernel_version)
{
passthru("dpkg -i /usr/src/linux-image-$kernel_version-vanillaice_$kernel_version-vanillaice-10.00.Custom_amd64.deb");
passthru("dpkg -i /usr/src/linux-headers-$kernel_version-vanillaice_$kernel_version-vanillaice-10.00.Custom_amd64.deb");
}

?>
