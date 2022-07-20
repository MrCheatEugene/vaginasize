<?php
// Добавьте в Cron
$json = json_decode(file_get_contents("usersDB.json"),true);
if(!is_null($json)){
	$keys=  array_keys($json);
	var_dump($keys);
	var_dump($json);
	$foolOfDay = '@'.$keys[array_rand($keys)];
	$fPair= '@'.$keys[array_rand($keys)];
	$sPair= '@'.$keys[array_rand($keys)];
	$pairOfDay = $fPair.' {ANDSIGN} '.$sPair;
	$nicestOfDay = '@'.$keys[array_rand($keys)];
	if($fPair == $sPair){
		while ($fPair == $sPair) {
			$fPair= '@'.$keys[array_rand($keys)];
			$sPair= '@'.$keys[array_rand($keys)];
		}
	$pairOfDay = $fPair.' {ANDSIGN} '.$sPair;
	}
	file_put_contents("foolOfDay", $foolOfDay);
	file_put_contents("pairOfDay", $pairOfDay);
	file_put_contents("nicestOfDay", $nicestOfDay);
}
$newJson = $json;
foreach ($json as $key => $value) {
	$newJson[$key] = $value = array();
}
unlink("usersDB.json");
file_put_contents("usersDB.json",json_encode($newJson,JSON_UNESCAPED_UNICODE));
