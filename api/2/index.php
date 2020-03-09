<?php
$db = new PDO("mysql:host=172.17.0.3;dbname=twitter", 'root', 'caseitau');  
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$db->exec("set names utf8"); //Garante UTF em versão < 5.3
$stmt = $db->query("
SELECT a.Hora, a.id_twitter AS 'Total'
  FROM
(
SELECT HOUR(t.created_at) AS Hora, COUNT(DISTINCT t.id_twitter ) AS id_twitter 
  FROM twitter.tweet t
GROUP BY HOUR(t.created_at)
) AS a
");
$total = $stmt->fetchAll(PDO::FETCH_OBJ);
print json_encode($total);
?> 