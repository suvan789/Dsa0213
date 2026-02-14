import cv2


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Webcam not accessible")
else:
    print("Press 's' for Slow Motion")
    print("Press 'f' for Fast Motion")
    print("Press 'n' for Normal Speed")
    print("Press 'q' to Quit")

    delay = 30  

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Webcam Video", frame)

        key = cv2.waitKey(delay) & 0xFF

        if key == ord('s'):       
            delay = 100
        elif key == ord('f'):     
            delay = 10
        elif key == ord('n'):     
            delay = 30
        elif key == ord('q'):     
            break

cap.release()
cv2.destroyAllWindows()
