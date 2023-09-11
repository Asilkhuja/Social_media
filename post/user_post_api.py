from fastapi import APIRouter, UploadFile, Body

from post import PublicPostModel, EditPostModel

#Создаем компонент
posts_router = APIRouter(prefix='/user_post', tags=['Работа с публикациями'])


#Запрос на публикацию поста
@posts_router.post('/public_post')
async def public_post(data: PublicPostModel):
    pass


#Запрос на изменение текста
@posts_router.put('/change_post')
async def change_post(data: EditPostModel):
    pass


#Запрос на удаление публикации
@posts_router.delete('/delete_post')
async def delete_post(post_id: int, user_id: int):
    pass


#Запрос на получение публикации
@posts_router.get('/get_all_posts')
async def get_all_posts():
    pass


#Запрос на добавление фото для публикации
@posts_router.post('/add_photo')
async def add_photo(user_id: int = Body(),
                    post_id: int = Body(),
                    photo_file: UploadFile = None):
    pass


#Запрос на удаление фотографии к публикации
@posts_router.delete('/delete_photo')
async def delete_photo(photo_id: int, user_id: int):
    pass