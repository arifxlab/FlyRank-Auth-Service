# 🔐 FlyRank Auth Service

A production-style authentication service built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **JWT Authentication** as part of the **FlyRank Backend AI Engineering Internship**.

This project demonstrates secure user authentication using hashed passwords, JWT-based authorization, protected API routes, and a clean layered architecture.

---

## 📌 Features

- User Registration
- User Login
- Password Hashing with bcrypt
- JWT Access Token Generation
- JWT Validation
- Protected Routes
- Current Authenticated User Endpoint
- Health Check Endpoint
- PostgreSQL Database Integration
- SQLAlchemy ORM
- Alembic Database Migrations
- Swagger API Documentation
- Proper HTTP Status Codes (200, 201, 400, 401, 403)

---

## 🏗️ Architecture

```
Client
   │
   ▼
FastAPI Routers
   │
   ▼
Service Layer
   │
   ▼
Security Layer (JWT + Password Hashing)
   │
   ▼
SQLAlchemy ORM
   │
   ▼
PostgreSQL
```

---

## 📂 Project Structure

```
FlyRank-Auth-Service/
│
├── alembic/
│   └── versions/
│
├── app/
│   ├── api/
│   │   ├── auth.py
│   │   ├── protected.py
│   │   └── health.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   │
│   ├── database/
│   │   └── database.py
│   │
│   ├── dependencies/
│   │   └── auth.py
│   │
│   ├── models/
│   │   └── user.py
│   │
│   ├── schemas/
│   │   └── auth.py
│   │
│   ├── services/
│   │   └── auth_service.py
│   │
│   └── main.py
│
├── tests/
├── .env.example
├── alembic.ini
├── pyproject.toml
├── README.md
└── uv.lock
```

---

## 🛠️ Technology Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.11+ |
| Framework | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy 2.x |
| Migrations | Alembic |
| Authentication | JWT |
| Password Hashing | bcrypt + Passlib |
| Validation | Pydantic |
| API Docs | Swagger UI |

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/FlyRank-Auth-Service.git
cd FlyRank-Auth-Service
```

---

### Create Virtual Environment

```bash
uv venv
```

Activate it.

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

---

### Install Dependencies

```bash
uv sync
```

---

## Environment Variables

Create a `.env` file.

Example:

```env
APP_NAME=FlyRank Auth Service
APP_VERSION=1.0.0
DEBUG=True

DATABASE_URL=postgresql://postgres:password@localhost:5432/flyrank_auth

SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## Database Migration

Create database tables.

```bash
uv run alembic upgrade head
```

---

## Run the Server

```bash
uv run uvicorn app.main:app --reload
```

Server

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## Root

```
GET /
```

Returns service status.

---

## Health Check

```
GET /health
```

Returns application health information.

---

## Register User

```
POST /auth/register
```

Example Request

```json
{
    "email": "naruto@leaf.com",
    "password": "rasengan123"
}
```

Example Response

```json
{
    "id": 1,
    "email": "naruto@leaf.com"
}
```

---

## Login

```
POST /auth/login
```

Example Request

```json
{
    "email": "naruto@leaf.com",
    "password": "rasengan123"
}
```

Example Response

```json
{
    "access_token": "JWT_TOKEN",
    "token_type": "bearer"
}
```

---

## Current User

```
GET /me
```

Requires JWT Authentication.

Example Response

```json
{
    "id": 1,
    "email": "naruto@leaf.com"
}
```

---

## Admin Endpoint

```
GET /admin
```

Returns **403 Forbidden** for authenticated users without admin privileges.

---

# Authentication Flow

```
User Registers
        │
        ▼
Password Hashed
        │
        ▼
Stored in PostgreSQL
        │
        ▼
User Logs In
        │
        ▼
Password Verified
        │
        ▼
JWT Generated
        │
        ▼
Client Stores JWT
        │
        ▼
Authorization: Bearer <token>
        │
        ▼
Protected Endpoint
```

---

# HTTP Status Codes

| Code | Meaning |
|------|---------|
| 200 | Success |
| 201 | Resource Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |

---

# Security Features

- Passwords are securely hashed using bcrypt.
- JWT authentication using HS256.
- Protected endpoints require a valid Bearer token.
- Passwords are never returned in API responses.
- User credentials are validated before issuing access tokens.

---

# Assignment Objectives Achieved

- User Registration
- Secure Password Hashing
- User Login
- JWT Authentication
- Protected API Route
- Honest 401 Responses
- Honest 403 Responses
- PostgreSQL Integration
- Alembic Migrations
- Swagger Documentation

---

# Future Improvements

- Refresh Tokens
- Role-Based Access Control (RBAC)
- User Roles and Permissions
- Email Verification
- Password Reset
- Docker Support
- Automated Unit Tests
- Rate Limiting
- Structured Logging
- CI/CD Pipeline

---

# Author

**Arif Khan**

Backend AI Engineering Intern

Built as part of the **FlyRank Backend AI Engineering Internship**.