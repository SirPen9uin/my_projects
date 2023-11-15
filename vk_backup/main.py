from vk_backup.vkapi import VKPhotoDownloader
from vk_backup.yandexdiskapi import YandexDiskUploader
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN_VK = os.getenv('VK')
YA_TOKEN = os.getenv('TOKEN_YA')

if __name__ == '__main__':
    print('Профиль пользователя ВК должен быть открытым')
    user_id = input('Укажите id пользователя ВК: ')

    vk_client = VKPhotoDownloader(TOKEN_VK, user_id)
    vk_client.photo_save()

    ya_client = YandexDiskUploader(YA_TOKEN)
    ya_client.create_folder()
    ya_client.upload_photo()