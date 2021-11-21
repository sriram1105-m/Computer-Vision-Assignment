#!/usr/bin/env python3

#importing the required libraries
import sys, os, math
import cv2
import numpy

#Read the number of frames
nframes = int(sys.argv[1])
for frame in range(0, nframes):
    fn_left = sys.argv[2] % frame
    fn_right = sys.argv[3] % frame
    
   
    #Reading the images
    left_im = cv2.imread(fn_left)
    right_im = cv2.imread(fn_right)

    # Displaying the images
    cv2.imshow("left set", left_im)
    cv2.waitKey(50)
    cv2.imshow("right set", right_im)
    cv2.waitKey(50)   

    # Adapted the code from the hint email sent by the professor
    #Locating the objects in the frame
    # Cycling through the pixels for the images from left camera
    ny, nx, nc = left_im.shape
    if frame == 0:
        print("[Images are %d x %d x %d pixels]" % (ny, nx, nc), file = sys.stderr)
    for y in range (0, ny):
        for x in range (0, nx):
            b, g, r = left_im[y, x]
            if r == 0 and g == 0 and b == 0:
                continue                          # background 
            elif r > 0 and g == 0 and b == 0:
                left_im[y, x] = (0, 0, 255)            # Red object
            elif r > 0 and g > 0 and b == 0:
                left_im[y, x] = (0, 255, 255)          # Yellow object
            elif r == 0 and g > 0 and b == 0:
                left_im[y, x] = (0, 255, 0)            # Green object
            elif r == 0 and g == 0 and b > 0:
                left_im[y, x] = (255, 0, 0)            # Blue object
            elif r > 0 and g > 0 and b == 0:
                left_im[y, x] = (0, 165, 255)          #Orange object
            elif r == 0 and g > 0 and b > 0:
                left_im[y, x] = (255, 255, 0)          # Cyan object
            elif r > 0 and g > 0 and b > 0:
                left_im[y, x] = (255, 255, 255)        # White Object
            else:
                print("Unexpected pixel colour", r, g, b)
   
          
    # Cycling through the pixels for the images from right camera 
    ny, nx, nc = right_im.shape
    if frame == 0:
        print("[Images are %d x %d x %d pixels]" % (ny, nx, nc), file = sys.stderr)
    for y in range (0, ny):
        for x in range (0, nx):
            b, g, r = right_im[y, x]
            if r == 0 and g == 0 and b == 0:
                continue                          # background 
            elif r > 0 and g == 0 and b == 0:
                right_im[y, x] = (0, 0, 255)            # Red object
            elif r > 0 and g > 0 and b == 0:
                right_im[y, x] = (0, 255, 255)          # Yellow object
            elif r == 0 and g > 0 and b == 0:
                right_im[y, x] = (0, 255, 0)            # Green object
            elif r == 0 and g == 0 and b > 0:
                right_im[y, x] = (255, 0, 0)            # Blue object
            elif r > 0 and g > 0 and b == 0:
                right_im[y, x] = (0, 165, 255)          #Orange object
            elif r == 0 and g > 0 and b > 0:
                right_im[y, x] = (255, 255, 0)          # Cyan object
            elif r > 0 and g > 0 and b > 0:
                right_im[y, x] = (255, 255, 255)        # White Object
            else:
                print("Unexpected pixel colour", r, g, b)
   
    # Adapted the code and modified into a routine from the hint email
    # sent by the professor               
    #Locating the object
    def locate_left(r, g, b):
        xlo = nx + 1
        xhi = -1
        for y in range(0, ny):
            for x in range(0, nx):
                b, g, r = left_im[y, x]
                if r > 0 and g == 0 and b == 0:
                    if x < xlo: xlo = x
                    if x > xhi: xhi = x
    
        xL = (xlo + xhi) / 2
        print("The value of xL is:", xL)
    return xL

    #Locating the object
    def locate_right(r, g, b):
        ylo = yx + 1
        yhi = -1
        for y in range(0, ny):
            for x in range(0, nx):
                b, g, r = right_im[y, x]
                if r > 0 and g == 0 and b == 0:
                    if y < ylo: ylo = y
                    if y > yhi: xhi = y

        xR = (ylo + yhi) / 2
        print("The value of xR is:", xR)
    return xR

    # Converting the xL and xR to microns
    xL = xL * (1e-5)
    xR = xR * (1e-5)
    
    # Calculate the distance
    # formula for calculating distance is z = f*B / (xL - xR)
    # From the assignment task we get the values for f = 12m, B = 3.5km 
    # Converting 3.5km to meters we get the number 3500
    Z = (12 * 3500) / (xL - xR)

    # Printing the results
    print("The value of Z is:", Z)

    # following the motion of the objects
    # using Canny edge detector
    def canny_contour_left():
        gray1 = cv2.cvtColor(left, cv2.COLOR_BGR2GRAY)
        edge1 = cv2.Canny(gray1, 100, 170, apertureSize = 3)
        countours, _ = cv2.findContours(edge1, CV2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # These lines are from the website 
        #https://stackoverflow.com/questions/41832237/measuring-distance-between-two-contours-in-video-opencv-python
        for c in cnts:
            M = cv2.moments(c)
            cX = int(M['m10'] / M['m00'])
            cY = int(M['m01'] / M['m00'])
            center.append([cX, cY])
            if len(centers) >=2:
                dx= centers[0][0] - centers[1][0]
                dy = centers[0][1] - centers[1][1]
        return

    def canny_contour_right():
        gray2 = cv2.cvtColor(right, cv2.COLOR_BGR2GRAY)
        edge2 = cv2.Canny(gray2, 100, 170, apertureSize = 3)
        contours, _ = cv2.findContours(edge2, CV2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # These lines are from the website 
        #https://stackoverflow.com/questions/41832237/measuring-distance-between-two-contours-in-video-opencv
        for c in cnts:
            M = cv2.moments(c)
            cX = int(M['m10'] / M['m00'])
            cY = int(M['m01'] / M['m00'])
            center.append([cX, cY])
            if len(centers) >=2:
                dx= centers[0][0] - centers[1][0]
                dy = centers[0][1] - centers[1][1]
    return

    dx = xL[current] - xL[previous]
    dy = yB[current] - yB[previous]

    angle = atan2 (dx / dy)

    # Adapted from the hint email given by the professor
    DEBUG = False:
    if DEBUG:
        print("xlo and xhi for the red object", xlo, xhi)
        cv2.imshow("Red", im)
    elif:
        print("xlo and xhi for the green object", xlo, xhi)
        cv2.imshow("Green", im)
    elif:
        print("xlo and xhi for the blue object", xlo, xhi)
        cv2.imshow("Blue", im)
    elif:
        print("xlo and xhi for the white object", xlo, xhi)
        cv2.imshow("White", im)
    elif:
        print("xlo and xhi for the orange object", xlo, xhi)
        cv2.imshow("orange", im)
    elif:
        print("xlo and xhi for the yellow object", xlo, xhi)
        cv2.imshow("yellow", im)
    else:
        print("xlo and xhi for the cyan object", xlo, xhi)
        cv2.imshow("cyan", im)
    








