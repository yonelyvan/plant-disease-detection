
import cv2 as cv
import numpy as np
#import matplotlib.pyplot as plt
#from scipy.signal import find_peaks_cwt
#from consts import *
#from math import ceil

def mask_hist_eq(mat):
	hist = cv.calcHist([mat], [0], mat, [256], [0, 256]).ravel().astype(np.uint8)
	lut = hist.cumsum()
	lut = 255 * lut / lut[-1]
	lut = np.round(lut).astype(np.uint8)
	mat = cv.LUT(mat, lut)
	return mat



# Load an color image in grayscale
img = cv.imread('img_oscuro.jpg',0)
cv.imshow('Original',img)
img=mask_hist_eq(img)
cv.imshow('Ecualizado',img)
cv.waitKey(0)
cv.destroyAllWindows()
