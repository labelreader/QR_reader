import numpy as np
import sys
import time
import cv2
import zbar
from PIL import Image

# will return index 
def indices(a,func) :
	return [i for (i, val) in enumerate(a) if func(val)]

def pollItem() :
	prodcall = raw_input("Enter item you wish to call: ")
	idx = indices(prodlist, lambda x: x == prodcall)
	print idx
	
	
	# connect a webcam
#Cam = cv2.VideoCapture(0)

	# read image from file
#img = cv2.imread('test_QR.png',0)
#img = cv2.imread('RW_QRcode1.png',0)
#img = cv2.imread('test_ean8.png', 0)
#img = cv2.imread('2018-02-25-234034.jpg', 0)

	# read image from webcam
#img = Cam.read()[1]

	# display image
#cv2.namedWindow('image', cv2.WINDOW_NORMAL)
#cv2.imshow('image',img)
#cv2.waitKey()
#cv2.destroyAllWindows()

	# initializing arrays 
prodlist= []
prodloc = []

	# initialize a scanner
scanner = zbar.ImageScanner()
scanner.parse_config('enable')

print 'start'
i = 0

# raw detection code

Cam = cv2.VideoCapture(1)
img = Cam.read()[1]
print 'read'
#downsample image 
resized = cv2.resize(img,(600,400), interpolation = cv2.INTER_AREA)
# convert to grayscale 
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY, dstCn=0)

pil = Image.fromarray(gray)
width, height = pil.size
	# output image size in pixles 
#print width, height 
raw = pil.tobytes()

	# create a reader
image = zbar.Image(width, height, 'Y800', raw)
	# scan the image for QRCodes
scanner.scan(image)
	# extract results and append them to a vector
for symbol in image:
	prodlist.append(symbol.data)
	prodloc.append(1)#print prodlist
i += 1
Cam = None
	
	# testing recall functionality 
print prodlist
pollItem()

