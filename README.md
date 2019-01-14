# slack_sannsenn_bot
SlackにJoinした新メンバーを参戦させるBotです。

# デモ
![run_challenger.gif](https://github.com/hatunina/slack_sannsenn_bot/blob/master/images/for_readme/demo.gif)

# 各種設定
## Botsの設定
Slack App からBotsを検索し設定する。  
<br>
![figure_1](https://github.com/hatunina/slack_sannsenn_bot/blob/master/images/for_readme/image1.png)
<br>
この時、発行されるAPIトークンをメモしておく。  
その後、メッセージを投稿させるチャンネルへBotを参加させる。  

## slackbot_setting.py
プロジェクト直下に `slackbot_settings.py` を作成し下記を追記する。
```text
API_TOKEN = "your api token"
# 参戦が含まれない文字が投稿された時のリプライ
default_reply = "?"
# コラージュ作成ロジック等が含まれるディレクトリ
PLUGINS = ['slack_rtm_src']
```

## その他
検知するメンションを変更する際は `rtm.py` の `@respond_to` を変更してください。
```python
@respond_to('参戦')
def mention_func(message):
    main_pipeline(message)
```

# 起動
```commandline
python run.py
```

# 参考
https://qiita.com/sukesuke/items/1ac92251def87357fdf6
https://note.nkmk.me/python-pillow-paste/
https://note.nkmk.me/python-pillow-composite/
https://qiita.com/ekzemplaro/items/6bd539983ba8997003b9