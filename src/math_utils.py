import numpy as np


def GP2vector(GP: list[float]) -> np.ndarray:
    """
    将GP的经纬度转化为单位方向向量
    :param GP: [纬度, 经度]（角度制）
    :return: 向量
    """
    phi = np.radians(GP[0])  # 纬度
    lambda_ = np.radians(GP[1])  # 经度
    x = np.cos(phi) * np.cos(lambda_)
    y = np.cos(phi) * np.sin(lambda_)
    z = np.sin(phi)
    return np.array([x, y, z])


def vector_angle(v1: np.ndarray, v2: np.ndarray) -> np.float64:
    """
    求两个向量夹角
    :param v1: 向量1
    :param v2: 向量2
    :return: 夹角（弧度制）
    """
    return np.arccos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))
