# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GxcLqgzk3eS5hS-tYxsDHxeshCBpnTd-
"""

import matplotlib.pyplot as plt
import numpy as np # Changed 'numoy' to 'numpy'
# make data
x=np.linspace(0, 10, 100) #linspace funksiyasi kesmani bo'laklarga bo'ladi
print(x)
y=4+2*np.sin(2*x)
print (y)
# plot
fig, ax=plt.subplots() #platformani yaratish
ax.plot(x,y, linewidth=2.0)

plt.title('Sinus funksiyasining grafi')


plt.show()
plt.show() # Added parentheses to call the function

import matplotlib.pyplot as plt
import numpy as np

# make the data
np.random.seed(3)
x=4+np.random.normal(0, 2, 24)
y=4+np.random.normal(0, 2, len(x))
# size and color:
sizes=np.random.uniform(15, 80, len(x))
colors=np.random.uniform(15, 80, len(x))

# plot
fig, ax=plt.subplots()

ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()

pip install opencv-python

from google.colab.patches import cv2_imshow
import cv2
rasm=cv2.imread("/content/photo_5368615206701360391_y (1).jpg")
cv2_imshow(rasm)

oqqora=cv2.cvtColor(rasm,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)

from google.colab.patches import cv2_imshow
import cv2
rasm=cv2.imread("/content/photo_5368615206701360390_y.jpg")
cv2_imshow(rasm)

oqqora=cv2.cvtColor(rasm,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)