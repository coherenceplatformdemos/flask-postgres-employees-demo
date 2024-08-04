# Employee Management Application

A Flask-based web application for managing employees. The application supports adding, editing, and deleting employees, and displays a list of all employees.

## Setup

### Prerequisites

- Docker
- Postgres

### Installation and Usage

1. **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd flask_postgres_employee_app
    ```

2. Add your database credentials to the `docker-compose.yml` file:
    ```yaml
    services:
      db:
        image: postgres:13
        environment:
          POSTGRES_DB: <database_name>
          POSTGRES_USER: <database_user>
          POSTGRES_PASSWORD: <database_password>
    ```

3. Add your database credentials to the `app.py` file:
    ```python
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://<database_user>:<database_password>@db:5432/<database_name>'
    ```

4. **Build and run the Docker container:**
    ```bash
    docker-compose up --build
    ```

5. **Run database migrations:**
    ```bash
    docker-compose exec web flask db upgrade
    ```

6. **Access the application:**
    Open your browser and navigate to `http://localhost:5000/`.

## Usage

![screenshot-1.png](images/screenshot-1.png)

1. **Add Employee:**
    - Fill out the form with the employee's name, email, and phone number.
    - Click "Add Employee".

2. **Edit Employee:**
    - Click the "Edit" link next to the employee you want to edit.
    - Update the employee's information in the form.
    - Click "Update".

3. **Delete Employee:**
    - Click the "Delete" link next to the employee you want to delete.
