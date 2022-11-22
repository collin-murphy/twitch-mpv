#imports
import sys
from subprocess import DEVNULL, STDOUT, check_call
from bs4 import BeautifulSoup
import requests as rq

def check_live(URL: str):
    request = rq.get(URL).content.decode('utf-8')
    return ('isLiveBroadcast' in request)

def handle_live(URL: str, streamer: str):
    if check_live(URL) == True:
        print(f'Opening {streamer}\'s stream.')
        open_mpv(URL)
    else:
        print(f'{streamer} is not live.')


def open_mpv(twitch_link_full:str):
    print(f'Opening {twitch_link_full}') 
    check_call(['mpv', twitch_link_full], stdout=DEVNULL, stderr=STDOUT)

    
def main():
    arg_count = len(sys.argv)
     
    streamer = ""
    if arg_count == 2:
        streamer = sys.argv[1]
    elif arg_count == 1:
        streamer = input('type a streamer name:')
    else:
        print("Usage: python3 twitch.py STREAMER-NAME")
        return

    link = f'http://www.twitch.tv/{streamer}'

    handle_live(link, streamer)    
    

    #open_mpv(link)


if __name__ == "__main__":
    main()