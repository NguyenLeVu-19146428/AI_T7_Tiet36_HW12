import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(30)
    if img_counter < 100:
        img_name = "./data/1/{}.jpg".format(img_counter)
        
        cv2.imwrite(img_name, frame)
    else:
        break
    img_counter += 1

cam.release()

cv2.destroyAllWindows()