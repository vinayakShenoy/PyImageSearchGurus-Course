#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import pyplot as plt
import cv2
import numpy as np


# In[8]:

def show_image():
    plt.show()

def display_image(title, img, render_image=True):
    if img.ndim == 3:
        img = img[:,:,::-1]
    plt.title(title)
    plt.imshow(img, cmap="gray")
    if render_image:
        show_image()
    
def create_subplot(fig, rows, columns, i, title, img):
    fig.add_subplot(rows, columns, i)
    display_image(title,img, render_image=False)