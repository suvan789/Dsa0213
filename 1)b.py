import cv2


image = cv2.imread(r"D:\computervisionprograms\image2.png")

if image is None:
    print("Error: Image not found")
else:
    
    blurred_image = cv2.GaussianBlur(image, (7, 7), 0)

    
    cv2.imshow("Original Image", image)
    cv2.imshow("Gaussian Blurred Image", blurred_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
