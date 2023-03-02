<?php
# curl -X POST --data "data='LANDLORDS'" http://localhost:8989/run.php

header("Access-Control-Allow-Origin: *");

echo "START";

print_r($_POST); die();

if ($_POST['data'] == 'LANDLORDS')
{
    for ($i = 1; $i <= 10; $i++)
    {
        echo "LANDLORD : $i";
        flush();
        ob_flush();    
        sleep(1);    
    }
}

echo "END";
?>