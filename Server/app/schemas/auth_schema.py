from marshmallow import Schema, fields, validate

class RegisterSchema(Schema):
    username = fields.String(required=True, validate=validate.Length(min=3))
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=6))

class LoginSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)

###Create RegisterSchema and LoginSchema for user authentication
###Add username and password fields with basic requirements
