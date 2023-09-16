from fastapi import APIRouter, UploadFile

from user import UserRegisterModel, UserLoginModel, EditUserModel

from database.userservice import login_user_db, register_user_db, get_exact_users_db, get_all_users_db


#Создаем компонент
user_router = APIRouter(prefix='/user', tags=['Управление с пользователями'])


#Запрос на входа в аккаунт
@user_router.post('/login')
async def login_user(data: UserLoginModel):
    result = login_user_db(**data.model_dump())

    return {'status': 1, 'message': result}


#Запрос на регистрацию пользователя
@user_router.post('/register')
async def register_user(data: UserRegisterModel):
    result = register_user_db(**data.model_dump())

    if result:
        return {'status': 1, 'message': result}

    return {'status': 0, 'message': 'Пользователь с такой почтой уже есть в базе'}


#Запрос на изменение информации пользователя
@user_router.put('/change_info')
async def change_info(data: EditUserModel):
    pass


#Запрос на получение информации о пользователе
@user_router.get('/get_user')
async def get_user(user_id: int = 0):
    if user_id == 0:
        result = get_all_users_db()

        return {'status': 1, 'message': result}

    else:
        result = get_exact_users_db(user_id)

        return {'status': 1, 'message': result}