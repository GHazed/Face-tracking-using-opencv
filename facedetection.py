import os

import cv2


imagepath =os.path.join('','data','human4.jpeg')

img= cv2.imread(imagepath)
print(img.shape)

#convert the image to gray scale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray_image.shape)


#load the classifier Haar Cascade 
face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

face = face_classifier.detectMultiScale(
    gray_image, scaleFactor= 1.3, minNeighbors=2
)


#draw a bounding box
for(x, y, w, h) in face:
    cv2.rectangle(img,(x,y),(x+w,y+h), (0, 255, 0), 2)


cv2.imshow('Detected face', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


