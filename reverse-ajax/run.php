<?php
# curl -X POST --data "data='LANDLORDS'" http://localhost:8989/run.php
# php -S localhost:8989

header("Access-Control-Allow-Origin: *");

$post_body = file_get_contents('php://input');

echo "FETCHING";
flush();
ob_flush();    
sleep(1);

if ($post_body == 'LANDLORDS')
{
    for ($i = 1; $i <= 10; $i++)
    {
        echo "LANDLORD : $i";
        flush();
        ob_flush();    
        sleep(1);
    }
}

if ($post_body == 'TENANTS')
{
    for ($i = 1; $i <= 10; $i++)
    {
        echo "TENANTS : $i";
        flush();
        ob_flush();    
        sleep(1);
    }
}

echo "DONE";
?>