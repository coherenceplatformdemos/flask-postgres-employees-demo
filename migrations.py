from flask_migrate import Migrate
from app import app, db
import os

# Initialize the migration object
migrate = Migrate(app, db)


# Function to run migrations automatically
def run_migrations():
	if not os.path.exists('migrations'):
		# Initialize the migration directory if it doesn't exist
		os.system('flask db init')
	# Generate a migration
	os.system('flask db migrate -m "Initial migration for Employee model"')
	# Apply the migration
	os.system('flask db upgrade')


# Main entry point
if __name__ == '__main__':
	with app.app_context():
		run_migrations()
else:
	with app.app_context():
		run_migrations()