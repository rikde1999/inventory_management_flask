from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app import db
from app.category.models import Category
from app.products.models import Product


def init_admin(app):
    admin = Admin(app, name="Inventory Admin", template_mode="bootstrap4")

    admin.add_view(ModelView(Category, db.session))
    admin.add_view(ModelView(Product, db.session))

    return admin
