from fastapi import APIRouter, Response
from config.database import conn
from models.user import users
from schemas.user import User
from starlette.status import HTTP_204_NO_CONTENT

from cryptography.fernet import Fernet


user = APIRouter()

key = Fernet.generate_key()
f = Fernet(key)


@user.get("/users")
async def get_users():
    return conn.execute(users.select()).fetchall()


@user.post('/users')
async def create_user(user: User):
    new_user = {'name': user.name, 'email':user.email}
    new_user['password'] = f.encrypt(user.password.encode('utf-8'))
    result = conn.execute(users.insert().values(new_user))
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()


@user.get('/users/{id}')
async def get_user_by_id(id: str):
    return conn.execute(users.select().where(users.c.id == id)).first()


@user.delete('/users/{id}')
async def delete_user_by_id(id: str):
    result =  conn.execute(users.delete().where(users.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)