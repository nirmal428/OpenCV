import cv2

image = cv2.imread("Basic\image.png")

if image is not None:
    h,w,c = image.shape
    print(f"Image Loaded :\n Hieght: {h}\n width:{w}\n channels: {c}")
else:
    print("Image not Load")    