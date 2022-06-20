from email import message
from flask import Flask, request, Response
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages.text_message import TextMessage
import logging

from viberbot.api.viber_requests import (
    ViberConversationStartedRequest, 
    ViberFailedRequest,
    ViberMessageRequest, 
    ViberSubscribedRequest, 
    ViberUnsubscribedRequest
    )


TOKEN = "4f5c605073e7e741-801386ee70f8470d-dd779006e2e4d2b8"

app = Flask(__name__)

bot_configuration = BotConfiguration(
    name="Test_Bot",
    avatar="http://viber.com/avatar.jpg",
    auth_token=TOKEN
)
viber = Api(bot_configuration)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


@app.route("/incoming", methods=["POST"])
def incoming():
    logger.debug(f"recieved request. post data: {request.get_data()}")
    if not viber.verify_signature(request.get_data(), request.headers.get("X-Viber-Content-Signature")):
        return Response(status=403)

    viber_request = viber.parse_request(request.get_data())
    
    if isinstance(viber_request, ViberMessageRequest):
        message = viber_request.message
        viber.send_messages(viber_request.sender.id, [message])
    elif isinstance(viber_request, ViberSubscribedRequest):
        viber.send_messages(viber_request.get_user.id, [TextMessage(text="Thanks for subscribing!")])
    elif isinstance(viber_request, ViberFailedRequest):
        logger.warn(f"Client failed receiving message. failure: {viber_request}")

    return Response(status=200)


if __name__ == "__main__":
    context = ("server.crt", "server.key")
    app.run(host="0.0.0.0", port=443, debug=True, ssl_context=context)
