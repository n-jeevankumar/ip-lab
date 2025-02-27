import cv2
import numpy as np

# Load an image
image = cv2.imread('D:\python\g4g.png')

# 1. Resizing the image
resized_image = cv2.resize(image, (400, 400))

# 2. Cropping the image (x1, y1, x2, y2)
cropped_image = image[50:200, 50:200]

# 3. Converting to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 4. Thresholding (binary thresholding)
_, thresholded_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# 5. Blurring the image (Gaussian blur)
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

# 6. Edge detection using Canny
edges = cv2.Canny(image, 100, 200)

# 7. Drawing a rectangle (start_point, end_point, color, thickness)
rectangle_image = image.copy()
cv2.rectangle(rectangle_image, (50, 50), (200, 200), (0, 255, 0), 3)

# 8. Drawing a circle (center, radius, color, thickness)
circle_image = image.copy()
cv2.circle(circle_image, (300, 300), 100, (0, 255, 255), -1)

# 9. Drawing a line (start_point, end_point, color, thickness)
line_image = image.copy()
cv2.line(line_image, (50, 50), (300, 300), (255, 0, 0), 5)

# 10. Rotating the image
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1)
rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))

# 11. Flipping the image (horizontal flip)
flipped_image_h = cv2.flip(image, 1)

# 12. Flipping the image (vertical flip)
flipped_image_v = cv2.flip(image, 0)

# 13. Applying perspective transform
pts1 = np.float32([[50, 50], [200, 50], [50, 200], [200, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250], [200, 200]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
perspective_image = cv2.warpPerspective(image, matrix, (w, h))

# 14. Applying a filter (Laplacian filter)
laplacian_image = cv2.Laplacian(gray_image, cv2.CV_64F)

# 15. Adding text on the image
text_image = image.copy()
cv2.putText(text_image, 'hi', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

# Display images (for each operation, you can choose to display the result)
cv2.imshow('Original', image)
cv2.waitKey(3000)
cv2.imshow('Resized', resized_image)
cv2.waitKey(3000)
cv2.imshow('Cropped', cropped_image)
cv2.waitKey(3000)
cv2.imshow('Gray', gray_image)
cv2.waitKey(3000)
cv2.imshow('Thresholded', thresholded_image)
cv2.waitKey(3000)
cv2.imshow('Blurred', blurred_image)
cv2.waitKey(3000)
cv2.imshow('Edges', edges)
cv2.waitKey(3000)
cv2.imshow('Rectangle', rectangle_image)
cv2.waitKey(3000)
cv2.imshow('Circle', circle_image)
cv2.waitKey(3000)
cv2.imshow('Line', line_image)
cv2.waitKey(3000)
cv2.imshow('Rotated', rotated_image)
cv2.waitKey(3000)
cv2.imshow('Flipped Horizontal', flipped_image_h)
cv2.waitKey(3000)
cv2.imshow('Flipped Vertical', flipped_image_v)
cv2.waitKey(3000)
cv2.imshow('Perspective Transform', perspective_image)
cv2.waitKey(3000)
cv2.imshow('Laplacian', laplacian_image)
cv2.waitKey(3000)
cv2.imshow('Text', text_image)
cv2.waitKey(3000)


cv2.destroyAllWindows()
