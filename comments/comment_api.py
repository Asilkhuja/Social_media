from fastapi import APIRouter

from comments import CommentModel, EditCommentModel


#Создаем компонент
comment_router = APIRouter(prefix='/comment', tags=['Работа с комментариями'])


#Запрос на публикацию кооментария
@comment_router.post('/add_comment')
async def add_comment(data: CommentModel):
    pass


#Запрос на изменение комментария
@comment_router.post('/change_comment')
async def change_comment(data: EditCommentModel):
    pass


#Запрос на удаление комментария
@comment_router.delete('/delete_comment')
async def delete_comment(comment_id: int):
    pass


#Запрос на получение комментария к определенной публикации
@comment_router.get('/get_comments')
async def get_comments(post_id: int):
    pass


#Запрос на добавление фото для публикации
@comment_router.post('/add_photo')
async def add_photo():
    pass


#Запрос на удаление фотографии к публикации
@comment_router.delete('/delete_photo')
async def delete_photo():
    pass