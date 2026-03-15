# FastAPI User Authentication & Management System

A RESTful API built with FastAPI featuring JWT authentication, user management, and MySQL database integration.

## Features

- ✅ User Registration & Login
- ✅ JWT Token Authentication
- ✅ Protected API Endpoints
- ✅ User Profile Management (CRUD Operations)
- ✅ Password Hashing with bcrypt
- ✅ MySQL Database Integration
- ✅ Input Validation with Pydantic
- ✅ Interactive API Documentation (Swagger UI)

## Tech Stack

- **Framework:** FastAPI
- **Database:** MySQL
- **ORM:** SQLAlchemy
- **Authentication:** JWT (JSON Web Tokens)
- **Password Hashing:** bcrypt
- **Validation:** Pydantic

## Project Structure

```
FastAPi/
├── routers/
│   ├── auth.py          # Authentication endpoints (register, login)
│   └── users.py         # User management endpoints (CRUD)
├── config.py            # Configuration and environment variables
├── database.py          # Database connection and session management
├── models.py            # SQLAlchemy database models
├── schemas.py           # Pydantic schemas for validation
├── main.py              # Application entry point
├── requirements.txt     # Project dependencies
├── .env.example         # Environment variables template
└── .gitignore          # Git ignore rules
```

## Installation

### Prerequisites

- Python 3.8+
- MySQL Server

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/lakshvarmacoder/fastapi-jwt-auth-api.git
   cd FastAPi
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup MySQL Database**
   ```sql
   CREATE DATABASE db;
   ```

5. **Configure environment variables**
   ```bash
   # Copy .env.example to .env
   cp .env.example .env
   
   # Edit .env and add your values
   SECRET_KEY=your-secret-key-here
   DATABASE_URL=mysql+pymysql://root:password@localhost/db
   ```

   To generate a secure SECRET_KEY:
   ```python
   import secrets
   print(secrets.token_urlsafe(32))
   ```

6. **Run the application**
   ```bash
   uvicorn main:app --reload
   ```

7. **Access the API**
   - API: http://127.0.0.1:8000
   - Interactive Docs: http://127.0.0.1:8000/docs
   - Alternative Docs: http://127.0.0.1:8000/redoc

## API Endpoints

### Authentication (Public)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Register new user |
| POST | `/auth/login` | Login and get JWT token |

### User Management (Protected - Requires JWT)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/users/` | Get all users |
| GET | `/users/{user_id}` | Get specific user |
| PUT | `/users/{user_id}` | Update user profile (own only) |
| DELETE | `/users/{user_id}` | Delete user account (own only) |

## Usage Examples

### 1. Register a User

```bash
curl -X POST "http://127.0.0.1:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "password123"
  }'
```

### 2. Login

```bash
curl -X POST "http://127.0.0.1:8000/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john@example.com",
    "password": "password123"
  }'
```

Response:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### 3. Access Protected Endpoint

```bash
curl -X GET "http://127.0.0.1:8000/users/" \
  -H "Authorization: Bearer <your-token-here>"
```

## Security Features

- **Password Hashing:** All passwords are hashed using bcrypt before storage
- **JWT Authentication:** Secure token-based authentication
- **Authorization:** Users can only modify their own data
- **Input Validation:** Pydantic models validate all inputs
- **Environment Variables:** Sensitive data stored in .env file

## Database Schema

### Users Table

| Column | Type | Constraints |
|--------|------|-------------|
| id | Integer | Primary Key, Auto Increment |
| username | String(50) | Not Null |
| email | String(100) | Unique, Not Null |
| hashed_password | String(255) | Not Null |
| is_active | Boolean | Default: True |
| created_at | DateTime | Default: UTC Now |

## Testing

Use the interactive Swagger UI at `http://127.0.0.1:8000/docs` to test all endpoints:

1. Register a new user
2. Login to get JWT token
3. Click "Authorize" button and paste token
4. Test protected endpoints

## Future Enhancements

- [ ] Email verification
- [ ] Password reset functionality
- [ ] Refresh tokens
- [ ] Rate limiting
- [ ] User roles and permissions
- [ ] Profile picture upload
- [ ] Pagination for user list
- [ ] Search and filter users

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.




