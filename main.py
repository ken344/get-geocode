# 「openstreetmap」
# 無料で、Keyなしで使用できるが、曖昧な条件に弱い

import requests
import json

# 緯度経度を取得したい住所
address = "東京都新宿区西新宿２丁目８−１"

# APIリクエストのURLを作成
url = f'https://nominatim.openstreetmap.org/search?format=json&q={address}'

# APIリクエストを送信して結果を取得
response = requests.get(url)
data = json.loads(response.text)

# 緯度経度を出力
if data:
    latitude = data[0]['lat']
    longitude = data[0]['lon']
    print(f'住所: {address}')
    print(f'緯度: {latitude}, 経度: {longitude}')
else:
    print('結果が見つかりませんでした')