from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration

viber = Api(BotConfiguration(
    name='PythonSampleBot',
    avatar='http://site.com/avatar.jpg',
    auth_token='445da6az1s345z78-dazcczb2542zv51a-e0vc5fva17480im9'
))

viber.set_webhook('ссылка на ваш сервер с ботом')