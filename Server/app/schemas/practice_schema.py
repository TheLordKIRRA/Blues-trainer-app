from marshmallow import Schema, fields, validate

class PracticeSessionSchema(Schema):
duration_minutes = fields.Integer(required=True)
notes = fields.String(required=False)
activity_type = fields.String(required=True)
