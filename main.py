import cv2
import glob

image_files = glob.glob('*.jpg')

for image_file in image_files:
    image = cv2.imread(image_file)
