# FastAPI-notes-app
A basic Notes application built with FastAPI, SQLAlchemy, and JWT authentication. This project demonstrates user registration, login, and authenticated CRUD operations on notes.

## Features

- User registration and JWT-based login
- Create, Read, Update, Delete notes (per user)
- SQLite as the database (easy to run locally)
- Swagger UI for testing APIs
- Modular project structure (models, routers, schemas)

To run this project locally, clone the repository, create a virtual environment using python -m venv venv, and activate it (venv\Scripts\activate on Windows or source venv/bin/activate on macOS/Linux). Then install dependencies using pip install -r requirements.txt, and start the server with uvicorn main:app --reload. Once running, you can access the API documentation at http://127.0.0.1:8000/docs.
