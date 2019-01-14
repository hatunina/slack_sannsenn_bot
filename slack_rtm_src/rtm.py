from slackbot.bot import respond_to
from src.main_pipeline import main_pipeline


@respond_to('参戦')
def mention_func(message):
    main_pipeline(message)
