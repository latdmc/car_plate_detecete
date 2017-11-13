# Main.py

import cv2
import numpy as np
import os
import os, os.path
import DetectChars
import DetectPlates
import PossiblePlate


images=[]
counter_car_plate=0
path='LicPlateImages/'
save_plate='plate/'
def read_images(path,numbers):
	images=[]
	for i in range(numbers):
		print path+str(i+1)+".png"+"\n"+"====================>"
		image=cv2.imread(path+str(i+1)+'.png')
		#image=cv2.resize(cv2.imread(path+str(i+1)+'.jpg'))
		images.append(image)
	
	return images

def write_image(vector_image,counter_path):
	for i in range(len(vector_image)):
		cv2.imwrite(save_plate+str(counter_path)+".png", vector_image[i].imgPlate)
		counter_path=counter_path+1
	return counter_path

list = os.listdir(path) # dir is your directory path
numbers_files = len(list)
print "total number of car plate:"+str(numbers_files)+"\n"
print "start read image:"

images=read_images(path,numbers_files)

print ########################
print "Read Car plate finisk....."
print "Start Extract Plate....."

for i in range(numbers_files):
	listOfPossiblePlates = DetectPlates.detectPlatesInScene(images[i])           # detect plates
	licPlate = listOfPossiblePlates[0]
	counter_car_plate=write_image(listOfPossiblePlates,counter_car_plate)

	#cv2.imshow("imgOriginalScene", listOfPossiblePlates[0].imgPlate)            # show scene image
	#cv2.imshow("asd",images[1])
	#cv2.waitKey(0)					# hold windows open until user presses a key
	##cv2.imshow("asd",images[1]);
	print i







