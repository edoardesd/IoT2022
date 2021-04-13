# Lesson 5

## [Thingspeak](https://thingspeak.com)

1. Create a channel with 2 fields

2. Update and read via MQTT ([docs](https://www.mathworks.com/help/thingspeak/mqtt-api.html))
  + Publish: `mosquitto_pub -h 'mqtt.thingspeak.com' -p '1883' -t 'channels/<channelID>/publish/<API_KEY>' -m 'field1=<VALUE>&field2=<VALUE>&status=MQTTPUBLISH'`
  + Subcribe: `mosquitto_sub -h mqtt.thingspeak.com -p 1883 -t channels/<channelID>/subscribe/fields/field1 -u <user.email> -P <MQTT_KEY>`

3. Update via HTTP
  + browser: `https://api.thingspeak.com/update?api_key=<API_KEY>&field1=<VALUE>`
  + Update via curl: `curl https://api.thingspeak.com/update\?api_key\=<API_KEY>\&field1\=<VALUE>`
  + Get last N values
  + Download CSV

  
#### Additional examples:
- `python3 thingspeak_requests.py`
- `python3 thingspeal_memory.py`
- `./thingspeak_memory.sh`

#### Interesting channels
- [Solar House](https://thingspeak.com/channels/34247)
- [Weather station](https://thingspeak.com/channels/895691)
- [My channels](https://bit.ly/2xQdEwx)

## [Node-Red](https://nodered.org/docs/getting-started/local)

1. Start node-red typing `node-red` on the terminal of your VM
2. Open the browser of the VM at: http://localhost:1880
- Hello World example
- [Random example](https://github.com/edoardesd/IoT2021/blob/master/lesson4/random-number)
- [Memory usage](https://github.com/edoardesd/IoT2021/blob/master/lesson4/node-red-exec-thingspeak): use the command `free -m | awk 'FNR==2 {print $4 "\n" $3}'`
- [Memory usage w/ dashboard](https://github.com/edoardesd/IoT2021/blob/master/lesson4/exec-dashboard-thingspeak) -> dashboard available at http://localhost:1880/ui
- [Data processing](https://github.com/edoardesd/IoT2021/blob/master/lesson5/node-red-alert_template)
