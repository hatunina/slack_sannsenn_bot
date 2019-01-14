import src.collage_generator as cg
from src.slack_util import SlackUtil

import src.util as util


def main_pipeline(message):
    # メンションを送ったユーザーのアイコンを取得
    icon_image = util.get_icon(message)

    # Slack API tokenを取得
    token = util.get_token(message)

    # メンションが送られたチャンネルを取得
    channel = util.get_channel(message)

    # コラ画像生成
    collage_im = cg.collage_generate_pipeline(icon_image)

    # Slackへコラ画像を投稿
    slack_util = SlackUtil(token, channel)
    slack_util.notify_with_image('New Challenger!!!', collage_im)
