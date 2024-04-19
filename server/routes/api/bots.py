from flask import Blueprint
from flask_cors import CORS
from flask_restful import Api

from bots import BotList, BotResource, BotChatResource
# url prefix will begin all routes so that we don't need to keep typing it
bot_routes = Blueprint('bot_routes', __name__, url_prefix="/api")
CORS(bot_routes, origins=["http://localhost:3001"])  # Apply CORS to the bot_routes blueprint
api = Api(bot_routes, errors=bot_routes.errorhandler)

api.add_resource(BotList, "/bots")
api.add_resource(BotResource, "/bots/<int:bot_id>")
api.add_resource(BotChatResource, "/bots/<int:bot_id>/chat")