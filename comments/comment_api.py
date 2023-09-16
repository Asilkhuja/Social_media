from fastapi import APIRouter

from comments import CommentModel, EditCommentModel

from database.commentservice import change_comment_db, add_comment_db, delete_comment_db, get_post_comments

#Создаем компонент
comment_router = APIRouter(prefix='/comment', tags=['Работа с комментариями'])


#Запрос на публикацию кооментария
@comment_router.post('/add_comment')
async def add_comment(data: CommentModel):
    result = add_comment_db(**data.model_dump())

    return {'status': 1, 'message': result}


#Запрос на изменение комментария
@comment_router.post('/edit_comment')
async def change_comment(data: EditCommentModel):
    result = change_comment_db(**data.model_dump())

    if result:
        return {'status': 1, 'message': result}

    return {'status': 0, 'message': 'Комментарий не найден'}


#Запрос на удаление комментария
@comment_router.delete('/delete_comment')
async def delete_comment(comment_id: int):
    result = delete_comment_db(comment_id)

    if result:
        return {'status': 1, 'message': result}

    return {'status': 0, 'message': 'Комментарий не найден'}


#Запрос на получение комментария к определенной публикации
@comment_router.get('/get_comments')
async def get_comments(post_id: int):
    result = get_post_comments(post_id)

    return {'status': 1, 'message': result}


#Запрос на добавление фото для публикации
@comment_router.post('/add_photo')
async def add_photo():
    pass


#Запрос на удаление фотографии к публикации
@comment_router.delete('/delete_photo')
async def delete_photo():
    pass