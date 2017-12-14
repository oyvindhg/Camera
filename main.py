#conda install -c menpo opencv3

import darknet.python.darknet as dn

import cv2
import os
from calibration import calibrate

resize = 0.3
main_path = os.getcwd()
im_path = main_path + '/GoPro'

os.chdir(im_path)
# rms, camera_mtx, dist_coeff, rotation, translation = calibrate(resize)
# if (rms > 1):
#     print('Bad calibration. RMS error: ', rms)
# im = cv2.imread('GOPR0857.JPG')
# im = cv2.resize(im, None, fx=resize, fy=resize, interpolation=cv2.INTER_CUBIC)
# cv2.imshow('orig', im)
# dst = cv2.undistort(im, camera_mtx, dist_coeff)
# cv2.imshow('undist', dst)
# cv2.imwrite('TEST_c_undist.jpg', dst)
#cv2.waitKey(0)

im = cv2.imread('GOPR0857.JPG')
os.chdir(main_path)

config = b"cfg/yolo.cfg"
weights = b"yolo.weights"
metadata = b"cfg/coco.data"

net = dn.load_net(config, weights, 0)
meta = dn.load_meta(metadata)

r = dn.detect(net, meta, im)