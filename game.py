import pygame.mixer
import sys
from pygame.mixer import Sound
from gpiozero import Button
from signal import pause

pygame.mixer.init()
    
button_sounds = {
    Button(2) : (Sound("music/intro.wav")).play,
    Button(3) : (Sound("music/good_2.wav")).play,
    Button(4) : (Sound("music/wrong.wav")).play,
    Button(17) : (Sound("music/level_3.wav")).play
}
try:
    for button, sound in button_sounds.items():
        button.when_pressed = sound
    pause()
except KeyboardInterrupt:
    print("Finish game -- Millionairs")
    sys.exit()
