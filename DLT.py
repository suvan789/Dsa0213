import cv2, numpy as np

img = cv2.imread("image.png")
h, w = img.shape[:2]

p1 = np.float32([[0,0],[w,0],[0,h],[w,h]])
p2 = np.float32([[20,50],[w-40,20],[50,h-40],[w-20,h-20]])

H = cv2.findHomography(p1, p2)[0]

cv2.imshow("DLT", cv2.warpPerspective(img, H, (w,h)))
cv2.waitKey(0)
cv2.destroyAllWindows()
