import cv2
import numpy as np


image = cv2.imread(r"D:\computervisionprograms\image.png")

if image is None:
    print("Error: Image not found")
else:
    
    height, width = image.shape[:2]

    
    tx = 100   
    ty = 50    

   
    translation_matrix = np.float32([[1, 0, tx],
                                     [0, 1, ty]])

    
    moved_image = cv2.warpAffine(image, translation_matrix, (width, height))
    cv2.imshow("Original Image", image)
    cv2.imshow("Moved Image", moved_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
