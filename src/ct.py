#
# Created by MC着火的冰块 on 2024/8/1
#
# ct: Coordinate Transformation 坐标变换
#

def pretty(num: float) -> int | float:
    """若小数点后为0，转为int"""
    return int(num) if num.is_integer() else num


def main() -> None:
    print('请右键照片，编辑，进入Windows自带的画图软件')

    print('请输入照片的宽和高（用空格隔开）：')
    width, height = map(int, input('>>>').split())

    while True:
        print('星星的像素位置（用空格隔开）：')
        x, y = map(int, input('>>>').split())
        print('坐标：')
        print(pretty(x - width / 2), pretty(y - height / 2))


if __name__ == '__main__':
    main()
