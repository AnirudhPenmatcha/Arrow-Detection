import cv2
import pandas as pd
from PIL import Image
import os

path = r"/home/anirudh_/PROJECTS/ARROW_DETECTOR/LOGITECH_IMAGES"
full_labels = pd.read_csv(path + '/train.csv')


def draw_boxes(image_name):
    selected_value = full_labels[full_labels.filename == image_name]
    img = cv2.imread(path + '/train images right/{}'.format(image_name), 0)
    for index, row in selected_value.iterrows():
        #img = cv2.rectangle(img, (row['xmin'], row['ymin']), (row['xmax'], row['ymax']), (0, 255, 0), 3)
        print(row['filename'])

        #cv2.imwrite(path + '/left/L{}'.format(row['filename']), cv2.flip(img[row['ymin']:row['ymax'], row['xmin']:row['xmax']], 1))
        #cv2.imshow('box', img[row['ymin']:row['ymax'], row['xmin']:row['xmax']])
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    return img


for filename in os.listdir(path + '/train images right'):
    draw_boxes(filename)
    #cv2.imwrite()
    #cv2.imshow('box', boxed_image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
