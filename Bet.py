import matplotlib
from PIL import ImageGrab
from PIL import Image
import time 
import pyautogui as p
import threading
import os
import pandas as pd 
import win32api
import win32con
import cv2
import numpy as np
from PIL import ImageGrab
import cv2
import keyboard
import csv 



from directKeys import click, queryMousePosition
import time

import numpy as np 
position = (1057,442)
 
#for x in range(4):
   # time.sleep(2)
   # print(p.displayMousePosition())

#a.show()
gameCoords = [1057,442,1057,442]



px_coord = [1057,442]
#CT Rgb is 57 57 57
# T RGB is 173 107 40   
#Dice RGB is  83 71 51

Rolls = []
x =0
number = 156
def rollFunc(x):
    x = 0
    while True:
         if x < number:
            win32api.keybd_event(win32con.VK_SNAPSHOT, 1)
            time.sleep(23)
                                #1047, 443, 1065, 471
            a = ImageGrab.grab()
            x+=1
            a.save("C:\\Users\\Kellan\\Desktop\\Bet script\\Images\\Image.jpg")
        #a.show()
            pix_rgb =                                                                                  a.load()
            RGB = pix_rgb[1211,494]
            print (RGB)
        #while True:
           # if x < number:
            #time.sleep(0)
            if RGB == (29, 29 , 29) or RGB == (97, 97, 98):
                #Rolls = 'CT'
                
                Rolls.append('CT')
            if RGB == (223, 143, 47) or RGB == (99,62,36) :
               # Rolls = 'T'
                
                Rolls.append('T')
            if (RGB == (218, 165, 55) or RGB == (222, 167, 54)):
               # Rolls='D'
               
                Rolls.append( 'D')
        #222, 167, 54):
            
            
            else:
                break
            
    #print(Rolls)
    #Rolls == (("[{0}]".format(' '.join(map(str,Rolls)))))
    print((("[{0}]".format(' '.join(map(str,Rolls))))))     
    print(Rolls)
    return(Rolls)
    print((("[{0}]".format(' '.join(map(str,Rolls))))))
    



#def removeQ(Rolls):
   # Rolls ==  ((("[{0}]".format(' '.join(map(str,Rolls))))))
    #return removeQ


    




def write(Rolls):

    with open("C:\\Users\\Kellan\\Desktop\\Bet script\\Rolls.csv" , mode = 'w') as Rolls_file:
        Roll_writer = csv.writer(Rolls_file, delimiter = " ", quoting = csv.QUOTE_MINIMAL, escapechar = '\\')
                                   # , delimiter= ' '
        Roll_writer.writerow(Rolls)
def main():
    for i in range(1000):
        rollFunc(0)
        #removeQ(Rolls)
        write(Rolls)
   
main()

#pix = a.load()
#print (pix[1057,442])


#while True:
 #   if x < number:
  #      time.sleep(0)
   #     if RGB(29, 29 , 29) == True:
    #        Rolls.append(" CT")
     #   if RGB(223, 143, 47) == True:
      #      Rolls.append(" T")
       # if RGB(83, 71, 51) == True:
        #    Rolls.append(" D")
        #else:
         #   Rolls.append(" B")
        #print(Rolls)

