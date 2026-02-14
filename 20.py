import cv2

img = cv2.imread("image.png",0)

blur = cv2.GaussianBlur(img,(5,5),0)
A = 2
highboost = cv2.addWeighted(img,A,blur,-1,0)

cv2.imshow("High Boost", highboost)
cv2.waitKey(0)
cv2.destroyAllWindows()
