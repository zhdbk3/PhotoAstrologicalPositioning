import argparse

import init
import mark
import get_z
import get_zenith
import calc


parser = argparse.ArgumentParser(description='照片测星定位(Photo Astrological Positioning)')

subparsers = parser.add_subparsers(title='子命令', dest='command')

init_parser = subparsers.add_parser('init', help='初始化')

mark_parser = subparsers.add_parser('mark', help='标注照片上的天体并计算GP')
mark_parser.add_argument('-r', '--read-path', default=None, help='读取已整理好的文件，不再手动输入，格式见README.md')

z_parser = subparsers.add_parser('z', help='计算像素焦距')

zenith_parser = subparsers.add_parser('zenith', help='天顶位置确定')
zenith_parser.add_argument('image_path', help='标注好直线的图片的路径')
zenith_parser.add_argument('-c', '--colour', default='green', help='直线颜色，可选red/green/blue，默认为green')

calc_parser = subparsers.add_parser('calc', help='定位计算')

args = parser.parse_args()

match args.command:
    case 'init':
        init.main()
    case 'mark':
        mark.main(args.read_path)
    case 'z':
        get_z.main()
    case 'zenith':
        get_zenith.main(args.image_path, args.colour)
    case 'calc':
        calc.main()
