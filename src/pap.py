import argparse
import os
import json

import mark
import get_z
import get_zenith
import calc

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='照片测星定位(Photo Astrological Positioning)')
    parser.add_argument('json_path', help='存放星星的json文件路径，若不存在会新建')

    subparsers = parser.add_subparsers(title='子命令', dest='command')

    mark_parser = subparsers.add_parser('mark', help='标注照片上的天体并计算GP')
    mark_parser.add_argument('-r', '--read', default=None, help='读取已整理好的文件，不再手动输入，格式见README.md')

    z_parser = subparsers.add_parser('z', help='计算像素焦距')

    zenith_parser = subparsers.add_parser('zenith', help='天顶位置确定')
    zenith_parser.add_argument('image_path', help='标注好直线的图片的路径')
    zenith_parser.add_argument('-c', '--colour', default='green', help='直线颜色，可选red,green,blue，默认为green')

    calc_parser = subparsers.add_parser('calc', help='定位计算')

    args = parser.parse_args()

    # 新建json文件如果没有的话
    if not os.path.exists(args.json_path):
        with open(args.json_path, 'w') as f:
            json.dump({'stars': []}, f)

    match args.command:
        case 'mark':
            mark.main(args.json_path, args.read)
        case 'z':
            get_z.main(args.json_path)
        case 'zenith':
            get_zenith.main(args.json_path, args.image_path, args.colour)
        case 'calc':
            calc.main(args.json_path)
