import os
import random
import time

import pygame as pygame

happyMusicList = os.listdir('.\happy')
sadMusicList = os.listdir('.\sad')

while True:
    print("Music Player")
    print("请输入心情：")
    inputs = eval(input())
    if inputs == 0:
        musicName = ".\\happy\\" + random.choice(happyMusicList)
    elif inputs == 1:
        musicName = ".\\sad\\" + random.choice(sadMusicList)
    elif inputs == 8:
        break
    else:
        print("输入有误！请重新输入")
        continue
    pygame.mixer.init()
    pygame.mixer.music.load(musicName)
    pygame.mixer.music.play()
    time.sleep(100)