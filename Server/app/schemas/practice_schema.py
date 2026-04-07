from marshmallow import Schema, fields, validate

class PracticeSessionSchema(Schema):
    id = fields.Integer(dump_only=True)
    session_name = fields.String(required=True, validate=validate.Length(max=100))
    audio_file = fields.String(required=False)
    user_id = fields.Integer(required=True)
    timestamp = fields.DateTime(dump_only=True)
