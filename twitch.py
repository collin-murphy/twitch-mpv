#imports
import sys
from subprocess import DEVNULL, STDOUT, check_call
from bs4 import BeautifulSoup
import requests as rq

#check if channel is live logic
def check_live(URL: str):
    request = rq.get(URL).content.decode('utf-8')
    return ('isLiveBroadcast' in request)

#handle what happens from check_live logic
def handle_live(URL: str, channel: str):
    #if channel is live, open
    if check_live(URL) == True:
        print(f'Opening {channel}\'s stream @ {URL}')
        open_mpv(URL)
    #if not, tell user
    else:
        print(f'{channel} is not live.')

#open file
def open_mpv(twitch_link_full:str):
    check_call(['mpv', twitch_link_full], stdout=DEVNULL, stderr=STDOUT)

#executed on script run    
def main():
    #get channel
    arg_count = len(sys.argv) 
    channel = ""
    if arg_count == 2:
        channel = sys.argv[1]
    elif arg_count == 1:
        channel = input('Type a channel name:')
    else:
        print("Usage: python3 twitch.py CHANNEL_NAME")
        return

    channel = channel.lower()
    #generate twitch link
    link = f'http://www.twitch.tv/{channel}'

    #check if channel is live
    handle_live(link, channel)    


if __name__ == "__main__":
    main()