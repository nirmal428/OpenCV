import cv2

image = cv2.imread("Basic\image.png")

if image is not None:
    success = cv2.imwrite("output_python.png" , image)
    if success:
        print("Image saved as output_python.png")
    else:
        print("Fail to save the image ")
else:
    print("error : image not found")

        