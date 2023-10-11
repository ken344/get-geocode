# Google Maps Geocoding APIを使って住所から緯度経度を取得する
# 一定回数を超えると有料になるが、曖昧な条件でも出力してくれる。

import os

import requests
import json
from dotenv import load_dotenv

# .envファイルの内容を読み込見込む
load_dotenv()

# Google Maps Geocoding APIのキーを設定
API_KEY = os.environ['G-MAP-API-KEY']

# 緯度経度を取得したい住所
address = "東京都新宿区西新宿２丁目８−１"

# APIリクエストのURLを作成
url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={API_KEY}'

# APIリクエストを送信して結果を取得
response = requests.get(url)
data = json.loads(response.text)

# 緯度経度を出力
if data['status'] == 'OK':
    latitude = data['results'][0]['geometry']['location']['lat']
    longitude = data['results'][0]['geometry']['location']['lng']
    print(f'住所: {address}')
    print(f'緯度: {latitude}, 経度: {longitude}')
else:
    print('エラー：', data['status'])