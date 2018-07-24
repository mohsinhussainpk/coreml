# -*- coding: utf-8 -*-
"""
Created on Sun May 13 20:26:53 2018

@author: Rafa
"""

import cv2
import os

path_read = 'D:/Google Drive/Tailored by big data/projects/bouding box detector/code/upper/ssd_keras-master/datasets/udacity_driving_datasets/'
path_save = 'D:/Google Drive/Tailored by big data/projects/bouding box detector/code/upper/ssd_keras-master/datasets/udacity_driving_datasets_100/'

for image_name in os.listdir(path_read):
    img = cv2.imread(path_read + image_name)
    img_res = cv2.resize(img, (100, 100))
    cv2.imwrite(path_save + image_name, img_res)