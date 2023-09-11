from fastapi import APIRouter

from user import UserModel, UserRegisterModel, UserLoginModel
#Создаем компонент
user_router = APIRouter(prefix='/user', tags=['Управление с пользователями'])


#Запрос на входа в аккаунт
@user_router.post('/login')
async def login_user(dara: UserLoginModel):
    pass


#Запрос на регистрацию пользователя
@user_router.post('/register')
async def register_user(data: UserRegisterModel):
    pass


#Запрос на изменение информации пользователя
@user_router.put('/change_info')
async def change_info(data: UserModel):
    pass


#Запрос на получение информации о пользователе
@user_router.get('/get_user')
async def get_user(user_id: int):
    pass