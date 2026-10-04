import cv2

image = cv2.imread("Basic\image.png")

if image is not None:
    cv2.imshow("window image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    
else:
    print("Image not found ")    

