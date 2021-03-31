#!/usr/bin/env python3
"""a simple sensor data generator that sends to an MQTT broker via paho"""
import json
import random
import string
import sys
import time

import multiprocessing as mp
import paho.mqtt.client as mqtt

from itertools import permutations 


def random_string(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def generate(host, port, username, password, topic, sensors, interval_ms, verbose, all_topics):
    mqttc = mqtt.Client(protocol=random.choice([mqtt.MQTTv31, mqtt.MQTTv311, mqtt.MQTTv5]))

    if host == "localhost":
        if username:
            mqttc.username_pw_set(username, password)

    if random.randint(0, 100) < 28:
        mqttc.will_set(topic, "error: {}".format(random_string(8)), qos=random.choice([0,1,2]), retain=False)
    

    mqttc.connect(host, port, keepalive=random.randint(10, 600))

    topic_sub = random.choices(all_topics, k=random.randint(0, 3))
    for t in topic_sub:
        mqttc.subscribe(t, random.choice([0,1,2]))

    keys = list(sensors.keys())
    interval_secs = interval_ms / 1000.0

    while True:
        sensor_id = random.choice(keys)
        sensor = sensors[sensor_id]
        min_val, max_val = sensor.get("range")
        val = random.randint(min_val, max_val)

        data = {
            "id": sensor_id,
            "value": val
        }

        for key in ["lat", "lng", "unit", "type"]:
            value = sensor.get(key)

            if value is not None:
                data[key] = value

        payload = json.dumps(data)

        if verbose:
            print("{} -- {}: {}".format(host, topic, payload))

        mqttc.publish(topic, payload, qos=random.choice([0,1,2]), retain=random.choice([True, False]))
        time.sleep(random.randint(interval_secs-4, interval_secs+100))

        if random.randint(0, 100) > 90:
            mqttc.reinitialise()

        if random.randint(0, 100) < 10:
            mqttc.disconnect()
            time.sleep(random.randint(0, 10))
            mqttc.connect(host, port)



def main(config_path):
    """main entry point, load and validate config and call generate"""
    try:
        with open(config_path) as handle:
            config = json.load(handle)
            mqtt_config = config.get("mqtt", {})
            misc_config = config.get("misc", {})
            sensors = config.get("sensors")

            interval_ms = misc_config.get("interval_ms", 500)
            verbose = misc_config.get("verbose", False)

            if not sensors:
                print("no sensors specified in config, nothing to do")
                return

            host = mqtt_config.get("host", "localhost")
            port = mqtt_config.get("port", 1883)
            username = mqtt_config.get("username")
            password = mqtt_config.get("password")
            topic = mqtt_config.get("topic", "mqttgen")

            # generate(host, port, username, password, topic, sensors, interval_ms, verbose)

            with mp.Pool(processes=len(topic)) as pool:
                n_results = pool.starmap(generate, [(random.choice(host), port, random.choice(username), random.choice(password), t, sensors, interval_ms, verbose, topic) for t in topic])


    except IOError as error:
        print("Error opening config file '%s'" % config_path, error)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print("usage %s config.json" % sys.argv[0])