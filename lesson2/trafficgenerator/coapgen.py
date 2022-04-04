import random
import subprocess
import time

import multiprocessing as mp

from random import randint, choice, choices


local_urls = ['/basic', '/living_room/door', '/main_door', '/living_room/temperature', '/living_room', '/hello_world', '/', '/hello_post', '/dining_room/door', '/dining_room/temperature', '/dining_room', '/test']
coapme_urls = ['/test', '/validate', '/hello', '/sink', '/separate', '/large', '/secret', '/broken', '/weird', '/weird44', '/weird33', '/weird55', '/weird333', '/location-query', '/large-create', '/query', '/seg1', '/path', '/location1', '/multi-format', '/3', '/4', '/5']
californium_urls = ['/create1', '/large', '/large-create', '/large-create/{}'.format(random.randint(1,30)), '/large-post', '/large-separate', '/large-update', '/link1', '/link2', '/location-query', '/obs', '/obs-large', '/obs-pumping']

def random_string(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def generate(url, server_type):

    url = "/usr/local/bin/coap {} {}".format(choice(['get', 'post', 'put', 'delete']), url)

    if randint(1, 100) < 10 and "get" in url:
        url += " -o"

    if randint(1, 100) > 50:
        url += " -c"

    url += " -b " + str(randint(1,6))

    print(url)
    while True:
        subprocess.Popen(url, shell=True)
        time.sleep(randint(3, 27))

        if server_type == "localhost" and "door" in url:
            if "post" in url:
                url = url + "?create -p " + random_string(randint(3))

            if "put" in url:
                url = url + "?status/  " + choice(['closed', 'open', 'none', 'ajar'])





def main():

    hostname = choice(["coap://0.0.0.0:5683", "coap://coap.me" ,"coap://californium.eclipse.org"])
    port = 5683

    if hostname == "coap://0.0.0.0:5683":
        topic_url = local_urls
        server_type = "localhost"

    if hostname == "coap://coap.me":
        topic_url = coapme_urls
        server_type = "coapme"


    if hostname == "coap://californium.eclipse.org":
        topic_url = californium_urls
        server_type = "californium"


    url_list = choices(topic_url, k=randint(3, 9))
    print(url_list)
    with mp.Pool(processes=len(url_list)) as pool:
        n_results = pool.starmap(generate, [("{}{}".format(hostname, url), server_type) for url in url_list])


if __name__ == '__main__':
    main()