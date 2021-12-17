from gtts import gTTS
from tqdm import tqdm
import time
with open("sound/time/list.txt", "r") as f:
    data = f.read()
data = data.split("\n")
with open("sound/time/log.txt", "r") as f:
    downloaded = f.read().split("\n")

print(f"undone downloads: {len(data)-len(downloaded)}")

for x in tqdm(range(len(data)), desc="Downloads"):
    if data[x-1] in downloaded:
        print("!404")
    else:
        download = gTTS(text = f"Agora são {data[x-1]}", lang="pt-BR")
        try:
            download.save(f"sound/time/{data[x-1]}mp3")
        except:
            end = time.time()+3600
            sended = False
            while time.time() <= end:
                remaining = int(end-time.time())
                if remaining % 10 == 0:
                    if not sended:
                        print(f"{remaining}: 'Waiting one hour due too many requests'")
                        sended = True
                else:
                    sended = False
            download.save(f"sound/time/{data[x-1]}mp3")
        with open("sound/time/log.txt", "a+") as f:
            f.write(f"{data[x-1]}\n")
        downloaded.append(data[x-1])
