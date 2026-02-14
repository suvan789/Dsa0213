import cv2
import numpy as np


cap = cv2.VideoCapture(r"D:\computervisionprograms\video.mp4")

if not cap.isOpened():
    print("Error: Video not found")
else:
    ret, frame = cap.read()
    if not ret:
        print("Error: Cannot read video")
    else:
        height, width = frame.shape[:2]

       
        src_points = np.float32([
            [0, 0],
            [width - 1, 0],
            [0, height - 1],
            [width - 1, height - 1]
        ])

        
        dst_points = np.float32([
            [50, 50],
            [width - 100, 40],
            [80, height - 80],
            [width - 50, height - 50]
        ])

        
        matrix = cv2.getPerspectiveTransform(src_points, dst_points)

        
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            
            transformed = cv2.warpPerspective(frame, matrix, (width, height))

            
            cv2.imshow("Original Video", frame)
            cv2.imshow("Perspective Transformed Video", transformed)

            if cv2.waitKey(30) & 0xFF == ord('q'):
                break

cap.release()
cv2.destroyAllWindows()
