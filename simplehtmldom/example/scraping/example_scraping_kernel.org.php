<?php
include_once('../../simple_html_dom.php');

function stable_kernel() {
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
    
function mainline_kernel() {
    // create HTML DOM
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
 


// -----------------------------------------------------------------------------
// test it!


$stable_kernel = stable_kernel();
echo "Stable kernel=$stable_kernel\n";

$mainline_kernel = mainline_kernel();
echo "Mainline kernel=$mainline_kernel\n";



?>
