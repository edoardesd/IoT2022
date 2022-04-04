import subprocess
import string
import time

import paho.mqtt.client as mqtt

from random import randint, choice, choices


def random_topics():
    return ["{}/{}/{}/{}".format(choice(first_level), choice(second_level), choice(third_level), choice(fourth_level)) for i in range(randint(1, 20))]

def random_string(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(choice(letters) for i in range(stringLength))

host = ["localhost", "test.mosquitto.org", "mqtt.eclipse.org", "broker.hivemq.com"]

first_level = ['factory', 'house', 'university', random_string(10), '', '#']
second_level = ['department{}'.format(randint(0,10)), 'building{}'.format(randint(0,10)), 'facility{}'.format(randint(0,10)), 'room{}'.format(randint(0,10)), random_string(10), '', '+', '#']
third_level = ['room{}'.format(randint(0,10)), 'floor{}'.format(randint(0,10)), 'area{}'.format(randint(0,10)), 'section{}'.format(randint(0,10)), '#', '+']
fourth_level = ['temperature', 'humidity', 'light', 'pollution', 'hydraulic_valve', 'deposit', '', '+', '#']

def main():
    mqttc = mqtt.Client(random_string(randint(1,20)), protocol=choice([mqtt.MQTTv31, mqtt.MQTTv311, mqtt.MQTTv5]))

    if host == "localhost":
        if username:
            mqttc.username_pw_set(random_string(randint(1,20)), random_string(randint(1,10)))


    mqttc.connect(choice(host), 1883, keepalive=randint(10, 600))

    topic_sub = choices(random_topics(), k=randint(0, 23))
    print(topic_sub)

    for t in topic_sub:
        try:
            mqttc.subscribe(t, choice([0,1,2]))
        except ValueError:
            pass

    mqttc.loop_forever()

if __name__ == '__main__':
    main()