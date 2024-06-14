from typing import TypedDict

from numpy import float64

FloatType = float | float64  # 浮点数
BinaryType = tuple[FloatType, FloatType]  # 二元组
QuadrupleType = tuple[FloatType, FloatType, FloatType, FloatType]  # 四元组


class StarDict(TypedDict):
    name: str
    coordinate: BinaryType
    GP: BinaryType
