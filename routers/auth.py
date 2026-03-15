from fastapi import APIRouter, Depends, HTTPException, status
from schemas import UserCreate, UserLogin, UserResponse
from sqlalchemy.orm import Session
from database import get_db
import bcrypt
from models import User
from jose import jwt
from datetime import datetime, timedelta
from config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_HOURS


router = APIRouter()

@router.post("/auth/register", response_model=UserResponse)
def register(user:UserCreate, db:Session = Depends(get_db)):
    try: 
        existing_user = db.query(User).filter(User.email == user.email).first()
        if existing_user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

        hashed_password = bcrypt.hashpw(
            user.password.encode(),
            bcrypt.gensalt()
        )

        new_user = User(
            username = user.username,
            email = user.email,
            hashed_password = hashed_password,
            is_active=True
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error creating user")


@router.post("/auth/login")
def login(user:UserLogin, db:Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user:
        raise  HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User Not Found")

    if not bcrypt.checkpw(user.password.encode(), db_user.hashed_password.encode()):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    payload = {
        "sub":str(db_user.id),
        "exp":datetime.utcnow() + timedelta(hours=ACCESS_TOKEN_EXPIRE_HOURS)
    }

    access_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }



