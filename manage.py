# manage.py
from flask.cli import FlaskGroup
from app import app, db

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
	db.create_all()
	print("Database tables created")


@cli.command("drop_db")
def drop_db():
	db.drop_all()
	print("Database tables dropped")


if __name__ == "__main__":
	cli()
