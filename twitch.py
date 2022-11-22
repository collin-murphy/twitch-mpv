#imports
from subprocess import DEVNULL, STDOUT, check_call
from bs4 import BeautifulSoup
import requests as rq

def check_live(URL: str):
    request = rq.get(URL)
    soup = BeautifulSoup(request.text, "html.parser")
    print(soup)

def main():
    streamer = input('type a streamer name:')

    link = f'http://www.twitch.tv/{streamer}'
    check_live(link)

    print(f'Opening {link}') 

    check_call(['mpv', link], stdout=DEVNULL, stderr=STDOUT)

if __name__ == "__main__":
    main()