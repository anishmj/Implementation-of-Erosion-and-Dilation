#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[2]:


import numpy as np


# In[50]:


img = np.zeros((400,600),dtype = 'uint8')
img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
font = cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(img,'ANISH M J',(5,70),font,2,(255,0,255),5,cv2.LINE_AA)
## magneta


# In[51]:


#img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)


# In[52]:


cv2.imshow("text",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[28]:


kernel1 = cv2.getStructuringElement(cv2.MORPH_CROSS,(7,7))
erode = cv2.erode(img,kernel1)


# In[29]:


cv2.imshow("EROSION",erode)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[30]:


dilate = cv2.dilate(img,kernel1)
cv2.imshow("DILATION",dilate)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




