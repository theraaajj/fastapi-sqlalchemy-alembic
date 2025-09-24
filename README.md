# FastAPI User Management API

This project is a simple user management API built with FastAPI, PostgreSQL, SQLAlchemy, and Alembic, demonstrating a modern backend stack for creating web services.

## Core Technologies

- **API Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Database Migrations**: Alembic

---

## Setup and Installation

1.  **Clone the Repository**
    ```bash
    git clone <your-repo-url>
    cd fastapi_user_project
    ```

2.  **Create and Activate a Virtual Environment**
    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    .\venv\Scripts\activate
    ```

3.  **Install Dependencies**
    *(First, create a requirements.txt file by running `pip freeze > requirements.txt`)*
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Database Connection**
    - Update the `DATABASE_URL` in `app/database.py`.
    - Update the `sqlalchemy.url` in `alembic.ini`.

---

## Database Migrations

[cite_start]This project uses Alembic to manage database schema versions[cite: 4].

-   **To apply all migrations** and bring the database to the latest version, run:
    ```bash
    alembic upgrade head
    ```

-   **To roll back the last migration**, you can use:
    ```bash
    alembic downgrade -1
    ```

---

## Running the Application

To run the live development server, use Uvicorn:

```bash
uvicorn app.main:app --reload

The server will be available at http://127.0.0.1:8000.

Testing the API
Once the server is running, navigate to 

http://12.0.0.1:8000/docs in your browser. This provides an interactive Swagger UI where you can test all the API endpoints directly.

---

With the `README.md` file created, the core project is 100% complete.

Shall we tackle the optional bonus feature of adding filtering to the `GET /users` endpoint next?