import numpy as np

import json


def GP2vector(GP: list[float]) -> np.ndarray:
    """
    将GP的经纬度转化为向量
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


def get_z_from_2_stars(star1: dict, star2: dict) -> float:
    """
    根据两颗星星算出z
    :param star1: 星星1
    :param star2: 星星2
    :return: z
    """
    # 计算理论夹角
    theta0 = vector_angle(GP2vector(star1['GP']), GP2vector(star2['GP']))

    # 读取数据备用
    x1, y1 = star1['coordinate']
    x2, y2 = star2['coordinate']

    def try_angle(z: float) -> np.float64:
        """
        根据已有条件，代入一个z求夹角
        当两颗星星在不同象限时，单调递减
        当两颗星星在相同象限时，先上升后下降
        :param z: 尝试的z
        :return: z为该值时的夹角（弧度制）
        """
        v1 = np.array([x1, y1, z])
        v2 = np.array([x2, y2, z])
        return vector_angle(v1, v2)

    # 二分查找
    acceptable_error = 1e-3  # 可接受的误差范围
    # 确定查找下限，从递减的部分开始
    left = 1
    step = 10
    last = 0
    while (tmp := try_angle(left)) > last:
        last = tmp
        left += step
    # 确定查找上限
    right = left + 1
    while try_angle(right) > theta0:
        right *= 2
    # 开始查找
    while right - left > acceptable_error:
        mid = (left + right) / 2
        if try_angle(mid) > theta0:
            left = mid
        else:
            right = mid

    return mid


def main(json_path: str) -> None:
    # 读取json数据
    with open(json_path, 'r') as f:
        data = json.load(f)
        stars = data['stars']

    # 两两枚举计算
    z_list = []
    for i in range(len(stars)):
        for j in range(i + 1, len(stars)):
            star1, star2 = stars[i], stars[j]
            z_ij = get_z_from_2_stars(star1, star2)
            z_list.append(z_ij)
            print(star1['name'], star2['name'], z_ij)
    z = np.mean(z_list)
    print('\n平均值', z)

    # 写入json
    data['z'] = z
    with open(json_path, 'w') as f:
        json.dump(data, f)


if __name__ == '__main__':
    main('data.json')
