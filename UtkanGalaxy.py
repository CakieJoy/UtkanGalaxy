import time
import os
import sys
import pyautogui
import webbrowser


def wait(int):
    time.sleep(int)

def cmd(command):
    os.system(command)

def openSite(url):
    webbrowser.open(url)

class Konsole:
    class Win:
        def clear():
            os.system("cls")
    class Mac:
        def clear():
            os.system("clear")

class FastCode:
    class App:
        class TerminalApp:
            def now(TerminalCommand):
                os.system(TerminalCommand)