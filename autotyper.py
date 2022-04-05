# -*- coding: utf-8 -*-

#code by JRay 2022/4/5

from pynput.keyboard import Controller
import time

keyboard = Controller()

start = 11000000
end = 20000000


time.sleep(1)
def typer(var):
    keyboard.type(var)
    
for num in range(start,end):
    var = str(num)
    typer(var)
    print(var)
    time.sleep(4.5)