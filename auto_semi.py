import pyautogui as py
import keyboard as key
import datetime as date

ACKNOWLEDGMENT_TERM = 0.2;

now = date.datetime.now()
count = 0
while True:
  key.wait("shift")
  while key.is_pressed("shift"): pass
  if (date.datetime.now() - now).total_seconds() < ACKNOWLEDGMENT_TERM:
    count += 1
  else:
    count = 1
  now = date.datetime.now()
  if count == 2:
    count = 0
    py.press(["end", ";", "enter"])