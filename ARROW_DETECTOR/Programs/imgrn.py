import os

# Function to rename multiple files
def main():
    path = r"/home/anirudh_/PROJECTS/ARROW_DETECTOR/LOGITECH_IMAGES/train images"
    for filename in os.listdir(path):
        
        print(filename)
        src = filename
        if(filename.endswith('.jpg.jpg') == 1):
            filename = filename.replace(".jpg.jpg", ".jpg")
            os.rename(path + "/{}".format(src), path + "/{}".format(filename))
            print(filename)
            #os.remove(path + "/{}".format(filename))
if __name__ == '__main__':
    main()
