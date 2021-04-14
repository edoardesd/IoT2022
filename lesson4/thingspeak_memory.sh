#!/bin/bash

echo "Hello!"
apiKey=XXXXXXXXXXXXXXXXXXXXXX

while :
do
	free=$(free -m | awk 'FNR==2 {print $4}')
	used=$(free -m | awk 'FNR==2 {print $3}')
	echo -e "\nfree mem: $free, used mem: $used"
	curl --silent --request POST --header "X-THINGSPEAKAPIKEY: $apiKey" --data "field1=$free&field2=$used" "http://api.thingspeak.com/update.json"
	sleep 20
done