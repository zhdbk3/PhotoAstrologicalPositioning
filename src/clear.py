import cv2

image = cv2.imread('../test/1.jpg')

# 增加对比度和亮度
alpha = 1.5  # 控制对比度 (1.0 表示不变)
beta = 0  # 控制亮度 (0 表示不变)
adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

# 高反差保留滤波
filtered = cv2.detailEnhance(adjusted, sigma_s=10, sigma_r=0.15)

# 写入并显示处理后的图像
cv2.imwrite('enhanced.jpg', filtered)
cv2.imshow('Enhanced Image', filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()
