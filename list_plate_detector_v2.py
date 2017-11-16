# Main.py

import cv2
import numpy as np
import os
import os, os.path
import DetectChars
import DetectPlates
import PossiblePlate


images=[]

rename_paths=0
path='license/'
rename_path='rename/'
save_plate='plate/'
def read_images(path,numbers):
	images=[]
	counter_car_plate=0
	print numbers
	for i in range(numbers):
		print ########################
		print "Read Car plate from:"+path+str(i)+".png"+"\n"+"====================>"
		image=cv2.imread(path+str(i)+'.png')
		print "Start Extract Plate....."
		listOfPossiblePlates = DetectPlates.detectPlatesInScene(image)           # detect plates
		counter_car_plate=write_image(listOfPossiblePlates,counter_car_plate)   #write file to plate folder
		#image=cv2.resize(cv2.imread(path+str(i+1)+'.jpg'))
		
	
def read_images_1(path,list,numbers):
	images=[]
	counter_car_plate=0
	print numbers
	for i in range(numbers):
		print ########################
		print "Read Car plate from:"+path+list[i]+"\n"+"====================>"
		image=cv2.imread(path+list[i])
		print "Start Extract Plate....."
		listOfPossiblePlates = DetectPlates.detectPlatesInScene(image)           # detect plates
		counter_car_plate=write_image(listOfPossiblePlates,counter_car_plate)   #write file to plate folder
		#image=cv2.resize(cv2.imread(path+str(i+1)+'.jpg'))
			


def rename_of_image(path,re_path,list,rename_paths,numbers):
	images=[]
	for i in range(numbers):
		orig_path=path+list[i]
		image=cv2.imread(orig_path)
		re_name_path=re_path+str(rename_paths)+'.png'
		print orig_path+"=>" +re_name_path
		cv2.imwrite(re_name_path, image)
		rename_paths=rename_paths+1

def write_image(vector_image,counter_path):
	for i in range(len(vector_image)):
		cv2.imwrite(save_plate+str(counter_path)+".png", vector_image[i].imgPlate)
		counter_path=counter_path+1
	return counter_path

list = os.listdir(path) # dir is your directory path
numbers_files = len(list)
print list
print "total number of car plate:"+str(numbers_files)+"\n"
print "start renmae of image................."
#rename_of_image(path,rename_path,list,rename_paths,numbers_files)


print "start read image.................."

from time import sleep
#sleep(0.1) # Time in seconds.
read_images_1(path,list,numbers_files)
#read_images(rename_path,numbers_files)





#for i in range(numbers_files):
	
	#licPlate = listOfPossiblePlates[0]
	

	#cv2.imshow("imgOriginalScene", listOfPossiblePlates[0].imgPlate)            # show scene image
	#cv2.imshow("asd",images[1])
	#cv2.waitKey(0)					# hold windows open until user presses a key
	##cv2.imshow("asd",images[1]);
	#print i







