#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import pyplot as plt
import cv2
import numpy as np


# In[8]:


def display_image(title, img):
    if img.ndim == 3:
        img = img[:,:,::-1]
    plt.title(title)
    plt.imshow(img, cmap="gray")
    plt.show()

