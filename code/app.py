from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
app.secret_key = 'aayush'


items = []


class Student(Resource):

    def get(self, name):

        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 202 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': "An item with name '{}' already exists. ".format(name)}, 400
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201


class ItemList(Resource):

    def get(self):
        return {'items': items}


api.add_resource(Student, '/student/<string:name>')
api.add_resource(ItemList, '/items')
app.run(port=5000, debug=True)