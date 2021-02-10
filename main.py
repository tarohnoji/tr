from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

import pya3rt
import os

app = Flask(__name__)

line_bot_api = LineBotApi("z4f1dwzscX+G9Dwn6qITXxC5wT7elFaXsPUaObg0b6t8BDGq1JzeLzCvjnVmKd7wbsEptWu3PcYu62R+kcH/3o/Uh9Cq+W3R18g7l04mLv6cugstjqGp+BJPFjq2lhW+ynMaPRqbIX/r0z5tCbiYmAdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("1aa61c9ce0b3775e1be4a113a56dbcf1")


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, sigunature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'ok'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #リプライを作成する
    reply = create_reply(event.message.text)
    line_bot_api.reply_message(
        event.reply_token,
        #実際にcreate_replyの返り値をTextMessageの引数として渡す
        TextSendMessage(text=reply))

def create_reply(user_text):
    apikey = "DZZaQUy1OTXJyfwe15vF4XQ8a2LiVUag"
    client = pya3rt.TalkClient(apikey)
    res = client.talk(user_text)

    return res ['results'][0]['reply']

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    app.run()

