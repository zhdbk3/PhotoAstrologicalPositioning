import cv2
import numpy as np

image = cv2.imread('../test/1.jpg')


# 色阶
def adjust_levels(image: np.ndarray, black_level: int, white_level: int) -> np.ndarray:
    """
    调整色阶
    :param image: 图像
    :param black_level: 黑场
    :param white_level: 白场
    :return: 调整后的图像
    """
    lut = np.zeros(256, dtype=np.uint8)
    for i in range(256):
        if i < black_level:
            lut[i] = 0
        elif i > white_level:
            lut[i] = 255
        else:
            lut[i] = (i - black_level) * 255 / (white_level - black_level)
    image = cv2.LUT(image, lut)
    return image


image = adjust_levels(image, 10, 245)

# 对比度
alpha = 1.2  # 对比度（1.0表示不变）
beta = 0  # 亮度（0表示不变）
image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

# 高反差保留
image = cv2.detailEnhance(image, sigma_s=10, sigma_r=0.15)

# 写入并显示处理后的图像
cv2.imwrite('clear.jpg', image)
cv2.imshow('Clear Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
