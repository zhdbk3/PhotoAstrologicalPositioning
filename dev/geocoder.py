#
# Created by MC着火的冰块 on 2024/8/23
#
# 暴力搜索出能用的地理编码服务
#

from geopy import geocoders

for name in geocoders.__all__:
    print(name)
    try:
        geolocator = getattr(geocoders, name)(user_agent='PhotoAstrologicalPositioning')
    except Exception as e:
        print(e)
    else:
        print('这个不需要 api_key')
        try:
            location = geolocator.reverse((39.906217, 116.3912757))
            print(location)
        except Exception as e:
            print(e)
        else:
            print('这个可以用！' + '*' * 100)
    print()

"""
ArcGIS
这个不需要 api_key
辽宁省抚顺市抚顺县
这个可以用！****************************************************************************************************
"""
