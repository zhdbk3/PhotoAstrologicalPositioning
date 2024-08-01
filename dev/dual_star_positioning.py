"""双星定位法公式推导"""

from sympy import Symbol, Eq, sin, cos, print_latex, solve, symbols
from sympy.vector import CoordSys3D, Vector
from sympy.abc import x, y, z

N = CoordSys3D('N')


def vector(x, y, z) -> Vector:
    return x * N.i + y * N.j + z * N.k


def GP2vector(phi: Symbol, lam: Symbol) -> Vector:
    """
    GP经纬度转向量
    :param phi: 纬度
    :param lam: 经度
    :return: 向量
    """
    x = cos(phi) * cos(lam)
    y = cos(phi) * sin(lam)
    z = sin(phi)
    return vector(x, y, z)


def get_plane(phi: Symbol, lam: Symbol, theta: Symbol) -> Eq:
    """
    求解一颗星星平面方程
    :param phi: GP纬度
    :param lam: GP经度
    :param theta: 高度角，与天顶角互余
    :return: 平面的方程
    """
    # 星星的单位方向向量
    n = GP2vector(phi, lam)
    # 求出以nsinθ为法向量且经过点nsinθ的平面方程
    normal_vector = n * sin(theta)  # 法向量
    components = normal_vector.components
    a, b, c = components[N.i], components[N.j], components[N.k]  # 点nsinθ的坐标，同时也是平面的a,b,c
    d = Symbol('d')
    plane = Eq(a * x + b * y + c * z, d)  # 平面方程
    # 将点代入求解
    plane0 = plane.subs({x: a, y: b, z: c})
    d0 = solve(plane0, d)[0]
    plane = plane.subs({d: d0})
    return plane


# 一颗星星
phi = Symbol('\\phi')
lam = Symbol('\\lambda')
theta = Symbol('\\theta')
plane = get_plane(phi, lam, theta)
print('Plane')
print_latex(plane)

# 两个平面方程
A1, B1, C1, D1 = symbols('A1 B1 C1 D1')
plane1 = Eq(A1 * x + B1 * y + C1 * z, D1)
A2, B2, C2, D2 = symbols('A2 B2 C2 D2')
plane2 = Eq(A2 * x + B2 * y + C2 * z, D2)
# 地球（单位球）方程
earth = Eq(x ** 2 + y ** 2 + z ** 2, 1)
print('Equations')
print_latex(plane1)
print_latex(plane2)
print_latex(earth)

# 联立求解
solution1, solution2 = solve([plane1, plane2, earth], [x, y, z], dict=True)
print('Solution Latex')
print_latex(solution1[x])
print_latex(solution1[y])
print_latex(solution1[z])
print_latex(solution2[x])
print_latex(solution2[y])
print_latex(solution2[z])

print('Solution')
print(solution1[x])
print(solution1[y])
print(solution1[z])
print(solution2[x])
print(solution2[y])
print(solution2[z])

print(solution1[x] == solution2[x])
print(solution1[y] == solution2[y])
print(solution1[z] == -solution2[z])
