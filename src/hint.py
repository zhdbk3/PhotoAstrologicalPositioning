from typing import TypedDict

from numpy import float64

FloatType = float | float64  # 浮点数
BinaryType = tuple[FloatType, FloatType]  # 二元组
QuadrupleType = tuple[FloatType, FloatType, FloatType, FloatType]  # 四元组


class StarDict(TypedDict):
    coordinate: BinaryType
    GP: BinaryType


class DataDict(TypedDict):
    stars: dict[str, StarDict]
    z: FloatType
    zenith: BinaryType
