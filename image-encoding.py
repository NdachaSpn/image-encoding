# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 12:36:24 2022

@author: Simon
"""
#how to install liblaries
## pip install opencv-python
##pip install numpy
#import neccesary liblaries
import cv2
import numpy as np

#binarize data to be encoded
def to_bin(data):
    if isinstance(data,str):
        return ''.join([format(ord(i),"08b")for i in data])
    elif isinstance(data,bytes) or isinstance(data,np.ndarray):
        return [format(i,"08b") for i in data]
    elif isinstance(data,int)or isinstance(data, np.unit8):
        return format(data, "08b")
    else:
        raise TypeError("type not supported")
        
        
#encoding function
def encode (image_name, secret_data):
    image=cv2.imread(image_name)
    n_bytes=image.shape[0]*image.shape[1]*3//8
    if len(secret_data)>n_bytes:
        raise ValueError("insufficient bytes/ storage")
        
    print("[*] Encoding DATA....")
    secret_data +="====="
    data_index=0
    
    binary_secret_data=to_bin(secret_data)
    
    data_len=len(binary_secret_data)
    
    for row in image:
        for pixel in row:
            r,g,b=to_bin(pixel)
            
            if data_index<data_len:
                pixel[0]=int(r[:-1]+binary_secret_data[data_index],2)
                data_index+=1
                
            if data_index<data_len:
                pixel[1]=int(g[:-1] + binary_secret_data[data_index],2)
                data_index +=1
                
            if data_index<data_len:
                pixel[2]=int(b[:-1]+ binary_secret_data[data_index],2)
                data_index +=1
                
            if data_index >= data_len:
                break
                
    return image

#pass message and png to be encoded
input_image="C:/Users/Simon/Pictures/findme.png"
output_image="encoded_image.PNG"
secret_data="welcome..you found me. how can we do business"

encoded_image=encode(image_name=input_image, secret_data=secret_data)

#save encoded image
cv2.imwrite(output_image, encoded_image)
    
    