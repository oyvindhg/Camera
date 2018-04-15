import freenect
from libfreenect.wrappers.python import frame_convert2
import numpy as np
import darknet.run_python as dn
import os, time
from show_image import show_labeled
import cv2
from create_3D_model import plot_3d

depth_x = 480
depth_y = 640

DEPTH_REGISTERED   = 4        # processed depth data in mm, aligned to 640x480 RGB
DEPTH_MM           = 5        # depth to each pixel in mm, but left unaligned to RGB image

# cv2.namedWindow('Depth')        #10 bits: Depth is from 0 to 1023. 11th bit gives 2047 if the IR can't read the pattern from the IR projector
# cv2.namedWindow('Image')
print('Press ESC in window to stop')



def show_depth(depth_image):
    depth_im = frame_convert2.pretty_depth_cv(depth_image)
    cv2.imshow('Depth', depth_im)

def show_image(image):
    cv2.imshow('Image', image)

def get_depth():
    return freenect.sync_get_depth(format=DEPTH_MM)[0]

def get_image():
    return frame_convert2.video_cv(freenect.sync_get_video()[0])

def get_image_and_depth():
    im, depth = freenect.synch_get_video_and_depth()
    return frame_convert2.video_cv(im[0]), depth[0]

def color_to_depth(image, depth_image):
    return freenect.color_to_depth(image, depth_image)


def depth_to_xyz(depth_image):
    return freenect.depth_to_xy(depth_image)


a = get_depth()
im_pre = get_image()
im = color_to_depth(im_pre, a)

#
# print("ok")
m = depth_to_xyz(a)
#
# #print(m)
#
# m = np.zeros((2,3,3))
# # #
# m[0][1][0] = 5
# m[1][1][0] = 2.5
# m[0][0][2] = 5
# m[0][2][1] = 2.5
#

plot_3d(m, im)

show_image(im)

cv2.waitKey()
#
#
#
quit()

cont = True
while cont:
    a = get_depth()
    im = get_image()


    same = color_to_depth(im, a)



    show_depth(a)
    show_image(same)



    # main_path = os.getcwd()
    # main_path = os.getcwd()
    # net_path = main_path + '/darknet'
    # os.chdir(net_path)
    #
    # method = "yolo"
    #
    # if method == "yolo9000":
    #     config = b"cfg/yolo9000.cfg"
    #     weights = b"yolo9000.weights"
    #     metadata = b"cfg/combine9k.data"
    # else:
    #     config = b"cfg/yolo.cfg"
    #     weights = b"yolo.weights"
    #     metadata = b"cfg/coco.data"
    #
    # dn.init(net_path)
    # net = dn.load_net(config, weights, 0)
    # meta = dn.load_meta(metadata)
    # boxes = dn.detection2(net, meta, im)
    # print('boxes:', boxes)

    # boxes = [(b'bicycle', 0.8509225845336914, (341.80010986328125, 285.9195861816406, 493.32745361328125, 324.6991882324219))]

    #show_labeled(im, boxes)

    #idea: extend registration.c/freenect_map_rgb_to_depth so that it takes left top and bottom right corner of BBs and finds new BBs


    if cv2.waitKey(10) == 27:
        break