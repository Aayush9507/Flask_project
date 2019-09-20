from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
api = Api(app)
app.secret_key = 'aayush'

jwt = JWT(app, authenticate, identity)  # Auth

items = []

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from resources.db import db
    db.init_app(app)
    app.run(port=5000, debug=True)