
import glob
import numpy as np
import cv2

def calibrate(resize):

    image_files = glob.glob('*.JPG')
    board_size = (6, 9)

    objp = np.zeros((board_size[0] * board_size[1], 3), np.float32)
    objp[:, :2] = np.mgrid[0:board_size[0], 0:board_size[1]].T.reshape(-1, 2)

    im_points = []
    obj_points = []

    h, w = 0, 0

    for image_file in image_files:
        im = cv2.imread(image_file)

        im = cv2.resize(im, None, fx=resize, fy=resize, interpolation=cv2.INTER_CUBIC)

        im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        (h, w) = im_gray.shape

        print(image_file)

        found, corners = cv2.findChessboardCorners(im_gray, board_size)  # found is non-zero if all corners are found

        if found == True:

            print('ok')

            # termination criteria
            term = (cv2.TERM_CRITERIA_MAX_ITER + cv2.TERM_CRITERIA_EPS, 30, 0.001)

            # Improve the corner positions on a sub-pixel level (increases the RMS)
            cv2.cornerSubPix(im_gray, corners, (5, 5), (-1, -1), term)

            im_points.append(corners)
            obj_points.append(objp)

            if image_file == "GOPR0857.JPG":
                # Draw and display the corners
                cv2.drawChessboardCorners(im, board_size, corners, found)
                cv2.imwrite('TEST_c_orig.jpg', im)
                cv2.imshow('img', im)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

    return cv2.calibrateCamera(obj_points, im_points, (w, h), None, None)
