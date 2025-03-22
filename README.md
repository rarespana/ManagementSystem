# ManagementSystem

ManagementSystem is a Django-based web application for managing counties and their administrators.

## Project Structure

```
ManagementSystem/
├── counties/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   ├── static/
│   │   └── counties/
│   │       └── style.css
│   ├── templates/
│   │   └── counties/
│   │       ├── all_admins.html
│   │       ├── county.html
│   │       ├── edit.html
│   │       ├── index.html
│   │       └── login.html
├── ManagementSystem/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── templates/
│   └── admin/
│       └── base_site.html
├── db.sqlite3
├── manage.py
├── requirements
└── .gitignore
```

## Requirements

- Python 3.8+
- Django 5.1.7
- Gunicorn 23.0.0

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/rarespana/ManagementSystem.git
    cd ManagementSystem
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements
    ```

4. Apply migrations:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Usage

- Access the admin interface at `http://127.0.0.1:8000/admin/` to manage users and counties.
- Use the main application at `http://127.0.0.1:8000/` to view and manage counties and their administrators.

## Features

- User authentication and management
- County management
- Administrator assignment to counties
- Custom user model with additional fields

## License

This project is licensed under the MIT License.
