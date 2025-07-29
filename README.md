# 📋 KPA Form Management Backend

A FastAPI-based backend system for managing KPA (Key Performance Area) form submissions, built with PostgreSQL.

## 🚀 Features

- Create and read KPA form entries
- RESTful API design
- Pydantic schema validation
- CORS-enabled for frontend integration
- Swagger UI documentation (`/docs`)

## 🛠️ Tech Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Schema Validation**: Pydantic
- **Deployment-ready** with environment config (`.env`)

## 📦 Project Structure

kpa_backend_fastapi/
├── app/
│ ├── init.py
│ ├── main.py
│ ├── crud.py
│ ├── database.py
│ ├── models.py
│ ├── routers/
│ │ └── kpaform.py
│ └── schemas.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt



## 📥 API Endpoints

- `GET /api/kpaformdata`: List all KPA form submissions
- `POST /api/kpaformdata`: Create a new KPA form submission
- `GET /`: Check server status

View Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 📄 .env Example

DATABASE_URL=postgresql://username:password@localhost:5432/dbname
