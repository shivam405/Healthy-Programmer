from pygame import mixer
from time import time
from datetime import datetime
def musicOnLoop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.set_volume(0.7)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")


if __name__ == '__main__':
    # musicOnLoop("water.ogg", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 40*60
    execsecs = 45*60
    eyessecs = 30*60
    while True:
        if time()-init_water > watersecs:
            print("Water drinking time. Enter 'drank' to stop the alarm.")
            musicOnLoop("water.ogg", "drank")
            init_water = time()
            log_now("Drank water at: ")
        if time()-init_eyes > eyessecs:
            print("Eye exercise time. Enter 'doneedrankyes' to stop the alarm.")
            musicOnLoop("eyes.ogg", "doneeyes")
            init_eyes = time()
            log_now("Eye Relaxed at: ")
        if time()-init_exercise > execsecs:
            print("Physical exercise time. Enter 'donephy' to stop the alarm.")
            musicOnLoop("physical.ogg", "donephy")
            init_exercise = time()
            log_now("physical exercise done at: ")


