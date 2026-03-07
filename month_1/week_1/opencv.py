# import cv2

# img = cv2.imread("image.jpeg")
# cv2.imshow("Image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import cv2 as cv
# import random

# img = cv.imread("./image.jpeg")

# if img is None:
#     sys.exit("Could not read the image.")

# cv.imshow("Display window", img)
# k = cv.waitKey(0)

# if k == ord("s"):
#     cv.imwrite("starry_night.png", img)

# for r in range(100):
#     for c in range(img.shape[1]):
#         img[r][c]= [random.randint(254, 255), random.randint(254, 255), random.randint(254, 255)]

# cv.imshow("Im", img)
# cv.waitKey(1000)
# cv.destroyAllWindows()


# Task 1 for CV intermediate to Advanced Learning 
# 1 Automatic Document Scanner
# import cv2 as cv
# img = cv.imread("./image.jpeg")

import numpy as np
import cv2 as cv

# img = cv.imread('messi5.jpg', cv.IMREAD_GRAYSCALE)
# assert img is not None, "file could not be read, check with os.path.exists()"

# res = cv.resize(img,None,fx=2, fy=2, interpolation = cv.INTER_CUBIC)

# #OR

# height, width = img.shape[:2]
# res = cv.resize(img,(2*width, 2*height), interpolation = cv.INTER_CUBIC)
# cv.imshow("Im", img)
# cv.waitKey(0)
# cv.destroyAllWindows()

# import numpy as np

# pts1 = np.float32([
# [56,65],
# [368,52],
# [28,387],
# [389,390]
# ])

# print(pts1)


# import cv2

# img = cv2.imread("image.jpeg")

# # Print original size
# print("Original shape:", img.shape)

# row = int(img.shape[0]/3)
# col = int(img.shape[1]/3)
# # TODO: resize the image to 50%
# resized = cv2.resize(img, (col, row))
# fliped_image = cv2.flip(resized, -1)
# cv2.imshow("Original", img)
# cv2.imshow("Resized", resized)
# cv2.imshow("Fliped", fliped_image)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


import cv2

img = cv2.imread('image.jpeg')
# resized = cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))
# horizontal = cv2.flip(resized, 1)
# vertical = cv2.flip(resized, 0)
# bothAxisFlip = cv2.flip(resized, -1)

# cv2.imshow("Original",img)
# cv2.imshow("Resized",resized)
# cv2.imshow("Horizontal",horizontal)
# cv2.imshow("vertical",vertical)
# cv2.imshow("Both azes Flip",bothAxisFlip)

# cv2.imwrite("Resized.jpg",resized)
# cv2.imwrite("Horizontal.jpg",horizontal)
# cv2.imwrite("vertical.jpg",vertical)
# cv2.imwrite("Both.jpg",bothAxisFlip)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


row, col = img.shape[:2]
center = (row/2,col/2)
M= cv2.getRotationMatrix2D(center, 30,1)

resize = cv2.resize(img, (int(img.shape[0]/2), int(img.shape[1]/2)))
rotated = cv2.warpAffine(resize, M, (col, row))
cv2.imshow("Rotated", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()