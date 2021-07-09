import os

path = os.path.join(os.getcwd(), 'test images & csv')

files = os.listdir(path)

for i in files:
    j = i.replace('.jpg.jpg', '.jpg')
    #print(j)
    os.rename(f'{path}/{i}', f'{path}/{j}')
