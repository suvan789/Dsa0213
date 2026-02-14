import cv2


image = cv2.imread(r"D:\computervisionprograms\image.png")

if image is None:
    print("Error: Image not found")
else:
    
    height, width = image.shape[:2]

   
    bigger = cv2.resize(image, (width*2, height*2), interpolation=cv2.INTER_LINEAR)

    
    smaller = cv2.resize(image, (width//2, height//2), interpolation=cv2.INTER_AREA)

  
    cv2.imshow("Original Image", image)
    cv2.imshow("Bigger Image", bigger)
    cv2.imshow("Smaller Image", smaller)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
