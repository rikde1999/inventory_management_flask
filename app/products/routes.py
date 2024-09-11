from flask import jsonify, request
from flask.views import MethodView
from app import db
from app.products.models import Product
from app.category.models import Category
from app.products.serializers import ProductSchema

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


class ProductAPI(MethodView):
    def get(self):

        products = Product.query.all()
        return jsonify(products_schema.dump(products)), 200

    def post(self):

        data = request.json

        errors = product_schema.validate(data)
        if errors:
            return jsonify(errors), 400

        category = Category.query.get(data["category_id"])
        if not category:
            return jsonify({"error": "Category not found"}), 404

        new_product = Product(
            name=data["name"],
            category_id=data["category_id"],
            price=data["price"],
            quantity=data["quantity"],
            description=data.get("description", ""),
        )

        db.session.add(new_product)
        db.session.commit()

        return jsonify(product_schema.dump(new_product)), 201


class ProductDetailAPI(MethodView):
    def put(self, product_id):

        product = Product.query.get_or_404(product_id)
        data = request.json

        errors = product_schema.validate(data)
        if errors:
            return jsonify(errors), 400

        product.name = data.get("name", product.name)
        product.category_id = data.get("category_id", product.category_id)
        product.price = data.get("price", product.price)
        product.quantity = data.get("quantity", product.quantity)
        product.description = data.get("description", product.description)

        db.session.commit()

        return jsonify(product_schema.dump(product)), 200

    def delete(self, product_id):

        product = Product.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Product deleted"}), 204
