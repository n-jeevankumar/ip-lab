import cv2
import numpy as np

# Load an image
image = cv2.imread('D:\\057\\tiger-jpg.jpg')


rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Original Image', image)
cv2.waitKey(0)
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)


h, w = image.shape[:2]
scale_factor = 0.5
scaled_image = cv2.resize(image, (int(w * scale_factor), int(h * scale_factor)))
cv2.imshow('Scaled Image', scaled_image)
cv2.waitKey(0)


translation = np.float32([[1, 0, 100], [0, 1, 30]])
translated_image = cv2.warpAffine(image, translation, (w, h))
cv2.imshow('Translated Image', translated_image)
cv2.waitKey(0)
