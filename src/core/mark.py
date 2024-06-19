import re


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
