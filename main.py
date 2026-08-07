from fastapi import FastAPI, HTTPException, Path, Query, Body, Depends
from typing import Optional, List, Dict, Annotated
from sqlalchemy.orm import Session
from starlette import status

from models import Base, User, Friend
from database import engine, session_local
from schemas import UserCreate, User as DbUser, UserLogin, UserRecord

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
	db = session_local()
	try:
		yield db
	finally:
		db.close()

@app.post("/user/create")
async def create_user(user: UserCreate, db: Session = Depends(get_db)) -> bool:
	try:
		db_user = User(name=user.name, email=user.email, password=user.password)
		db.add(db_user)
		db.commit()
		db.refresh(db_user)

		return True
	except Exception as e:
		return False

@app.post("/user/login", response_model=DbUser)
async def login_user(user: UserLogin, db: Session = Depends(get_db)) -> DbUser:
	db_user = db.query(User).filter(
		User.email == user.email,
		User.password == user.password
	).first()
	if db_user is None:
		raise HTTPException(
			status_code=status.HTTP_401_UNAUTHORIZED,
			detail="Invalid email or password"
		)

	return db_user

@app.put("/user/update_record")
async def update_record(user: UserRecord, db: Session = Depends(get_db)):
	try:
		# Находим пользователя по id
		db_user = db.query(User).filter(User.id == user.id).first()

		# Обновляем рекорд
		db_user.record = user.record
		db.commit()
		db.refresh(db_user)

		print("Рекорд пользователя обновлен")
	except Exception as e:
		# Откатываем транзакцию в случае ошибки
		db.rollback()
		print(f"Ошибка при обновлении рекорда")

@app.get("/user/get_name")
async def get_name(name: str, db: Session = Depends(get_db)) -> bool:
	try:
		# Проверяем есть ли пользователь с таким же именем
		db_user = db.query(User).filter(User.name == name).first()

		if db_user is None:
			return True
		else:
			return False
	except Exception as e:
		print(f"Ошибка при проверки имени")
		return False