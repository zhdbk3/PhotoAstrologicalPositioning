import json

import numpy as np
from numpy import sqrt

from math_utils import vector_angle


def get_plane(GP: list[float], theta: np.float64) -> tuple[np.float64, np.float64, np.float64, np.float64]:
    """
    获取一颗星星的平面方程Ax + By + Cz = D的A, B, C, D
    :param GP: 直射点经纬度
    :param theta: 高度角
    :return: A, B, C, D
    """
    phi = np.radians(GP[0])
    lambda_ = np.radians(GP[1])
    A = np.sin(phi) * np.sin(theta)
    B = np.sin(theta) * np.cos(lambda_) * np.cos(phi)
    C = np.sin(lambda_) * np.sin(theta) * np.cos(phi)
    D = np.sin(theta) ** 2
    return A, B, C, D


def solve(params1: tuple[np.float64, np.float64, np.float64, np.float64],
          params2: tuple[np.float64, np.float64, np.float64, np.float64]) -> list[tuple[np.float64, np.float64]]:
    """
    解两个平面与地球联立的方程组
    :param params1: A1, B1, C1, D1
    :param params2: A2, B2, C2, D2
    :return: 交点的经纬度（角度制）
    """
    A1, B1, C1, D1 = params1
    A2, B2, C2, D2 = params2
    x = (
                -A1 * B1 * B2 * D2 + A1 * B2 ** 2 * D1 - A1 * C1 * C2 * D2 + A1 * C2 ** 2 * D1 + A2 * B1 ** 2 * D2 - A2 * B1 * B2 * D1 + A2 * C1 ** 2 * D2 - A2 * C1 * C2 * D1 - B1 * C2 * sqrt(
            A1 ** 2 * B2 ** 2 + A1 ** 2 * C2 ** 2 - A1 ** 2 * D2 ** 2 - 2 * A1 * A2 * B1 * B2 - 2 * A1 * A2 * C1 * C2 + 2 * A1 * A2 * D1 * D2 + A2 ** 2 * B1 ** 2 + A2 ** 2 * C1 ** 2 - A2 ** 2 * D1 ** 2 + B1 ** 2 * C2 ** 2 - B1 ** 2 * D2 ** 2 - 2 * B1 * B2 * C1 * C2 + 2 * B1 * B2 * D1 * D2 + B2 ** 2 * C1 ** 2 - B2 ** 2 * D1 ** 2 - C1 ** 2 * D2 ** 2 + 2 * C1 * C2 * D1 * D2 - C2 ** 2 * D1 ** 2) + B2 * C1 * sqrt(
            A1 ** 2 * B2 ** 2 + A1 ** 2 * C2 ** 2 - A1 ** 2 * D2 ** 2 - 2 * A1 * A2 * B1 * B2 - 2 * A1 * A2 * C1 * C2 + 2 * A1 * A2 * D1 * D2 + A2 ** 2 * B1 ** 2 + A2 ** 2 * C1 ** 2 - A2 ** 2 * D1 ** 2 + B1 ** 2 * C2 ** 2 - B1 ** 2 * D2 ** 2 - 2 * B1 * B2 * C1 * C2 + 2 * B1 * B2 * D1 * D2 + B2 ** 2 * C1 ** 2 - B2 ** 2 * D1 ** 2 - C1 ** 2 * D2 ** 2 + 2 * C1 * C2 * D1 * D2 - C2 ** 2 * D1 ** 2)) / (
                A1 ** 2 * B2 ** 2 + A1 ** 2 * C2 ** 2 - 2 * A1 * A2 * B1 * B2 - 2 * A1 * A2 * C1 * C2 + A2 ** 2 * B1 ** 2 + A2 ** 2 * C1 ** 2 + B1 ** 2 * C2 ** 2 - 2 * B1 * B2 * C1 * C2 + B2 ** 2 * C1 ** 2)
    y = (A1 ** 2 * B2 * D2 - A1 * A2 * B1 * D2 - A1 * A2 * B2 * D1 + A1 * C2 * sqrt(
        A1 ** 2 * B2 ** 2 + A1 ** 2 * C2 ** 2 - A1 ** 2 * D2 ** 2 - 2 * A1 * A2 * B1 * B2 - 2 * A1 * A2 * C1 * C2 + 2 * A1 * A2 * D1 * D2 + A2 ** 2 * B1 ** 2 + A2 ** 2 * C1 ** 2 - A2 ** 2 * D1 ** 2 + B1 ** 2 * C2 ** 2 - B1 ** 2 * D2 ** 2 - 2 * B1 * B2 * C1 * C2 + 2 * B1 * B2 * D1 * D2 + B2 ** 2 * C1 ** 2 - B2 ** 2 * D1 ** 2 - C1 ** 2 * D2 ** 2 + 2 * C1 * C2 * D1 * D2 - C2 ** 2 * D1 ** 2) + A2 ** 2 * B1 * D1 - A2 * C1 * sqrt(
        A1 ** 2 * B2 ** 2 + A1 ** 2 * C2 ** 2 - A1 ** 2 * D2 ** 2 - 2 * A1 * A2 * B1 * B2 - 2 * A1 * A2 * C1 * C2 + 2 * A1 * A2 * D1 * D2 + A2 ** 2 * B1 ** 2 + A2 ** 2 * C1 ** 2 - A2 ** 2 * D1 ** 2 + B1 ** 2 * C2 ** 2 - B1 ** 2 * D2 ** 2 - 2 * B1 * B2 * C1 * C2 + 2 * B1 * B2 * D1 * D2 + B2 ** 2 * C1 ** 2 - B2 ** 2 * D1 ** 2 - C1 ** 2 * D2 ** 2 + 2 * C1 * C2 * D1 * D2 - C2 ** 2 * D1 ** 2) - B1 * C1 * C2 * D2 + B1 * C2 ** 2 * D1 + B2 * C1 ** 2 * D2 - B2 * C1 * C2 * D1) / (
                A1 ** 2 * B2 ** 2 + A1 ** 2 * C2 ** 2 - 2 * A1 * A2 * B1 * B2 - 2 * A1 * A2 * C1 * C2 + A2 ** 2 * B1 ** 2 + A2 ** 2 * C1 ** 2 + B1 ** 2 * C2 ** 2 - 2 * B1 * B2 * C1 * C2 + B2 ** 2 * C1 ** 2)
    z1 = -(A1 * B2 - A2 * B1) * sqrt(
        A1 ** 2 * B2 ** 2 + A1 ** 2 * C2 ** 2 - A1 ** 2 * D2 ** 2 - 2 * A1 * A2 * B1 * B2 - 2 * A1 * A2 * C1 * C2 + 2 * A1 * A2 * D1 * D2 + A2 ** 2 * B1 ** 2 + A2 ** 2 * C1 ** 2 - A2 ** 2 * D1 ** 2 + B1 ** 2 * C2 ** 2 - B1 ** 2 * D2 ** 2 - 2 * B1 * B2 * C1 * C2 + 2 * B1 * B2 * D1 * D2 + B2 ** 2 * C1 ** 2 - B2 ** 2 * D1 ** 2 - C1 ** 2 * D2 ** 2 + 2 * C1 * C2 * D1 * D2 - C2 ** 2 * D1 ** 2) / (
                 A1 ** 2 * B2 ** 2 + A1 ** 2 * C2 ** 2 - 2 * A1 * A2 * B1 * B2 - 2 * A1 * A2 * C1 * C2 + A2 ** 2 * B1 ** 2 + A2 ** 2 * C1 ** 2 + B1 ** 2 * C2 ** 2 - 2 * B1 * B2 * C1 * C2 + B2 ** 2 * C1 ** 2) + (
                 A1 ** 2 * C2 * D2 - A1 * A2 * C1 * D2 - A1 * A2 * C2 * D1 + A2 ** 2 * C1 * D1 + B1 ** 2 * C2 * D2 - B1 * B2 * C1 * D2 - B1 * B2 * C2 * D1 + B2 ** 2 * C1 * D1) / (
                 A1 ** 2 * B2 ** 2 + A1 ** 2 * C2 ** 2 - 2 * A1 * A2 * B1 * B2 - 2 * A1 * A2 * C1 * C2 + A2 ** 2 * B1 ** 2 + A2 ** 2 * C1 ** 2 + B1 ** 2 * C2 ** 2 - 2 * B1 * B2 * C1 * C2 + B2 ** 2 * C1 ** 2)
    z2 = -z1
    # 转化为经纬度
    phi = np.degrees(np.arctan2(y, x))
    lambda1 = np.degrees(np.arcsin(z1))
    lambda2 = np.degrees(np.arcsin(z2))
    return [(phi, lambda1), (phi, lambda2)]


