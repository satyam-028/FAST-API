# FastAPI CRUD API 🚀

A simple and beginner-friendly **CRUD REST API** built using **FastAPI, SQLAlchemy, Pydantic, and SQLite**.

This project demonstrates how to build a backend API with database integration and perform basic CRUD operations:

* Create items
* Read all items
* Read a single item
* Update items
* Delete items

---

## 📌 Project Overview

This project is a basic FastAPI backend application that uses:

* **FastAPI** — Web framework for building APIs
* **Uvicorn** — ASGI server for running the FastAPI application
* **SQLAlchemy** — ORM for database operations
* **SQLite** — Lightweight relational database
* **Pydantic** — Request validation and response serialization
* **CORS Middleware** — Allows frontend applications to communicate with the API

The application automatically creates the required database table when the server starts.

---

## 🛠️ Tech Stack

| Technology | Purpose                        |
| ---------- | ------------------------------ |
| Python     | Programming language           |
| FastAPI    | API framework                  |
| Uvicorn    | Application server             |
| SQLAlchemy | ORM / Database interaction     |
| SQLite     | Database                       |
| Pydantic   | Data validation                |
| CORS       | Frontend-backend communication |

---

## 📂 Project Structure

```text
FAST-API/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── requirements.txt
├── Procfile
├── .gitignore
└── crud.db
```

### `main.py`

Contains the FastAPI application and all CRUD API endpoints.

It also contains:

* FastAPI app configuration
* CORS configuration
* Database dependency
* CRUD operations
* Error handling

### `database.py`

Responsible for database configuration.

The project uses SQLite:

```python
DATABASE_URL = "sqlite:///./crud.db"
```

SQLAlchemy engine and database sessions are also configured here.

### `models.py`

Contains the SQLAlchemy database model.

The `Item` model contains:

```text
id
name
description
price
```

### `schemas.py`

Contains Pydantic schemas used for:

* Request validation
* Creating items
* Returning item responses

### `requirements.txt`

Contains the Python dependencies required to run the project.

### `Procfile`

Contains the command used to start the application on platforms that support a Procfile:

```text
web: uvicorn main:app --host=0.0.0.0 --port=$PORT
```

---

# ⚡ Features

## 1. Create Item

Create a new item using:

```http
POST /items/
```

Example request:

```json
{
    "name": "Laptop",
    "description": "Gaming Laptop",
    "price": 75000
}
```

---

## 2. Get All Items

Retrieve all items:

```http
GET /items/
```

The API also supports pagination using:

```text
skip
limit
```

Example:

```http
GET /items/?skip=0&limit=10
```

---

## 3. Get Single Item

Retrieve a specific item using its ID:

```http
GET /items/{item_id}
```

Example:

```http
GET /items/1
```

If the item does not exist, the API returns:

```json
{
    "detail": "Item not found"
}
```

with HTTP status:

```text
404 Not Found
```

---

## 4. Update Item

Update an existing item:

```http
PUT /items/{item_id}
```

Example:

```http
PUT /items/1
```

Request body:

```json
{
    "name": "Updated Laptop",
    "description": "Updated gaming laptop",
    "price": 80000
}
```

---

## 5. Delete Item

Delete an item:

```http
DELETE /items/{item_id}
```

Example:

```http
DELETE /items/1
```

Successful response:

```json
{
    "message": "Item deleted successfully"
}
```

---

# 🗄️ Database

This project uses **SQLite** with SQLAlchemy.

The database URL is:

```python
sqlite:///./crud.db
```

The database file is:

```text
crud.db
```

The main database table is:

```text
items
```

### Item Table

| Column      | Type    | Required |
| ----------- | ------- | -------- |
| id          | Integer | Yes      |
| name        | String  | Yes      |
| description | String  | No       |
| price       | Float   | Yes      |

---

# 🔄 CRUD Flow

The application follows this basic flow:

```text
Client
   │
   ▼
FastAPI
   │
   ▼
Pydantic Schema
   │
   ▼
SQLAlchemy
   │
   ▼
SQLite Database
```

For example, when creating an item:

```text
POST /items/
      ↓
FastAPI receives request
      ↓
Pydantic validates data
      ↓
SQLAlchemy creates database object
      ↓
SQLite stores the item
      ↓
FastAPI returns JSON response
```

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/satyam-028/FAST-API.git
```

Move into the project directory:

```bash
cd FAST-API
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

Start the FastAPI server using Uvicorn:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

or:

```text
http://localhost:8000
```

---

# 📚 API Documentation

FastAPI automatically generates interactive API documentation.

## Swagger UI

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger allows you to:

* View all endpoints
* Send GET requests
* Send POST requests
* Send PUT requests
* Send DELETE requests
* Test request bodies
* View response schemas

---

## ReDoc

FastAPI also provides ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

# 🔗 API Endpoints

| Method | Endpoint           | Description      |
| ------ | ------------------ | ---------------- |
| GET    | `/`                | Check API status |
| POST   | `/items/`          | Create an item   |
| GET    | `/items/`          | Get all items    |
| GET    | `/items/{item_id}` | Get one item     |
| PUT    | `/items/{item_id}` | Update an item   |
| DELETE | `/items/{item_id}` | Delete an item   |

---

# 🧪 Example API Usage

## Create Item

```http
POST /items/
Content-Type: application/json
```

```json
{
    "name": "Keyboard",
    "description": "Mechanical Keyboard",
    "price": 2500
}
```

Response:

```json
{
    "id": 1,
    "name": "Keyboard",
    "description": "Mechanical Keyboard",
    "price": 2500
}
```

---

## Get Items

```http
GET /items/
```

Example response:

```json
[
    {
        "id": 1,
        "nam
```
