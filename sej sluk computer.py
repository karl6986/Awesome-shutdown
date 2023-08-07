#setup
#-------------------------------------------------------------------
from ctypes import *
from pygame import mixer
from tkinter import *
import os
import time
from win32gui import *
from win32api import *
from win32con import *
import win32gui
import win32con
time.sleep(5)
ok = windll.user32.BlockInput(True)
def ScreenOFF():
    """
    Function to turn off the screen.
    """
    return win32gui.SendMessage(win32con.HWND_BROADCAST,
                            win32con.WM_SYSCOMMAND, win32con.SC_MONITORPOWER, 2)

def ScreenON():
    """
    Function to turn on the screen.
    """
    return win32gui.SendMessage(win32con.HWND_BROADCAST,
                            win32con.WM_SYSCOMMAND, win32con.SC_MONITORPOWER, -1)


#-------------------------------------------------------------------

mixer.init()
mixer.music.load("D:\hej.mp3")
mixer.music.play()
time.sleep(60)
mixer.music.pause()
ScreenOFF()
mixer.music.unpause()
time.sleep(7)
mixer.music.fadeout(7777)
time.sleep(10)
os.system("shutdown -s -t 0")