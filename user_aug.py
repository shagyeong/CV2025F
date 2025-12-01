import numpy as np
import cv2

from user_shear   import user_shear
from user_spnoise import user_spnoise


src=cv2.imread("./assets/person.jpg",cv2.IMREAD_COLOR)
cv2.imshow("src",src)

dst_user_shear=  user_shear(src)
dst_user_spnoise=user_spnoise(src,3000)
cv2.imshow("dst_user_shear",  dst_user_shear)
cv2.imshow("dst_user_spnoise",dst_user_spnoise)
cv2.waitKey(0)
