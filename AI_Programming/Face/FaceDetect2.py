#example 6.6

import cv2
import face_recognition

image = cv2.imread('./pics/face0.jpg')
cv2.imshow('photo', image)

rgb_frame = image[:, :, ::-1] #convert to RGB format
face_locations = face_recognition.face_locations(rgb_frame)

count = 0
for face_location in face_locations:
    count = count + 1
    top, right, bottom, left = face_location
    print("Face {} Top: {}, Left: {}, Bottom: {}, Right: {}").format(count, top, left, bottom, right)
    face_image = image[top:bottom, left:right]
    title = "face = str(count)"
    cv.imshow(title, face_image)



cv2.waitKey(0)
cv2.destroyAllWindows
                 
    