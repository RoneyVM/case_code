<?php
$db = new PDO("mysql:host=172.17.0.3;dbname=twitter", 'root', 'caseitau');  
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$db->exec("set names utf8"); //Garante UTF em versão < 5.3
$stmt = $db->query("
SELECT hashtag, lang, COUNT(hashtag) FROM twitter.tweet GROUP BY lang, hashtag
");
$users = $stmt->fetchAll(PDO::FETCH_OBJ);
print json_encode($users);
?> 