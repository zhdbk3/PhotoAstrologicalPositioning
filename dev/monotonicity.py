"""
探究当两颗星星在同一象限时，尝试夹角与尝试z的函数的增减性
"""
import numpy as np
import matplotlib.pyplot as plt


def vector_angle(v1: np.ndarray, v2: np.ndarray) -> np.float64:
    """
    求两个向量夹角
    :param v1: 向量1
    :param v2: 向量2
    :return: 夹角（弧度制）
    """
    return np.arccos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))


def try_angle(z: np.float64) -> np.float64:
    """
    根据已有条件，代入一个z求夹角
    :param z: 尝试的z
    :return: z为该值时的夹角（弧度制）
    """
    # 天囷一 天苑一
    v1 = np.array([-97, 97.5, z])
    v2 = np.array([-412, 580.5, z])
    return vector_angle(v1, v2)


# 理论夹角
theta0 = 0.3906931771730551

# 绘制函数图像
x1 = np.linspace(0, 2000, 2000)
y1 = [try_angle(z) for z in x1]
plt.plot(x1, y1)
# 绘制理论夹角水平线
plt.axhline(theta0, color='r')

plt.savefig('../assets/monotonicity.jpg')
plt.show()
