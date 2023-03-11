import win32com.client
import keyboard
import numpy
import mouse
from glob import glob
from time import sleep
from os import path
from os import system
from os import remove

check_win = path.exists("C:\Windows\SysWOW64")

if check_win == True:
    clear = 'cls'
else:
    clear = 'clear'

shell = win32com.client.Dispatch("WScript.Shell")

if glob('*.I2plg'):
  print("ISZ-2021 Plugin Loader Has Detected an .I2plg Plugin File in Current Directory.")
  print("Type The 'File Name' Below to Load It.")
  print(" ")
  decent = input("File Name: ")

  if ".I2plg" in decent:
    print(" ")
  else:
    print(" ")
    decent = decent + ".I2plg"

system(clear)

with open(decent,'r') as plugFile:
  creator = plugFile.readline().rstrip()
  
  code1 = plugFile.readline().rstrip()
  code1_note = plugFile.readline().rstrip()
  
  code2 = plugFile.readline().rstrip()
  code2_note = plugFile.readline().rstrip()
  
  code3 = plugFile.readline().rstrip()
  code3_note = plugFile.readline().rstrip()
  
  code4 = plugFile.readline().rstrip()
  code4_note = plugFile.readline().rstrip()
  
  print(f"Plugin Creator: {creator}")
  print(f"Loaded Plugin: {decent}.")
  print(" ")
  print(f"Code #1 Hotkey - '7'.")
  print(f"{code1_note}")
  print(" ")
  print(f"Code #2 Hotkey - '8'.")
  print(f"{code2_note}")
  print(" ")
  print(f"Code #3 Hotkey - '9'.")
  print(f"{code3_note}")
  print(" ")
  print(f"Code #4 Hotkey - '0'.")
  print(f"{code4_note}")
  print(" ")


while 1==1:
    if keyboard.read_key() == "7":
        shell.sendkeys("`")
        shell.sendkeys(code1)
        keyboard.press_and_release("Enter")

    if keyboard.read_key() == "8":
        shell.sendkeys("`")
        shell.sendkeys(code2)
        keyboard.press_and_release("Enter")

    if keyboard.read_key() == "9":
        shell.sendkeys("`")
        shell.sendkeys(code3)
        keyboard.press_and_release("Enter")

    if keyboard.read_key() == "0":
        shell.sendkeys("`")
        shell.sendkeys(code4)
        keyboard.press_and_release("Enter")

    if keyboard.read_key() == "=":
        break