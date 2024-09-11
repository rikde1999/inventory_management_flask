from marshmallow import Schema, fields


class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    category_id = fields.Int(required=True)
    price = fields.Float(required=True)
    quantity = fields.Int(required=True)
    description = fields.Str()
