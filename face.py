import cv2
import dlib
from PIL import Image                                                            
import numpy                                                                     
import glob
import shutil
import os
import sys 

def Check(Path):
    # Load the detector   
    detector = dlib.get_frontal_face_detector()

    # read the image
    img = cv2.imread(Path)

    # Convert image into grayscale
    gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

    # Use detector to find landmarks
    faces = detector(gray)
    if(len(faces) > 0):
        return True
    else:
        return False
filesPath = sys.argv[1]
filelist= [file for file in os.listdir(filesPath) if file.endswith('.jpeg')]


for x in filelist:
  if(Check(filesPath+x) == True):
      os.replace(filesPath+x,"Face/"+x)
  else:
      os.replace(filesPath+x,"nonFace/"+x)
  

