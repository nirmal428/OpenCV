import cv2

image = cv2.imread("Basic\image.png")

if image is None:
    print("error : Image not found")
else:
    print("Image load successfully")    

