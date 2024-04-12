from flask import Blueprint
from flask_cors import CORS

bot_routes = Blueprint('bot_routes', __name__)
# any port from localhost is okay to access these routes
CORS(bot_routes, origins=["http://localhost:*"])  # Apply CORS to the bot_routes blueprint

@bot_routes.route('/api/bots')
def get_all_bots():
    bots = [
    {
      "id": "1",
      "name": "Claudette",
      "tagline": "Claudette uses the API of claude.ai to help",
      "fullDescription": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
      "location": "Boston, MA"
    },
    {
      "id": "2",
      "name": "Chatty",
      "location": "Miami, FL",
      "tagline": "Chaty use the API of ChatGPT to help.",
      "fullDescription": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
      "company": {
        "name": "Veneer Solutions",
        "description": "Veneer Solutions is a creative agency specializing in digital design and development. Our team is dedicated to pushing the boundaries of creativity and innovation to deliver exceptional results for our clients.",
        "contactEmail": "contact@loremipsum.com",
        "contactPhone": "555-555-5555"
      }
    },
    {
      "id": "3",
      "name": "Bill",
      "tagline": "Bill is just a standard human masquerading as a bot. He's a little tempermental at times",
      "fullDescription": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
      "location": "Boston, MA"
    },
    {
      "id": "4",
      "name": "Henry",
      "tagline": "Henry is an extra bot not normally shown",
      "fullDescription": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
      "location": "Boston, MA"
    }
  ]
    return bots