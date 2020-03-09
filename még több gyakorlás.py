# -*- coding: utf-8 -*-

import cv2
from matplotlib import pyplot as plt
import os

image_path = r"C:\Users\Ildikó\Desktop\proba.png"
image_path = r"C:\proba.png"


image = cv2.imread(image_path)

plt.figure()
plt.imshow(image[:, :, 0])
#plt.close()

blur=cv2.GaussianBlur(image,(5,5),0)

plt.figure()
plt.imshow(blur[:, :, 0])


from scipy import misc

import matplotlib.pyplot as plt


fig = plt.figure()


  # show the filtered result in grayscale

ax1 = fig.add_subplot(121)  # left side

ax2 = fig.add_subplot(122)  # right side

ascent = misc.ascent()

result = gaussian_filter(ascent, sigma=5)

ax1.imshow(ascent)

ax2.imshow(result)

plt.show()