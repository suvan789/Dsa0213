import cv2


video = cv2.VideoCapture(r"D:\computervisionprograms\video.mp4")

if not video.isOpened():
    print("Error: Video not found")
else:
    print("Press 'q' to quit")

    while True:
        ret, frame = video.read()

        if not ret:
            break

        cv2.imshow("Video Playback", frame)

     

        key = cv2.waitKey(30)   

        if key == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()
