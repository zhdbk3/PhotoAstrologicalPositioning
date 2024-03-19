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
    try:
        with open(json_path, 'r') as f:
            pass
    except FileNotFoundError:
        with open(json_path, 'w') as f:
            json.dump({'stars': []}, f)
    with open(json_path, 'r') as f:
        data = json.load(f)
    data['stars'].append({
        'name': name,
        'coordinate': coordinate,
        'GP': GP
    })
    with open(json_path, 'w') as f:
        json.dump(data, f)


def main(json_path):
    print('输入ok结束')
    while (name := input('\n星星名字>>>')) != 'ok':
        coordinate = input('照片上星星的坐标，用英文逗号分隔>>>')
        coordinate = eval(f'({coordinate})')
        hour_angle = to_hours(input('时角>>>'))
        declination = to_degrees(input('赤纬>>>'))
        # 计算GP
        latitude = declination
        longitude = 360 - hour_angle * 15
        GP = (latitude, longitude)
        print('GP', GP)
        # 写入json
        write_star(name, coordinate, GP, json_path)


if __name__ == '__main__':
    print(to_hours('16h04m10.53s'), to_degrees('+13°39\'15.2"'))
    write_star('星星名字', (1, 2), (3, 4), 'tmp.json')
    main('data.json')
