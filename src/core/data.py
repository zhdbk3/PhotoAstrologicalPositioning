from typing import Optional

from hint import *
from .mark import to_hours, to_degrees
from .get_z import get_z


class Data:
    def __init__(self):
        self.stars: dict[str, StarDict] = {}
        self.z: Optional[FloatType] = None
        self.zenith: Optional[BinaryType] = None

    def add_star(self, name: str, x: float, y: float, hour_angle: str, declination: str):
        """
        添加星星
        :param name: 星星名字
        :param x: 照片上横坐标
        :param y: 照片上纵坐标
        :param hour_angle: 时角
        :param declination: 赤纬
        :return: None
        """
        # 将时角和赤纬统一单位
        hour_angle = to_hours(hour_angle)
        declination = to_degrees(declination)
        # 计算GP
        latitude = declination
        longitude = 360 - hour_angle * 15
        GP = (latitude, longitude)

        # 写入数据
        self.stars[name] = {'coordinate': (x, y), 'GP': GP}

    def get_z(self) -> float:
        """
        计算像素焦距
        :return: 像素焦距
        """
        self.z = get_z(self.stars)
        return self.z
