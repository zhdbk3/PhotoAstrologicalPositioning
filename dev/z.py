"""
计算6个小时候仍没有结果，遂放弃公式法
"""

import io
import sys

from sympy import Symbol, sin, cos, acos, Eq, simplify, print_latex, solve
from sympy.vector import CoordSys3D, Vector

# 兼容github输出
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

N = CoordSys3D('N')


def vector(x, y, z) -> Vector:
    return x * N.i + y * N.j + z * N.k


def GP2vector(phi: Symbol, lambda_: Symbol) -> Vector:
    """
    GP经纬度转向量
    :param phi: 纬度
    :param lambda_: 经度
    :return: 向量
    """
    x = cos(phi) * cos(lambda_)
    y = cos(phi) * sin(lambda_)
    z = sin(phi)
    return vector(x, y, z)


def vector_angle(vector1: Vector, vector2: Vector):
    """求两向量夹角"""
    return acos(vector1.dot(vector2) / (vector1.magnitude() * vector2.magnitude()))


# 已知数据
# 两颗星星的GP
phi1 = Symbol('\\phi_1')  # 纬度
lambda1 = Symbol('\\lambda_1')  # 经度
phi2 = Symbol('\\phi_2')
lambda2 = Symbol('\\lambda_2')
# 两颗星星在照片上的坐标
x1 = Symbol('x_1')
y1 = Symbol('y_1')
x2 = Symbol('x_2')
y2 = Symbol('y_2')

# 理论夹角
theta0 = simplify(vector_angle(GP2vector(phi1, lambda1), GP2vector(phi2, lambda2)))
print('理论夹角', theta0)
print_latex(theta0)
# 要求的像素焦距z
z = Symbol('z')
# 尝试夹角
theta = simplify(vector_angle(vector(x1, y1, z), vector(x2, y2, z)))
print('尝试夹角', theta)
print_latex(theta)

sys.stdout.flush()

# 令尝试夹角与理论夹角相等，求出z
result = solve(Eq(theta, theta0), z)
print('结果', result)
print_latex(result)
