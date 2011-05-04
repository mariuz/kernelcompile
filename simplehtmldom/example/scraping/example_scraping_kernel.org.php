<?php
include_once('../../simple_html_dom.php');

function scraping_kernel() {
    // create HTML DOM
    $html = file_get_html('http://www.kernel.org/kdist/version.shtml');
    foreach($html->find('tr') as $row) {
     $kernel_version=$row->find('strong', 0)->innertext;
        $ret[] = $kernel_version;
    }
    
    // clean up memory
    $html->clear();
    unset($html);

    return $ret;
}


// -----------------------------------------------------------------------------
// test it!


$ret = scraping_kernel();

foreach($ret as $v) {
    echo $v;
}

?>
