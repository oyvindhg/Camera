#conda install -c menpo opencv3


import cv2
import glob
import numpy as np

image_files = glob.glob('*.jpg')
board_size = (6,8)

objp = np.zeros((board_size[0]*board_size[1],3), np.float32)
objp[:,:2] = np.mgrid[0:board_size[0],0:board_size[1]].T.reshape(-1,2)

im_points = []
obj_points = []

h, w = 0, 0

for image_file in image_files:
    im = cv2.imread(image_file)
    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    (h, w) = im_gray.shape

    found, corners = cv2.findChessboardCorners(im_gray, board_size) #found is non-zero if all corners are found

    if found == True:

        # termination criteria
        term = (cv2.TERM_CRITERIA_MAX_ITER + cv2.TERM_CRITERIA_EPS, 30, 0.001)

        # Improve the corner positions on a sub-pixel level (increases the RMS)
        cv2.cornerSubPix(im_gray, corners, (5, 5), (-1, -1), term)

        im_points.append(corners)
        obj_points.append(objp)

        # Draw and display the corners
        #img = cv2.drawChessboardCorners(im, board_size, corners, ret)
        #cv2.imshow('img', im)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()


rms, camera_mtx, dist_coeff, rotation, translation = cv2.calibrateCamera(obj_points, im_points, (w, h), None, None)

if (rms > 1):
    print('Bad calibration. RMS error: ', rms)

im = cv2.imread('right.jpg')
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(camera_mtx, dist_coeff, (w, h), 1, (w, h))
dst = cv2.undistort(im, camera_mtx, dist_coeff, None, newcameramtx)

# crop the image. ROI are all-good pixels regions in the image
x,y,w,h = roi
dst = dst[y:y+h, x:x+w]
cv2.imshow('img', dst)

dst = cv2.undistort(im, camera_mtx, dist_coeff)

cv2.imshow('im2', dst)


cv2.waitKey(0)

