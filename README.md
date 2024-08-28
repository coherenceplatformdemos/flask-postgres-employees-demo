<p align="center">
  <a href="https://www.withcoherence.com">
    <img alt="Coherence Logo" title="Coherence" src="./logo.png" width="400" style="color: black">
  </a>
</p>


<p align="center">
  <i>Platform-as-a-service in your own Cloud</i><br/> 
  <a href="https://www.withcoherence.com">withcoherence.com</a>
</p>

<h1 align="center">
Flask and Postgres Example
</h1>

<p align="center">
<img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white">
<img src="https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white">
</p>

<br/>

# Full stack Flask and Postgres application (employee management)

<p>
This is the code to accompany the tutorial available at our <a href="https://docs.withcoherence.com/coherence-templates/full-stack-template/?tabs=flask">Framework Guide (Flask)</a> page.
</p>

You can use it as a starting point for any full stack Flask application. Read the guide to see how to deploy it to a production environment in your own cloud, or see the instructions below to run a development version of it locally.

## Setup

### Prerequisites

- Docker
- Postgres

### Installation and Usage

1. **Clone the repository:**
    ```bash
    git clone https://github.com/<your_github_username>/flask-postgres-employees-demo.git
    cd flask-postgres-employees-demo
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

## Running migrations

To run migrations, use the following command:
```bash
docker-compose exec web python migrations.py
```

or on Coherence add to your cnc.yaml file:

```yaml
migrate: python migrations.py
```

## Resources

Take a look at the following for more information:

* [Coherence](https://www.withcoherence.com)
* [Why Choose Coherence](https://docs.withcoherence.com/#why-choose-coherence)
* [Coherence Documentation](docs.withcoherence.com)

**Cloud Infrastructure On Autopilot**

_Deploy containerized and serverless apps to your own cloud in minutes, not weeks._
