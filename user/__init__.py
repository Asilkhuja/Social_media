from pydantic import BaseModel


#Валидатор публикации поста
class UserModel(BaseModel):
    user_id: int
    new_info: str

class UserRegisterModel(BaseModel):
    name: str
    first_name: str
    mobile_number: int
    mail: str
    adress: str

class UserLoginModel(BaseModel):
    mail: str
    password: str
