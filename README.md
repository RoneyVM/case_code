# case_code


Estrutura da Pasta

opt
  |- itau
        |- APP
             
         




Deploy
	
Aplicação: roneymoreira/case-app:1.0 (172.17.0.2)
Comandos
#Iniciando
docker run --privileged -v /etc/hosts:/etc/hosts -v /opt/itau/html:/var/www/html \
-v /opt/itau/APP:/APP -itd -p 80:80 -p 10050 --name app roneymoreira/case-app:1.0 /bin/bash;
#Iniciando o Serviço app
docker exec $(docker ps | grep "case-itau-roney-app" | awk '{print $1}') /etc/init.d/apache2 start; 
docker exec $(docker ps | grep "case-itau-roney-app" | awk '{print $1}') /etc/init.d/zabbix-agent start; 
docker exec $(docker ps | grep "case-itau-roney-app" | awk '{print $1}') /etc/init.d/filebeat start; 

	Banco de Dados: roneymoreira/case-sql:1.0 (172.17.0.3)
Comandos
#Iniciando
docker run --privileged -v /etc/hosts:/etc/hosts -itd -p 3306:3306 -p 10050 --name sql \ roneymoreira/case-sql:1.0 /bin/bash;
#Iniciando o Serviço sql
docker exec $(docker ps | grep "case-itau-roney-sql" | awk '{print $1}') /etc/init.d/mysql start;
docker exec $(docker ps | grep "case-itau-roney-sql" | awk '{print $1}') /etc/init.d/zabbix-agent start; 

	Monitoração / Métricas: roneymoreira/case-mon:1.0 (172.17.0.4)
Comandos
#Iniciando
docker run --privileged -v /etc/hosts:/etc/hosts -itd -p 8080:8080 -p 10050 -p 3000:3000 --name mon \
 roneymoreira/case-mon:1.0 /bin/bash;
#Iniciando o Serviço mon
docker exec $(docker ps | grep "case-itau-roney-mon" | awk '{print $1}') /etc/init.d/apache2 start; 
docker exec $(docker ps | grep "case-itau-roney-mon" | awk '{print $1}') /etc/init.d/zabbix-server start; 
docker exec $(docker ps | grep "case-itau-roney-mon" | awk '{print $1}') /etc/init.d/zabbix-agent start; 
docker exec $(docker ps | grep "case-itau-roney-mon" | awk '{print $1}') /etc/init.d/grafana-server start; 

	Loggings: roneymoreira/case-log:1.0 (172.17.0.5)
Comandos
#Iniciando
docker run --privileged -v /etc/hosts:/etc/hosts -itd -p 5601:5601 -p 10050 -p 9200:9200 \
-p 9300:9300 --name log case-itau-roney-log:1.0 /bin/bash;
#Iniciando o Serviço log
docker exec $(docker ps | grep "case-itau-roney-log" | awk '{print $1}') /etc/init.d/zabbix-agent start; 
docker exec $(docker ps | grep "case-itau-roney-log" | awk '{print $1}') /etc/init.d/elasticsearch start; 
docker exec $(docker ps | grep "case-itau-roney-log" | awk '{print $1}') /etc/init.d/kibana start; 
