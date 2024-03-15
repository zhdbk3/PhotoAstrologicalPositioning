import cv2
import numpy as np

image = cv2.imread('clear.jpg')

# 边缘检测
edges = cv2.Canny(image, 50, 150)

# 检测直线
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=10)
line_list: list[tuple[float, float]] = []   # [(k, b), ...]

for line in lines:
    x1, y1, x2, y2 = line[0]
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    line_list.append((k, b))
    cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imwrite('lines.jpg', image)
cv2.imshow('Lines', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
