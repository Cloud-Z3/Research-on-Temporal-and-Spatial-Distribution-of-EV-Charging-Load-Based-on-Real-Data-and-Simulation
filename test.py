import requests

if __name__ == '__main__':
    target = 'https://lbs.amap.com/demo/javascript-api/example/personalized-map/set-map-cotent/'
    req = requests.get(url=target)
    print('地图显示要素' in req.text)