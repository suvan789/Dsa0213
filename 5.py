import cv2


image = cv2.imread(r"D:\computervisionprograms\image.png")

if image is None:
    print("Error: Image not found")
else:
   
    height, width = image.shape[:2]

    
    center = (width // 2, height // 2)

    
    rotate_clockwise = cv2.getRotationMatrix2D(center, -45, 1.0)
    clockwise_image = cv2.warpAffine(image, rotate_clockwise, (width, height))

   
    rotate_counter = cv2.getRotationMatrix2D(center, 45, 1.0)
    counter_image = cv2.warpAffine(image, rotate_counter, (width, height))

   
    cv2.imshow("Original Image", image)
    cv2.imshow("Clockwise Rotation", clockwise_image)
    cv2.imshow("Counter Clockwise Rotation", counter_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
