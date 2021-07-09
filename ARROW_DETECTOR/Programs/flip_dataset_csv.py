import cv2
import os
import pandas as pd
import numpy as np
import time

df = pd.read_csv('right test images & csv/test_labels.csv')
column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
list_filename = []
img_width = 640
img_height = 480
#For Right Arrow
#obj_class = 'right_arrow'
#For Left Arrow
obj_class = 'left_arrow'
new_data = []

for i in df.index:
    phot = cv2.imread(os.path.join(os.getcwd(), 'right test images & csv', df['filename'][i]))
# For Left Arrow
    name = df['filename'][i]
    hor_flip = cv2.flip(phot, 1)
    cv2.imwrite(f'/home/anirudh_/images/right test images & csv/L{name}.jpg', hor_flip)
    hor_flip = cv2.rectangle(hor_flip,(640-df['xmin'][i],df['ymin'][i]),(640-df['xmax'][i],df['ymax'][i]),(0,0,255),2)
    cv2.imshow("FLIPPED_VIEW", hor_flip)
    data = (f'L{name}', img_width, img_height, obj_class, 640-df['xmin'][i], df['ymin'][i], 640-df['xmax'][i], df['ymax'][i])
#For Right Arrow
    # cv2.imwrite(f'/home/anirudh_/More Images/R 0/{j}.jpg', phot)
    # phot = cv2.rectangle(phot,(df['xmin'][i],df['ymin'][i]),(df['xmax'][i],df['ymax'][i]),(255,0,0),2)
    # cv2.imshow("ACTUAL_VIEW", phot)
    # data = (f'{j}', img_width, img_height, obj_class, df['xmin'][i], df['ymin'][i], df['xmax'][i], df['ymax'][i])
    new_data.append(data)
    new_df = pd.DataFrame(new_data, columns=column_name)
    time.sleep(0.05)
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

#For Left Arrow
new_df.to_csv('test.csv', index=None)

#For Right Arrow
# new_df.to_csv('train_right_more.csv', index=None)
