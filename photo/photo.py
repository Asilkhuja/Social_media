from fastapi import APIRouter, UploadFile


photo_router = APIRouter(prefix='/photo', tags=['Фотки'])


#Получить все или определенное фото
@photo_router.get('/get-photos')
async def gat_all_or_exact_photo(photo_id: int = None):
    pass

#Добавление фото (для аватарки)
@photo_router.post('/add-photo')
async def add_user_photo(photo_file: UploadFile, user_id: int):
    #Сохранить локально фото
    with open(f'media/{photo_file.filename}', 'wb') as file:
        user_photo = await photo_file.read()

        file.write(user_photo)

    return {'message': 'сохранил'}



#Изменить фото (для аватарки)
@photo_router.put('/edit-photo')
async def edit_profile_photo(photo_id: int, new_photo_file):
    pass

#Удалить фото
@photo_router.delete('/delete-photo')
async def delete_photo(photo_id: int):
    pass