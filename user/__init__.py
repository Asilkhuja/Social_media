from pydantic import BaseModel

#Валидатор изменения данных пользователя
class EditUserModel(BaseModel):
    user_id: int
    edit_data: str
    new_data: str

#Валидатор регистрации пользователя
class UserRegisterModel(BaseModel):
    name: str
    surname: str
    email: str
    phone_number: str
    city: str
    profile_photo: str
    password: str

#Валидатор входа в аккаунт
class UserLoginModel(BaseModel):
    mail: str
    password: str
