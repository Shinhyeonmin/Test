import cv2
import time

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

custom_img = cv2.imread('Lady.jpg', cv2.IMREAD_COLOR)

font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX

while True:
    # Capture frame_by_frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=10,
        minSize=(30, 30),
    )
    cv2.line(frame, (0,35), (1600, 35), (0, 255, 100), 4)
    cv2.putText(frame, 'SNOWMAN~*~*', (30, 30), font, 1,
                (0, 0, 255), 2)

    #Draw a rectangle on the face

    for (x, y, w, h) in faces:
        #cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), 2)
        cv2.circle(frame, (x+100, y-95), 40, (255, 255, 255), -1)
        cv2.circle(frame, (x + 100, y-135), 35, (255, 255, 255), -1)
        cv2.circle(frame, (x-50, y+5), 40, (255, 255, 255), -1)
        cv2.circle(frame, (x-50, y-35), 35, (255, 255, 255), -1)
        cv2.circle(frame, (x+300, y+5), 40, (255, 255, 255), -1)
        cv2.circle(frame, (x+300, y-35), 35, (255, 255, 255), -1)
        cv2.putText(frame, 'Hello', (x+67, y-115), font, 1,(0, 0, 0), 2)
        cv2.putText(frame, 'My', (x-75, y-15), font, 1, (0, 0, 0), 2)
        cv2.putText(frame, 'Friend', (x+260, y-15), font, 1, (0, 0, 0), 2)


    #Display the resulting frame
    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()