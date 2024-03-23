import argparse

import mark
import get_zenith
import get_z
import calc

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='照片测星定位(Photo Astrological Positioning)')
    subparsers = parser.add_subparsers(title='子命令', dest='command')

    mark_parser = subparsers.add_parser('mark', help='标注照片上的天体并计算GP')
    mark_parser.add_argument('-j', '--json-path', required=True, help='存放星星的json文件路径，若不存在会新建')
    mark_parser.add_argument('-r', '--read', default=None, help='读取已整理好的文件，不再手动输入，格式见README.md')

    zenith_parser = subparsers.add_parser('zenith', help='天顶位置确定')
    zenith_parser.add_argument('image_path', help='标注好直线的图片的路径')
    zenith_parser.add_argument('-c', '--colour', default='green', help='直线颜色，可选red,green,blue，默认为green')
    zenith_parser.add_argument('-j', '--json-path', required=True, help='存放星星的json文件路径')

    z_parser = subparsers.add_parser('z', help='计算像素焦距')
    z_parser.add_argument('-j', '--json-path', required=True, help='存放星星的json文件路径')

    calc_parser = subparsers.add_parser('calc', help='定位计算')
    calc_parser.add_argument('-j', '--json_path', required=True, help='存放星星的json文件路径')

    args = parser.parse_args()
    match args.command:
        case 'mark':
            mark.main(args.json_path, args.read)
        case 'zenith':
            get_zenith.main(args.image_path, args.colour, args.json_path)
        case 'z':
            get_z.main(args.json_path)
        case 'calc':
            calc.main(args.json_path)
