"""双星定位法公式推导"""

from sympy import Symbol, Eq, sin, cos, print_latex, solve, latex
from sympy.vector import CoordSys3D, Vector
from sympy.abc import x, y, z

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


def get_plane(phi: Symbol, lambda_: Symbol, theta: Symbol) -> Eq:
    """
    求解一颗星星平面方程
    :param phi: GP纬度
    :param lambda_: GP经度
    :param theta: 高度角，与天顶角互余
    :return: 平面的方程
    """
    # 星星的单位方向向量
    n = GP2vector(phi, lambda_)
    # 求出以nsinθ为法向量且经过点nsinθ的平面方程
    normal_vector = n * sin(theta)  # 法向量
    a, b, c = normal_vector.components.values()  # 点nsinθ的坐标，同时也是平面的a,b,c
    d = Symbol('d')
    plane = Eq(a * x + b * y + c * z, d)  # 平面方程
    # 将点代入求解
    plane0 = plane.subs({x: a, y: b, z: c})
    d0 = solve(plane0, d)[0]
    plane = plane.subs({d: d0})
    return plane


# 星星1
phi1 = Symbol('\\phi_1')
lambda1 = Symbol('\\lambda_1')
theta1 = Symbol('\\theta_1')
plane1 = get_plane(phi1, lambda1, theta1)
# 星星2
phi2 = Symbol('\\phi_2')
lambda2 = Symbol('\\lambda_2')
theta2 = Symbol('\\theta_2')
plane2 = get_plane(phi2, lambda2, theta2)
# 地球（单位球）方程
earth = Eq(x ** 2 + y ** 2 + z ** 2, 1)

# 联立求交点坐标
print(fr'\begin{{cases}} {latex(plane1)} \\ {latex(plane2)} \\ {latex(earth)} \end{{cases}}')
result = solve([plane1, plane2, earth], [x, y, z])
print_latex(result)
