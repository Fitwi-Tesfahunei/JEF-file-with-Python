# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 00:46:12 2022

@author: User
"""

import numpy as np
# Function to create stitch sequence

'''circle(r) creates a circle with radius r in mm'''
def circle(r):
    th = np.arange(0,2*np.pi,0.1) # theta from 0 to 2*pi (360 degrees)
    
    stitches = []
    for i in th:
        if r*np.cos(i)<0:
            if r*np.sin(i)<0:
                stitches += [256+int(r*np.cos(i)),256+int(r*np.sin(i))]
            else:
                stitches += [256+int(r*np.cos(i)),int(r*np.sin(i))]
        else:
            if r*np.sin(i)<0:
                stitches += [int(r*np.cos(i)),256+int(r*np.sin(i))]
            else:
                stitches += [int(r*np.cos(i)),int(r*np.sin(i))]
    for j in range(len(stitches)):
        if stitches[j] == 256:
            stitches[j] = 0
    return stitches

''' fractal() creates a fractal on the 4 edges of the embroidery'''
def fractal():
    stitches = []
    for i in range(6):
        for i in range(5):
            stitches += [ 0, 246,] # move -5mm in the y direction
        for i in range(4):
            stitches += [ 246, 0,] # move -4mm in the x direction
        for i in range(2):
            stitches += [0,10,] # move 2mm in the y direction
        for i in range(2):
            stitches += [10,0,] # move 2mm in the x direction
        for i in range(3):
            stitches += [0,10,] # move 3mm in the y direction
        for i in range(6):
            stitches += [246,0,] # move -6mm in the x direction
        for i in range(3):
            stitches += [0,246,] # move -3mm in the y direction
        for i in range(2):
            stitches += [10,0,] # move 2mm in the x direction
        for i in range(2):
            stitches += [0,246,] # move -2mm in the y direction
        for i in range(4):
            stitches += [246,0,] # move -4mm in the x direction
        for i in range(5):
            stitches += [0,10,] # move 5mm in the y direction
        for i in range(5):
            stitches += [246,0,] # move -5mm in the x direction
            
    for i in range(4):
        for i in range(4):
            stitches += [0,10,] # move 4mm in the y direction
        for i in range(2):
            stitches += [10,0,] # move 2mm in the x direction
        for i in range(2):
            stitches += [0,246,] # move -2mm in the y direction
        for i in range(3):
            stitches += [10,0,] # move 3mm in the x direction
        for i in range(6):
            stitches += [0,10,] # move 6mm in the y direction
        for i in range(3):
            stitches += [246,0,] # move -3mm in the x direction
        for i in range(2):
            stitches += [0,246,] # move -2mm in the y direction
        for i in range(2):
            stitches += [246,0,] # move -2mm in the x direction
        for i in range(4):
            stitches += [0,10,] # move 4mm in the y direction
        for i in range(5):
            stitches += [10,0,] # move 5mm in the x direction
        for i in range(5):
            stitches += [0,10,] # move 5mm in the y direction
        for i in range(5):
            stitches += [246,0,] # move -5mm in the x direction
    for i in range(4):
        stitches += [0,10,] # move 4mm in the y direction
    for i in range(2):
        stitches += [10,0,] # move 2mm in the x direction
    for i in range(2):
        stitches += [0,246,] # move -2mm in the y direction
    for i in range(3):
        stitches += [10,0,] # move 3mm in the x direction
    for i in range(6):
        stitches += [0,10,] # move 6mm in the y direction
    for i in range(3):
        stitches += [246,0,] # move -3mm in the x direction
    for i in range(2):
        stitches += [0,246,] # move -2mm in the y direction
    for i in range(2):
        stitches += [246,0,] # move -2mm in the x direction
    for i in range(4):
        stitches += [0,10,] # move 4mm in the y direction
    for i in range(5):
        stitches += [10,0,] # move 5mm in the x direction
        
    for i in range(5):
        for i in range(5):
            stitches += [0,10,] # move 5mm in the y direction
        for i in range(4):
            stitches += [10,0,] # move 4mm in the x direction
        for i in range(2):
            stitches += [0,246,] # move -2mm in the y direction
        for i in range(2):
            stitches += [246,0,] # move -2mm in the x direction
        for i in range(3):
            stitches += [0,246,] # move -3mm in the y direction
        for i in range(6):
            stitches += [10,0,] # move 6mm in the x direction
        for i in range(3):
            stitches += [0,10,] # move 3mm in the y direction
        for i in range(2):
            stitches += [246,0,] # move -2mm in the x direction
        for i in range(2):
            stitches += [0,10,] # move 2mm in the y direction
        for i in range(4):
            stitches += [10,0,] # move 4mm in the x direction
        for i in range(5):
            stitches += [0,246,] # move -5mm in the y direction
        for i in range(5):
            stitches += [10,0,] # move 5mm in the x direction
    for i in range(5):
        stitches += [0,10,] # move 5mm in the y direction
    for i in range(4):
        stitches += [10,0,] # move 4mm in the x direction
    for i in range(2):
        stitches += [0,246,] # move -2mm in the y direction
    for i in range(2):
        stitches += [246,0,] # move -2mm in the x direction
    for i in range(3):
        stitches += [0,246,] # move -3mm in the y direction
    for i in range(6):
        stitches += [10,0,] # move 6mm in the x direction
    for i in range(3):
        stitches += [0,10,] # move 3mm in the y direction
    for i in range(2):
        stitches += [246,0,] # move -2mm in the x direction
    for i in range(2):
        stitches += [0,10,] # move 2mm in the y direction
    for i in range(4):
        stitches += [10,0,] # move 4mm in the x direction
    for i in range(5):
        stitches += [0,246,] # move -5mm in the y direction
        
    for i in range(4):
        for i in range(5):
            stitches += [10,0,] # move 5mm in the x direction
        for i in range(4):
            stitches += [0,246,] # move -4mm in the y direction
        for i in range(2):
            stitches += [246,0,] # move -2mm in the x direction
        for i in range(2):
            stitches += [0,10,] # move 2mm in the y direction
        for i in range(3):
            stitches += [246,0,] # move -3mm in the x direction
        for i in range(6):
            stitches += [0,246,] # move -6mm in the y direction
        for i in range(3):
            stitches += [10,0,] # move 3mm in the x direction
        for i in range(2):
            stitches += [0,10,] # move 2mm in the y direction
        for i in range(2):
            stitches += [10,0,] # move 2mm in the x direction
        for i in range(4):
            stitches += [0,246,] # move -4mm in the y direction
        for i in range(5):
            stitches += [246,0,] # move -5mm in the x direction
        for i in range(5):
            stitches += [0,246,] # move -5mm in the y direction
            
    for i in range(5):
        stitches += [10,0,] # move 5mm in the x direction
    for i in range(4):
        stitches += [0,246,] # move -4mm in the y direction
    for i in range(2):
        stitches += [246,0,] # move -2mm in the x direction
    for i in range(2):
        stitches += [0,10,] # move 2mm in the y direction
    for i in range(3):
        stitches += [246,0,] # move -3mm in the x direction
    for i in range(6):
        stitches += [0,246,] # move -6mm in the y direction
    for i in range(3):
        stitches += [10,0,] # move 3mm in the x direction
    for i in range(2):
        stitches += [0,10,] # move 2mm in the y direction
    for i in range(2):
        stitches += [10,0,] # move 2mm in the x direction
    for i in range(4):
        stitches += [0,246,] # move -4mm in the y direction
    for i in range(5):
        stitches += [246,0,] # move -5mm in the x direction

    return stitches

'''star(h,w) creates a star fractal. h indicates the hight of the star
    while w indicates the width of the star'''        
def star():
    stitches = []
    for i in range(0,40):
        stitches += [ 10, int(0.5*15-2.5),]   #add w 1.1mm stiches moving up at a slope of 0.5
    
    for i in range(0,40):
        stitches += [ 246, 0,]   #add w 1mm stiches going left
    
    for i in range(0,40):
        stitches += [ 10, int(256+(-0.5*25+7.5)),]   #add w 1.1mm stiches moving down at a slope of -0.5

    for i in range(0,20):
        stitches += [ 246, int(-1.5*-5+7.5),]   #add h*2/3 1.8mm stiches moving up at a slope of -1.5

    for i in range(0,20):
       stitches += [ 246, int(256+(1.5*-15+7.5)),]   #add h*2/3 1.8mm stiches moving down at a slope of 1.5
    return stitches

'''filler_bottom() fills the bottom fractals with zigzags'''
def filler_bottom():
    stitches = []
    for i in range(11):
        stitches += [236,0,]
        stitches += [20,253]
    for i in range(4):
        stitches += [236,0,]
        stitches += [236,0,]
        for i in range(4):
            stitches += [10,255]
    stitches += [256-60,0]
    for i in range(4):
        stitches += [236,0,]
        stitches += [236,0,]
        for i in range(4):
            stitches += [10,1]
    stitches += [236,0,]
    stitches += [236,0,]
    for i in range(11):
        stitches += [20,0,]
        stitches += [236,3]
    
    return stitches

'''filler_left() fills the left fractals with zigzags'''
def filler_left():
    stitches = []
    for i in range(11):
        stitches += [0,20,]
        stitches += [253,236,]
    for i in range(4):
        stitches += [0,20,]
        stitches += [0,20,]
        for i in range(4):
            stitches += [255,246]
    stitches += [0,60]
    for i in range(4):
        stitches += [0,20,]
        stitches += [0,20,]
        for i in range(4):
            stitches += [1,246]
    stitches += [0,20,]
    stitches += [0,20,]
    for i in range(11):
        stitches += [0,236,]
        stitches += [3,20,]
    
    return stitches

'''filler_top() fills the top fractals with zigzags'''
def filler_top():
    stitches = []
    for i in range(11):
        stitches += [20,0,]
        stitches += [236,3]
    for i in range(4):
        stitches += [20,0,]
        stitches += [20,0,]
        for i in range(4):
            stitches += [246,1]
    stitches += [60,0]
    for i in range(4):
        stitches += [20,0,]
        stitches += [20,0,]
        for i in range(4):
            stitches += [246,255]
    stitches += [20,0,]
    stitches += [20,0,]
    for i in range(11):
        stitches += [236,0,]
        stitches += [20,253]
    
    return stitches

'''filler_right() fills the right fractals with zigzags'''
def filler_right():
    stitches = []
    for i in range(11):
        stitches += [0,236,]
        stitches += [3,20,]
    for i in range(4):
        stitches += [0,236,]
        stitches += [0,236,]
        for i in range(4):
            stitches += [1,10]
    stitches += [0,256-60]
    for i in range(4):
        stitches += [0,236,]
        stitches += [0,236,]
        for i in range(4):
            stitches += [255,10]
    stitches += [0,236,]
    stitches += [0,236,]
    for i in range(11):
        stitches += [0,20,]
        stitches += [253,236,]
    
    return stitches

'''right_bottom_corner() creates a triangular fractal on the right bottom corner'''
def right_bottom_corner():
    stitches = []
    a = []
    r = 25
    for i in range(25):
        a.append(r)
        r -=1
        k = 0
    for i in range(12):
        for j in range(a[k]):
            stitches += [10,10,]
        k +=1
        stitches += [0,246,]
        for i in range(a[k]):
            stitches += [246,246,]
        k +=1
        stitches += [10,0,]
            
    return stitches

'''right_top_corner() creates a triangular fractal on the right top corner'''
def right_top_corner():
    stitches = []
    a = []
    r = 25
    for i in range(25):
        a.append(r)
        r -=1
        k = 0
    for i in range(12):
        for j in range(a[k]):
            stitches += [246,10,]
        k +=1
        stitches += [10,0,]
        for i in range(a[k]):
            stitches += [10,246,]
        k +=1
        stitches += [0,10,]
            
    return stitches

'''left_top_corner() creates a triangular fractal on the left top corner'''
def left_top_corner():
    stitches = []
    a = []
    r = 25
    for i in range(25):
        a.append(r)
        r -=1
        k = 0
    for i in range(12):
        for j in range(a[k]):
            stitches += [246,246,]
        k +=1
        stitches += [0,10,]
        for i in range(a[k]):
            stitches += [10,10,]
        k +=1
        stitches += [246,0,]
            
    return stitches

'''left_bottom_corner() creates a triangular fractal on the left bottom corner'''
def left_bottom_corner():
    stitches = []
    a = []
    r = 25
    for i in range(25):
        a.append(r)
        r -=1
        k = 0
    for i in range(12):
        for j in range(a[k]):
            stitches += [10,246,]
        k +=1
        stitches += [246,0,]
        for i in range(a[k]):
            stitches += [246,10,]
        k +=1
        stitches += [0,246,]
            
    return stitches

def getStitchSequence():

    stitches = [128, 2] 	# 128 = escape_character , 2=Move 
    stitches += [0, 0]	# followed by 8 bit displacement X,Y
    stitches += [156, 181]	# go to (-10, -7.5)
    
    # Create the star fractal
    for i in range(10):
        stitches += star()
        stitches += [1, 1,] # move 0.1mm in the x direction and 0.1mm in the y direction
    
    stitches += [100,0,80,150] # spacing
    stitches += [128, 1] # change color
    
    # Create the circle fractal
    for i in range(6):
        stitches += circle(25) # Circle of radius 25mm

    stitches += [100,0,100,0,100,0,100,0,0,156] # Spacing
    stitches += [128, 1] # Change color
    
    # Create the edge fractals 
    for i in range(6):
        stitches += fractal()
    stitches += [128, 1] # Change color
    
    # Fill the edge fractals
    for i in range(5):
        stitches += filler_bottom()
        stitches += [256-50,0]
    stitches += filler_bottom()
    
    for i in range(4):
        stitches += filler_left()
        stitches += [0,50]
    stitches += filler_left()

    for i in range(5):
        stitches += filler_top()
        stitches += [50,0]
    stitches += filler_top()
    
    for i in range(4):
        stitches += filler_right()
        stitches += [0,256-50]
    stitches += filler_right()
    
    stitches += [128, 1] # Change color
    stitches += [131,0,131,0,] # Spacing
    
    # Create the triangular fractals on the corners
    stitches += right_bottom_corner()
    stitches += [136,0,136,0,]
    stitches += right_bottom_corner()
    
    stitches += [10,0,0,100,0,100,0,100,0,100,0,50,] # Spacing
    
    stitches += right_top_corner()
    stitches += [0,136,0,136,]
    stitches += right_top_corner()
    
    stitches += [0,10,156,0,156,0,156,0,156,0,156,0,156,0,] # Spacing
    
    stitches += left_top_corner()
    stitches += [120,0,120,0,]
    stitches += left_top_corner()
    
    stitches += [246,0,0,156,0,156,0,156,0,156,0,206,] # Spacing
    
    stitches += left_bottom_corner()
    stitches += [0,120,0,120,]
    stitches += left_bottom_corner()
    
    stitches += [128, 16]   # 128 = escape_character , 16=last_stitch 
    return stitches


# Function to create JEF file header

def getJefHeader(num_stitches):
    jefBytes = [    0, 0, 0, 0,   # The byte offset of the first stitch
                    10, 0, 0, 0,   # unknown command
                    ord("2"), ord("0"), ord("2"), ord("2"), #YYYY
                    ord("0"), ord("3"), ord("1"), ord("3"), #MMDD
                    ord("2"), ord("0"), ord("5"), ord("8"), #HHMM
                    ord("0"), ord("0"), 99, 0, #SS00
                      5, 0, 0, 0,   # Thread count nr. (nr of thread changes)
                    (num_stitches) & 0xff, (num_stitches) >> 8 & 0xff, 0, 0, # Number of stitches
                      3, 0, 0, 0, # Sewing machine Hoop
                    # Extent 1
                     100, 0, 0, 0, # Left boundary dist from center (in 0.1mm)
                     100, 0, 0, 0, # Top boundary dist from center (in 0.1mm)
                     100, 0, 0, 0, # Right boundary dist from center (in 0.1mm)
                     100, 0, 0, 0, # Bottom boundary dist from center (in 0.1mm)
                    # Extent 2
                     100, 0, 0, 0, # Left boundary dist from center (in 0.1mm)
                     100, 0, 0, 0, # Top boundary dist from center (in 0.1mm)
                     100, 0, 0, 0, # Right boundary dist from center (in 0.1mm)
                     100, 0, 0, 0, # Bottom boundary dist from center (in 0.1mm)
                    # Extent 3
                     100, 0, 0, 0, # Left boundary dist from center (in 0.1mm)
                     100, 0, 0, 0, # Top boundary dist from center (in 0.1mm)
                     100, 0, 0, 0, # Right boundary dist from center (in 0.1mm)
                     100, 0, 0, 0, # Bottom boundary dist from center (in 0.1mm)
                    # Extent 4
                     100, 0, 0, 0, # Left boundary dist from center (in 0.1mm)
                     100, 0, 0, 0, # Top boundary dist from center (in 0.1mm)
                     100, 0, 0, 0, # Right boundary dist from center (in 0.1mm)
                     100, 0, 0, 0, # Bottom boundary dist from center (in 0.1mm)
                    # Extent 5
                     100, 0, 0, 0, # Left boundary dist from center (in 0.1mm)
                     100, 0, 0, 0, # Top boundary dist from center (in 0.1mm)
                     100, 0, 0, 0, # Right boundary dist from center (in 0.1mm)
                     100, 0, 0, 0, # Bottom boundary dist from center (in 0.1mm)
                      10, 0, 0, 0, # Thread Color (Vermilion)
                      68, 0, 0, 0, # Thread Color (Canary Yellow)
                      1, 0, 0, 0, # Thread Color (Black)
                      30, 0, 0, 0, # Thread Color (Blue Ink)
                      3, 0, 0, 0, # Thread Color (Sunflower)
                     13, 0, 0, 0, # Thread type (unknown)
                ]
    return jefBytes

#Main program combines headers and stich sequence

def main():
    stitchseq = getStitchSequence()
    header = getJefHeader(len(stitchseq)//2)
    data = bytes(header) + bytes(stitchseq)
    with open("Digital Embroidery.jef", "wb") as f:
        f.write(data)

if __name__ == '__main__':
    main()
