
from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

products = {
    'pepsi' : {'type': '2 lt bootle', 'price': 150, 'qty': 280},
    'coke' : {'type': '500 ml bootle', 'price': 65, 'qty': 450},
    'sprite' :{'type': '300 ml bootl', 'price': 50, 'qty': 100}
}

class Products(Resource):

    def get(self, product):
        return {product: products[product]}

    def put(self, product):
        products[product]['category'] = request.form['category']
        return {'result': products}

    def delete(self, product):
        if product in products:
            del products[product]
            return {'result':products}
        else:
            return {'KeyError': "Invalid Key, Please metion a valid key"}

api.add_resource(Products, "/getproduct/<string:product>")

if __name__ == '__main__':
    app.run(debug=True)

    