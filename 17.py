import cv2, numpy as np

img = cv2.imread("image.png",0)

kernel = np.array([[-1,-1,-1],
                   [-1,8,-1],
                   [-1,-1,-1]])

sharp = cv2.filter2D(img,-1,kernel)

cv2.imshow("Laplacian Diagonal", sharp)
cv2.waitKey(0)
cv2.destroyAllWindows()
