"""
slackに関するモジュール
"""

import requests
import io


class SlackUtil(object):
    """
    Slack関連クラス
    """

    def __init__(self, token, channel):
        # type: (str, str) -> None
        """
        slack設定のコンストラクタ
        :param token: slackのtoken
        :param channel: 投稿先チャンネル名
        """
        self.token = token
        self.channel = channel

    def notify_with_image(self, massage, image):
        # type: (str, Image) -> None
        """
        slackにメッセージと画像を投稿する
        :param massage: 投稿内容
        :param image: PILのImage
        """

        param = {
            'token': self.token,
            'channels': self.channel,
            'initial_comment': massage,
            'title': "New Challenger!!!"
        }

        # Imageオブジェクトをバイナリに変換
        output = io.BytesIO()
        image.save(output, format='JPEG')
        image_binary = output.getvalue()

        requests.post(url="https://slack.com/api/files.upload", params=param, files={'file': image_binary})
