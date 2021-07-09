function images = loadImages()

files = dir(['/home/anirudh_/PROJECTS/ARROW_DETECTOR/LOGITECH_IMAGES/right' '*.jpg'])

images = zeros(643, 2);

for i = 1:length(files)
    
  images = size(imread(['/home/anirudh_/PROJECTS/ARROW_DETECTOR/LOGITECH_IMAGES/right/' files(643).name]))

end
