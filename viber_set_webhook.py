from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration

TOKEN = "4f5c605073e7e741-801386ee70f8470d-dd779006e2e4d2b8"

viber = Api(BotConfiguration(
    name='PythonSampleBot',
    avatar='http://site.com/avatar.jpg',
    auth_token=TOKEN
))

viber.set_webhook('ссылка на ваш сервер с ботом')