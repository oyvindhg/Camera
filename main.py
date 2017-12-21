#conda install -c menpo opencv3


import darknet.run_python as dn
import cv2
import os
from calibration import calibrate
from show_image import show_labeled

resize = 0.3
main_path = os.getcwd()
im_path = main_path + '/GoPro'

os.chdir(im_path)
rms, camera_mtx, dist_coeff, rotation, translation = calibrate(resize)
if (rms > 1):
    print('Bad calibration. RMS error: ', rms)

os.chdir(main_path)

im = cv2.imread('Test_images/GOPR0943.JPG')
im = cv2.resize(im, None, fx=resize, fy=resize, interpolation=cv2.INTER_CUBIC)
cv2.imshow('orig', im)
cv2.imwrite('orig.jpg', im)
im_undist = cv2.undistort(im, camera_mtx, dist_coeff)
cv2.imshow('undist', im_undist)
cv2.imwrite('im_undist.jpg', im_undist)
cv2.waitKey(0)



# im = cv2.resize(im, None, fx=resize, fy=resize, interpolation=cv2.INTER_CUBIC)
# im = cv2.undistort(im, camera_mtx, dist_coeff)
# cv2.imshow('undist', im)
# cv2.waitKey(0)

net_path = main_path + '/darknet'
os.chdir(net_path)

method = "yolo"

if method == "yolo9000":
    config = b"cfg/yolo9000.cfg"
    weights = b"yolo9000.weights"
    metadata = b"cfg/combine9k.data"
else:
    config = b"cfg/yolo.cfg"
    weights = b"yolo.weights"
    metadata = b"cfg/coco.data"


dn.init(net_path)
net = dn.load_net(config, weights, 0)
meta = dn.load_meta(metadata)
boxes = dn.detection2(net, meta, im_undist)
print(boxes)

#boxes = [(b'bicycle', 0.8509225845336914, (341.80010986328125, 285.9195861816406, 493.32745361328125, 324.6991882324219))]

show_labeled(im_undist, boxes)