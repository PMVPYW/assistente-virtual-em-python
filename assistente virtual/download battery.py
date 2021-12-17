from gtts import gTTS

for x in range(0, 100):
    print(f"{x}%")
    download = gTTS(text = f"A bateria está a {x}%", lang="pt-BR")
    download.save(f"battery/{x}.mp3")
print("finish!")
