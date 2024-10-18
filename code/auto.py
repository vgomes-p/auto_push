#****************************************************************#
#                                                                #
#    Lembrete: Mude o caminho para o diretorio na linha 41!!!    #
#                                                                #
#****************************************************************#

#!pip install pyautogui

import pyautogui as at
import time as tm

at.PAUSE = .5

def actenter(void):
	at.write(void)
	at.press('enter')

def maxsr():
	at.keyDown("win")
	at.press("up")
	at.keyUp("win")

def splitsr():
	at.keyDown("win")
	at.press("right")
	at.keyUp("win")

def minsr():
	at.keyDown("alt")
	at.keyDown("space")
	at.press("n")
	at.keyUp("alt")
	at.keyUp("space")

#open terminal
at.press("win")
actenter("terminal")
tm.sleep(1.5)
maxsr()
actenter("fish")
tm.sleep(1)
actenter("clear")


#open dir
actenter("cd repository")
actenter("cd auto_push")

#git status
actenter("git status")
tm.sleep(1.5)

#git add
actenter("git add .")

#git commit
actenter('git commit -m "auto_commit_by_vgomes-p_py"')

#git push
actenter('git push')