"""
utilモジュール
"""

import requests
from PIL import Image
import io


def get_icon(message):
    icon_url = message.user.get('profile').get('image_512')
    icon = requests.get(icon_url, stream=True)

    # 取得したバイナリデータはオンメモリで処理するのでImage型に変換
    icon_image = Image.open(io.BytesIO(icon.content))

    return icon_image


def get_token(message):
    token = message._client.token
    return token


def get_channel(message):
    channel = message.channel._body.get('name_normalized')
    return channel