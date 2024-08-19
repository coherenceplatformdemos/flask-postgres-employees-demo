# app.py
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Ensure the database URL starts with 'postgresql://'
db_url = os.environ.get('DATABASE_URL')
if db_url.startswith('postgres://'):
	db_url = db_url.replace('postgres://', 'postgresql://', 1)

app.config['SQLALCHEMY_DATABASE_URI'] = db_url
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Employees(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	email = db.Column(db.String(120), unique=False, nullable=False)
	phone = db.Column(db.String(20), nullable=False)


@app.route('/')
def index():
	employees = Employees.query.all()
	return render_template('index.html', employees=employees, editing=False)


@app.route('/add', methods=['POST'])
def add_employee():
	name = request.form['name']
	email = request.form['email']
	phone = request.form['phone']
	new_employee = Employees(name=name, email=email, phone=phone)
	db.session.add(new_employee)
	db.session.commit()
	return redirect(url_for('index'))


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_employee(id):
	employee = Employees.query.get_or_404(id)
	if request.method == 'POST':
		employee.name = request.form['name']
		employee.email = request.form['email']
		employee.phone = request.form['phone']
		db.session.commit()
		return redirect(url_for('index'))
	return render_template('index.html', employee=employee, editing=True)


@app.route('/delete/<int:id>')
def delete_employee(id):
	employee = Employees.query.get_or_404(id)
	db.session.delete(employee)
	db.session.commit()
	return redirect(url_for('index'))


if __name__ == '__main__':
	with app.app_context():
		db.create_all()
	app.run(host='0.0.0.0', port=8080, debug=True)
else:
	with app.app_context():
		db.create_all()
	app.run(host='0.0.0.0', port=8080, debug=False)


def run_app():
	with app.app_context():
		db.create_all()
	app.run(host='0.0.0.0', port=8080, debug=False)