import os

streamer = input("type a streamer name:")

link = f"http://www.twitch.tv/{streamer}"
print(f"Opening {link}") 
os.system(f"mpv {link} --no-terminal &")
