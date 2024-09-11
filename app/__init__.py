from flask import Flask
from config import Config, db, init_db
from app.admin import init_admin
from app.category.routes import CategoryAPI, CategoryDetailAPI
from app.products.routes import ProductAPI, ProductDetailAPI


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_db(app)

    init_admin(app)

    category_view = CategoryAPI.as_view("category_api")
    category_detail_view = CategoryDetailAPI.as_view("category_detail_api")
    app.add_url_rule("/categories/", view_func=category_view, methods=["GET", "POST"])
    app.add_url_rule(
        "/categories/<int:category_id>",
        view_func=category_detail_view,
        methods=["PUT", "DELETE"],
    )

    product_view = ProductAPI.as_view("product_api")
    product_detail_view = ProductDetailAPI.as_view("product_detail_api")
    app.add_url_rule("/products/", view_func=product_view, methods=["GET", "POST"])
    app.add_url_rule(
        "/products/<int:product_id>",
        view_func=product_detail_view,
        methods=["PUT", "DELETE"],
    )

    return app
