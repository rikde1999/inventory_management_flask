from flask import Flask, jsonify, request
from flask.views import MethodView
from app import db
from app.category.models import Category


class CategoryAPI(MethodView):
    def get(self):
        categories = Category.query.all()
        result = [
            {"id": c.id, "name": c.name, "description": c.description}
            for c in categories
        ]
        return jsonify(result), 200

    def post(self):
        data = request.json
        new_category = Category(name=data["name"], description=data.get("description"))
        db.session.add(new_category)
        db.session.commit()
        return (
            jsonify(
                {
                    "id": new_category.id,
                    "name": new_category.name,
                    "description": new_category.description,
                }
            ),
            201,
        )


class CategoryDetailAPI(MethodView):
    def put(self, category_id):
        category = Category.query.get_or_404(category_id)
        data = request.json
        category.name = data.get("name", category.name)
        category.description = data.get("description", category.description)
        db.session.commit()
        return (
            jsonify(
                {
                    "id": category.id,
                    "name": category.name,
                    "description": category.description,
                }
            ),
            200,
        )

    def delete(self, category_id):
        category = Category.query.get_or_404(category_id)
        db.session.delete(category)
        db.session.commit()
        return jsonify({"message": "Category deleted"}), 204
