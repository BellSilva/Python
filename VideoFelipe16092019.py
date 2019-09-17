# Importing all necessary libraries 
import cv2 
import os
import numpy as np
from matplotlib import pyplot as plt
  
# Read the video from specified path 
cam = cv2.VideoCapture("C:\\Users\\aluno\\Downloads\\y2mate.com - darling_in_the_franxx_opening_hd_hCzkkHwR2gg_720p.mp4") 
  
try: 
      
    # creating a folder named data 
    if not os.path.exists('data'): 
        os.makedirs('data') 
  
# if not created then raise error 
except OSError: 
    print ('Error: Creating directory of data') 
  
# frame 
currentframe = 0
  
while(True): 
      
    # reading from frame 
    ret,frame = cam.read() 
    
    
    
    if ret:
        
        # if video is still left continue creating images 
        name = './data/frame' + str(currentframe) + '.jpg'
        print ('Creating...' + name) 
  
        # writing the extracted images 
        cv2.imwrite(name, frame) 
  
        # increasing counter so that it will 
        # show how many frames are created 
        currentframe += 1
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        mask = np.zeros(frame.shape[:2], np.uint8)
        mask[100:300, 100:400] = 255
        masked_img = cv2.bitwise_and(frame,frame,mask = mask)
        hist_full = cv2.calcHist([frame],[0],None,[256],[0,256])
        hist_mask = cv2.calcHist([frame],[0],mask,[256],[0,256])
        
        cv2.imshow('frame',gray)
        cv2.waitKey(0)
    
        
        
    else: 
        break
  
# Release all space and windows once done 
cam.release() 
cv2.destroyAllWindows()