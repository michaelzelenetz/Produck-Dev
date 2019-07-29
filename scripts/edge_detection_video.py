"""
Michael Z: This script demonstrates reading video from the Raspberry Pi Camera into OpenCV and using the built in Canny 
algorithm to detect edges and to eliminate the details.

Usage: run on raspberry pi with: $ python3 edge_detection_video.py
       Hit 'q' to terminate.
       
Note: this does not save to file and will not work in headless mode--you should connect a monitor to the Raspberry Pi for this demo

www.pyimagesearch.com/2016/08/29/common-errors-using-the-raspberry-pi-camera-module
"""
#import packages

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

#initialize camera
camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size = (640,480))

time.sleep(0.1)

#capture frames from camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        #get the imagea a Numpy Array
        image = frame.array

        edges = cv2.Canny(image, 100,200)
        cv2.imshow("Frame", edges)
        key = cv2.waitKey(1) & 0xFF

        #clear stream and get next frame
        rawCapture.truncate(0)

        # if 'q' is pressed then break loop
        if key == ord("q"):
                break

