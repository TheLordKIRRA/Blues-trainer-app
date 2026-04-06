from flask_migrate import Migrate
from app.db.database import db
from app import create_app  # Assuming you have a create_app function

app = create_app()
migrate = Migrate(app, db)

if __name__ == '__main__':
    # Run migrations
    with app.app_context():
        # Create all tables (for initial setup)
        db.create_all()
        
        # Or use Alembic commands via CLI:
        # flask db init (if not done)
        # flask db migrate -m "Initial migration"
        # flask db upgrade
        pass