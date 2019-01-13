import src.image_generator as ig
from src.slack_util import SlackUtil

import src.util as util


def main_pipeline(message):
    icon_image = util.get_icon(message)
    im = ig.image_generate_pipeline(icon_image)

    token = util.get_token(message)
    channel = util.get_channel(message)

    slack_util = SlackUtil(token, channel)
    slack_util.notify_with_image('New Challenger!!!', im)