def dual_star_positioning(star1: dict, star2: dict, zenith_vector: np.ndarray, z: float) -> tuple[tuple[float]]:
    """
    双星定位
    :param star1: 星星1
    :param star2: 星星2
    :param zenith_vector: 天顶向量
    :param z: 像素焦距
    :return: 两个经纬度
    """
    # 读取数据，计算高度角
    x1, y1 = star1['coordinate']
    theta1: np.float64 = np.pi / 2 - vector_angle(np.array([x1, y1, z]), zenith_vector)  # 高度角与天顶角互余
    x2, y2 = star2['coordinate']
    theta2: np.float64 = np.pi / 2 - vector_angle(np.array([x2, y2, z]), zenith_vector)
    # IDE你犯什么大病啊，这nm明明就是np.float64

    # 计算平面方程
    params1 = get_plane(star1['GP'], theta1)
    params2 = get_plane(star2['GP'], theta2)

    p1, p2 = solve(params1, params2)
    print(star1['name'], star2['name'], p1, p2)


def main(json_path: str):
    # 读取数据
    with open(json_path, 'r') as f:
        data = json.load(f)
    stars = data['stars']
    x_zenith, y_zenith = data['zenith']
    z = data['z']
    zenith_vector = np.array([x_zenith, y_zenith, z])
    # 两两求交点
    for i in range(len(stars)):
        for j in range(i + 1, len(stars)):
            dual_star_positioning(stars[i], stars[j], zenith_vector, z)


if __name__ == '__main__':
    main('data.json')
