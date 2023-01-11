import cv2
import numpy as np

img = cv2.imread('./image/fig4.jpg', 0)
_, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# hit in origin
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (21,21))
dst = cv2.erode(img, kernel)

# get new SE
kernelC = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25,25))
kernelC = 1 - kernelC
ker = np.ones((3,3), dtype = np.uint8)
kernelC = kernelC - cv2.erode(kernelC, ker)

# hit in complement
imgC = 255 - img
dstC = cv2.erode(imgC, kernelC)

# anding and dilating
dst = cv2.bitwise_and(dst, dstC)
dst = cv2.dilate(dst, kernel)
cv2.imwrite('./result/Overlapping.jpg', dst)

cv2.imwrite('./result/Non-overlapping.jpg', cv2.morphologyEx((img - dst), cv2.MORPH_OPEN, ker))


# problem 1
#dst = cv2.erode(img, kernel)
#mask_shape = (dst.shape[0] - 20, dst.shape[1] - 20)
#mask = np.zeros(mask_shape, dtype = np.uint8)
#mask = cv2.copyMakeBorder(mask, 10,10,10,10, cv2.BORDER_CONSTANT, value = 255)

#dst = cv2.bitwise_and(dst, mask)
#dst = cv2.dilate(dst, kernel)
#cv2.imwrite('./result/Edge.jpg', dst)


# determine kernel size
#for sz in range(11,30,2):
#    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(sz,sz))
#    dst = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
#    print(f"size: {sz}*{sz}, counts:", len(np.nonzero(dst)[0]))
#kernel_edge = np.hstack([np.zeros([31,10]), np.ones([31,1])])
#kernel_edge[0][0] = 1;
#kernel_edge = kernel_edge.astype(np.uint8)
#kernel = np.ones((sz, sz), dtype = np.uint8)
#cv2.imshow('before', img)
#cv2.waitKey(0)
