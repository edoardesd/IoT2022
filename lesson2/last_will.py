import paho.mqtt.client as mqtt
import time

mqttc = mqtt.Client()

lastwill_msg = "Error, smart bulb gone offline" # Last will message
topic = "room2/bulb"

mqttc.will_set(topic, lastwill_msg, qos=1 ,retain=False)
print("Setting Last will message --{}---, on topic {}".format(lastwill_msg, topic))

print("\nClient connected")
mqttc.connect("localhost", 1883)

mqttc.publish(topic, "bulb reading: ON")

time.sleep(500)