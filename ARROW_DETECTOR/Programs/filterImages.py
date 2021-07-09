import os
import cv2

images = os.listdir("/home/anirudh_/images/")
#images.sort()
j = 0
length = len(images)
for i in images:
    img = cv2.imread(r"/home/anirudh_/images/" + i, 1)
    print(i, j, length)
    j+=1
    cv2.imshow(i, img)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        continue
    elif cv2.waitKey(0) & 0xFF == ord('e'):
        cv2.destroyAllWindows()
        os.remove(i)
