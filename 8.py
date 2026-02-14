import cv2
import numpy as np


image = cv2.imread(r"D:\computervisionprograms\image.png")

if image is None:
    print("Error: Image not found")
else:
    height, width = image.shape[:2]

    
    src_points = np.float32([
        [0, 0],
        [width - 1, 0],
        [0, height - 1],
        [width - 1, height - 1]
    ])

    
    dst_points = np.float32([
        [50, 50],
        [width - 100, 30],
        [70, height - 80],
        [width - 50, height - 50]
    ])

    matrix = cv2.getPerspectiveTransform(src_points, dst_points)

   
    perspective_image = cv2.warpPerspective(image, matrix, (width, height))

    
    cv2.imshow("Original Image", image)
    cv2.imshow("Perspective Transformed Image", perspective_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
