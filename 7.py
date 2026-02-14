import cv2
import numpy as np

image = cv2.imread(r"D:\computervisionprograms\image.png")

if image is None:
    print("Error: Image not found")
else:
    height, width = image.shape[:2]

 
    src_pts = np.float32([
        [0, 0],
        [width - 1, 0],
        [0, height - 1]
    ])

    
    dst_pts = np.float32([
        [50, 50],
        [width - 100, 50],
        [50, height - 100]
    ])

    
    affine_matrix = cv2.getAffineTransform(src_pts, dst_pts)

    
    affine_image = cv2.warpAffine(image, affine_matrix, (width, height))

   
    cv2.imshow("Original Image", image)
    cv2.imshow("Affine Transformed Image", affine_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
