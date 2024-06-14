import json


def main() -> None:
    # 创建data.json
    with open('data.json', 'w') as f:
        json.dump({'stars': []}, f)
    print("照片测星定位：已初始化")


if __name__ == '__main__':
    main()
