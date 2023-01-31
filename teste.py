import cv2
import sys
import json

args = sys.argv
img = cv2.imread("data/datasets/img_small/test/000.png",0) 
print(img)