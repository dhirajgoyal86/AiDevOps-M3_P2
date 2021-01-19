###pip install opencv-python

# Importing all necessary libraries 
import cv2 
import os 

# Read the video from specified path 
cam = cv2.VideoCapture("./video-in/carla-simulator-30mph.mp4") 

try: 

    # creating a folder named video-out 
    if not os.path.exists('video-out'): 
        os.makedirs('video-out') 

# if not created then raise error 
except OSError: 
    print ('Error: Creating directory of video-out') 

# frame 
currentframe = 0

while(True): 

    # reading from frame 
    ret,frame = cam.read() 

    if ret: 
        # if video is still left continue creating images 
#        name = './video-out/frame' + str(currentframe) + '.jpg'
        name = './video-out/sample' + str(currentframe) + '.jpg'		
        print ('Creating...' + name) 

        # writing the extracted images 
        cv2.imwrite(name, frame) 

        # increasing counter so that it will 
        # show how many frames are created 
        currentframe += 1
    else: 
        break

# Release all space and windows once done 
cam.release() 
cv2.destroyAllWindows() 
