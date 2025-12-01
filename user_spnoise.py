import numpy as np
import cv2

def user_spnoise(src,n):
    r=src.shape[:2][0]             # row size
    c=src.shape[:2][1]             # column size
    dst=src

    # salt(255)
    for _ in range(n):
        y=np.random.randint(0,r)
        x=np.random.randint(0,c)
        dst[y,x]=255
    
    # pepper(0)
    for _ in range(n):
        y=np.random.randint(0,r)
        x=np.random.randint(0,c)
        dst[y,x]=0
    return dst