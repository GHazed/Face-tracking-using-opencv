import os

import cv2


img =cv2.imread(os.path.join('.', 'data', 'Image_human1.png'))

resized_img = cv2.resize(img, (306, 205)) #(width, height) whereas in shape(height, width)
print(img.shape)
print(resized_img.shape)

cv2.imshow('img',img)
cv2.imshow('resized_img',resized_img)
cv2.waitKey(0)
