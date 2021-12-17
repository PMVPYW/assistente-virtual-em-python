import time
import datetime
import playsound
import speech_recognition as sr
import webview
import os
import pyautogui
import ctypes
import threading

recon = sr.Recognizer()


def play_game():
    playsound.playsound("sound/general/select_game.mp3")
    with open("games/games.txt", "r") as f:
        games = f.read().split("\n")
    for x in range(len(games)):
        print(f"[{x}] {games[x]} ")
    try:
        option = int(input())
        if option == 0:
            import bullet_game
        elif option == 1:
            import pong_game
        elif option == 2:
            import snake_game
        elif option == 3:
            import traffic_racer
        else:
            print("game not found!")
            playsound.playsound("sound/general/game_not_found.mp3")
    except:
        pass



playsound.playsound("sound/general/init.mp3")
while True:
    
    print("listening...")
    with sr.Microphone() as source:
        recon.adjust_for_ambient_noise(source)
        audio = recon.listen(source)
    said = ""
    try:
        said = recon.recognize_google(audio, language="pt-BR")
        said = said.lower()
        print(said)
    except:
        print("404")
    
    if "horas" in said:
        now = datetime.datetime.now()
        now = now.strftime("sound/time/%#H horas, %#M minutos.mp3")
        playsound.playsound(now)
    
    if "horário" in said:
        playsound.playsound("sound/general/schedule.mp3")
        webview.create_window("horário", "https://gisem.dei.estg.ipleiria.pt/horarios")
        webview.start()
    if "linha de comandos" in said:
        os.system(input("insira o comando: "))
    
    if "programa" in  said:
        program = ""
        try:
            program = said.replace("programa", "")
            print(program)
            pyautogui.press("winleft")
            time.sleep(0.5)
            pyautogui.write(program)
            time.sleep(0.5)
            pyautogui.press("return")
        except:
            playsound.playsound("sound/general/select_program_no_recognized.mp3")
    if "bloquear computador" in said or "bloquear o computador" in said:
        print("blocking")
        playsound.playsound("sound/general/block_computer.mp3")
        ctypes.windll.user32.LockWorkStation()
    if "definições" in said:
        playsound.playsound("sound/general/settings.mp3")
        pyautogui.press("winleft")
        time.sleep(0.5)
        pyautogui.write("definições")
        time.sleep(0.5)
        pyautogui.press("winleft")
    if "jogo" in said or "jogar" in said:
        t1 = threading.Thread(target=play_game)
        try:
            t1.start()
        except:
            pass
    if "reiniciar computador" in said:
        playsound.playsound("sound/general/reboot_computer.mp3")
        os.system("shutdown -r -t 0")
    if "desligar computador" in said or "encerrar computador" in said:
        playsound.playsound("sound/general/shutdown_computer.mp3")
        os.system("shutdown -p")
        playsound.playsound("sound/general/goodbye.mp3")
        exit()

    if "adeus" in said or "desligar" in said or "terminar processo" in said:
        playsound.playsound("sound/general/goodbye.mp3")
        exit()
