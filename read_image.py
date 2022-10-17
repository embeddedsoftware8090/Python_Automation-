import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('memory.PNG', cv2.IMREAD_GRAYSCALE)

cv2.imshow('memory',img)
cv2.waitKey(0)
#cv2.destroyAllWindows()