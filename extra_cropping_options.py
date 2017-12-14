
# newcameramtx, roi = cv2.getOptimalNewCameraMatrix(camera_mtx, dist_coeff, (w, h), 1, (w, h))
# im_cal = cv2.undistort(im, camera_mtx, dist_coeff, None, newcameramtx)
#
# # crop the image. ROI are all-good pixels regions in the image
# x,y,w,h = roi
# im_cal2 = im_cal[y:y+h, x:x+w]
#
# im_blend = cv2.addWeighted(im,0.5,im_cal,0.5,0)
#
# cv2.imshow('blend', im_blend)
#
# cv2.imshow('full_undist', im_cal)
#
# cv2.imshow('cut', im_cal2)
#
# cv2.imwrite('TEST_c_orig.jpg', im)
#
# cv2.imwrite('TEST_c_full_undist.jpg', im_cal)
