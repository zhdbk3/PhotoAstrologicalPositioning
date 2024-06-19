import numpy as np

from hint import *


def GP2vector(GP: BinaryType) -> np.ndarray:
    """
    将GP的经纬度转化为单位方向向量
    :param GP: (纬度, 经度)（角度制）
    :return: 向量
    """
    phi = np.radians(GP[0])  # 纬度
    lam = np.radians(GP[1])  # 经度
    x = np.cos(phi) * np.cos(lam)
    y = np.cos(phi) * np.sin(lam)
    z = np.sin(phi)
    return np.array([x, y, z])


def vector_angle(v1: np.ndarray, v2: np.ndarray) -> FloatType:
    """
    求两个向量夹角
    :param v1: 向量1
    :param v2: 向量2
    :return: 夹角（弧度制）
    """
    return np.arccos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))
