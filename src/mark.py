import re
import json


def to_hours(hour_angle: str) -> float:
    """
    将单位转化为h
    :param hour_angle: 时角，字符串形式
    :return: 单位为h的量
    """
    pattern = re.compile(r'(\d+)h(\d+)m(\d+.\d+)s')
    match = pattern.match(hour_angle)
    h, m, s = match.groups()
    return float(h) + float(m) / 60 + float(s) / 3600


def to_degrees(declination: str) -> float:
    """
    将单位转化为度
    :param declination: 赤纬，字符串形式
    :return: 单位为度的量
    """
    pattern = re.compile(r'([+\-])(\d+)°(\d+)\'(\d+.\d+)\"')
    match = pattern.match(declination)
    sign, d, m, s = match.groups()
    return (1 if sign == '+' else -1) * (float(d) + float(m) / 60 + float(s) / 3600)


def write_star(name: str, coordinate: tuple[float, float], GP: tuple[float, float], json_path: str) -> None:
    """
    将星星数据写入json文件
    :param name: 星星名字
    :param coordinate: 照片上坐标
    :param GP: 直射点经纬度
    :param json_path: json路径
    :return: None
    """
    # 若不存在文件则新建
    try:
        with open(json_path):
            pass
    except FileNotFoundError:
        with open(json_path, 'w') as f:
            json.dump({'stars': []}, f)
    # 读取已有数据
    with open(json_path, 'r') as f:
        data = json.load(f)
    # 添加这颗星星
    data['stars'].append({
        'name': name,
        'coordinate': coordinate,
        'GP': GP
    })
    with open(json_path, 'w') as f:
        json.dump(data, f)


def calculate_and_write(name: str, coordinate: tuple[float, float], hour_angle: str, declination: str,
                        json_path: str) -> None:
    """
    计算星星并写入
    :param name: 星星名字
    :param coordinate: 照片上坐标
    :param hour_angle: 时角
    :param declination: 赤纬
    :param json_path: json路径
    :return: None
    """
    # 将时角和赤纬统一单位
    hour_angle = to_hours(hour_angle)
    declination = to_degrees(declination)
    # 计算GP
    latitude = declination
    longitude = 360 - hour_angle * 15
    GP = (latitude, longitude)
    print(name, 'GP', GP)

    # 写入json
    write_star(name, coordinate, GP, json_path)


def main(json_path: str, read: None | str = None) -> None:
    """
    标记星星，计算GP
    :param json_path: json路径
    :param read: 读取整理好的文件，如果没有则为None
    :return: None
    """
    # 有整理好的文件
    if read is not None:
        with open(read, 'r', encoding='utf-8') as f:
            text = f.readlines()
            for line in text:
                _, name, x, y, hour_angle, declination, _ = line.replace(' ', '').split('|')
                coordinate = (float(x), float(y))
                calculate_and_write(name, coordinate, hour_angle, declination, json_path)
        return

    # 手动输入
    print('输入ok结束')
    while (name := input('\n星星名字>>>')) != 'ok':
        # 输入信息
        coordinate = input('照片上星星的坐标，用英文逗号分隔>>>')
        coordinate = eval(f'({coordinate})')
        hour_angle = input('时角>>>')
        declination = input('赤纬>>>')
        # 计算并写入
        calculate_and_write(name, coordinate, hour_angle, declination, json_path)


if __name__ == '__main__':
    main('data.json', '../test/stars.txt')
