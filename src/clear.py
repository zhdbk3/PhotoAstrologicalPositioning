import cv2

image = cv2.imread('../test/1.jpg')

lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
l, a, b = cv2.split(lab)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
l = clahe.apply(l)
lab = cv2.merge((l, a, b))
image = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

# # 对比度
# alpha = 1.2  # 对比度（1.0表示不变）
# beta = 0  # 亮度（0表示不变）
# image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
#
# # 高反差保留
# image = cv2.detailEnhance(image, sigma_s=10, sigma_r=0.15)

# 写入并显示处理后的图像
cv2.imwrite('clear.jpg', image)
cv2.imshow('Clear Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
