import cv2
import numpy as np

from intersection_of_multi_lines import intersection_of_multi_lines

import json


def main(json_path: str, image_path: str, c: str):
    # 转化颜色字符串为色调
    match c:
        case 'red':
            hue = 0
        case 'green':
            hue = 120
        case 'blue':
            hue = 240
        case _:
            raise ValueError('颜色必须为red,green,blue之一')

    # 读取图片
    image = cv2.imread(image_path)

    # 转为HSV颜色空间
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # 保留指定颜色的部分
    lower = np.array([hue - 10, 100, 100])
    upper = np.array([hue + 10, 255, 255])
    mask = cv2.inRange(hsv_image, lower, upper)
    cv2.destroyAllWindows()

    # 检测直线
    lines = cv2.HoughLinesP(mask, 1, np.pi / 180, 50, minLineLength=100, maxLineGap=1000)
    # 转化为向量
    start_points = []
    directions = []
    for line in lines:
        x1, y1, x2, y2 = line[0]
        start_points.append([x1, y1])
        directions.append([x2 - x1, y2 - y1])
    start_points = np.array(start_points)
    directions = np.array(directions)

    # 计算距离这些直线距离之和最近的点
    zenith = intersection_of_multi_lines(start_points, directions)[0:2]
    # 转化为以图片中心为原点的坐标
    zenith[0] -= image.shape[1] / 2
    zenith[1] -= image.shape[0] / 2
    print(zenith)

    # 写入json
    with open(json_path, 'r') as f:
        data = json.load(f)
    data['zenith'] = (zenith[0][0], zenith[1][0])
    with open(json_path, 'w') as f:
        json.dump(data, f)


if __name__ == '__main__':
    main('data.json', '../test/lines.jpg', 'red')
