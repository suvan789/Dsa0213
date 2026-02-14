import cv2
import numpy as np


image = cv2.imread(r"D:\computervisionprograms\image.png")

if image is None:
    print("Error: Image not found")
else:
    height, width = image.shape[:2]

    
    src_pts = np.float32([
        [50, 50],
        [width - 50, 50],
        [50, height - 50],
        [width - 50, height - 50]
    ])

    
    dst_pts = np.float32([
        [10, 100],
        [width - 100, 50],
        [100, height - 50],
        [width - 50, height - 100]
    ])

   
    H, status = cv2.findHomography(src_pts, dst_pts)

    
    homography_image = cv2.warpPerspective(image, H, (width, height))

   
    cv2.imshow("Original Image", image)
    cv2.imshow("Homography Transformed Image", homography_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
