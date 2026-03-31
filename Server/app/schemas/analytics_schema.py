from marshmallow import Schema, fields

class DateRangeSchema(Schema):
    """Validates a date range used when requesting analytics."""
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)


class SessionAnalyticsSchema(Schema):
    """Response schema for analytics results on practice sessions."""
    total_sessions = fields.Int(required=True)
    total_minutes = fields.Int(required=True)
    average_duration = fields.Float(required=True)
    streak = fields.Int(required=True)
    accuracy_trend = fields.List(fields.Float(), required=True)
    progress_score = fields.Float(required=True)


class AccuracyBreakdownSchema(Schema):
    """Detailed analysis of accuracy metrics."""
    pitch_accuracy = fields.Float(required=True)
    tempo_accuracy = fields.Float(required=True)
    timing_accuracy = fields.Float(required=True)
    overall_accuracy = fields.Float(required=True)


class TrendPointSchema(Schema):
    """Represents a single point in a trend graph."""
    date = fields.Date(required=True)
    score = fields.Float(required=True)


class TrendResponseSchema(Schema):
    """Describes an entire set of trend graph data."""
    trend = fields.List(fields.Nested(TrendPointSchema), required=True)
