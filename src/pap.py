import argparse

import get_zenith

parser = argparse.ArgumentParser(description='照片测星定位(Photo Astrological Positioning)')
subparsers = parser.add_subparsers(title='子命令', dest='command')

zenith_parser = subparsers.add_parser('zenith', help='天顶位置确定')
zenith_parser.add_argument('image_path', help='标注好直线的图片的路径')
zenith_parser.add_argument('-c', '--colour', default='green', help='直线颜色，可选red,green,blue，默认为green')

args = parser.parse_args()
match args.command:
    case 'zenith':
        get_zenith.main(args.image_path, args.colour)
