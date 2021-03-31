import requests
import time


from random import randint, choice, choices

api_list = ['https://api.github.com', 'https://api.publicapis.org/', 'https://http.cat/{}'.format(randint(100, 500)), 'https://dog.ceo/api/breeds/image/random', 
            'http://placegoat.com/200', 'https://aws.random.cat/meow', 'https://random.dog/woof.json', 'https://randomfox.ca/floof/', 'https://api.jikan.moe/v3/search/anime?q=dragonball&limit=16', ' https://api.jikan.moe/v3/search/anime?q=naruto&limit=16',
            'https://api.lyrics.ovh/v1/prodigy/invaders_must_die', 'https://api.lyrics.ovh/v1/idles/danny_nedelko', 'https://api.lyrics.ovh/v1/ministri/noi_fuori', 'https://picsum.photos/200/300']

def main():
    while True:
        response = requests.get(choice(api_list))
        print(response.content)
        time.sleep(randint(3, 20))


if __name__ == '__main__':
    main()