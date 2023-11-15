from urllib.parse import urlencode
import requests
import json
from tqdm import tqdm
import datetime
import os
from dotenv import load_dotenv

class VKPhotoDownloader:
    API_BASE_URL = 'https://api.vk.com/method'
    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id

    def get_common_params(self):
        return {
            'access_token': self.token,
            'v': '5.131'
        }

    def build_url(self, api_method):
        return f'{self.API_BASE_URL}/{api_method}'


    def get_profile_photo(self):
        params = self.get_common_params()
        params.update({
            'owner_id': self.user_id,
            'album_id': 'profile',
            'extended': 1
        })
        response = requests.get(self.build_url('photos.get'), params=params)
        return response.json()


    def photo_save(self):
        photo_info = self.get_profile_photo()
        all_photos = photo_info['response']['items']
        best_resolution_all = {}
        num = 0
        print('По умолчанию сохраняется 5 фотографий.')
        print('Хотите изменить значение по умолчанию?')
        decision = input('Введите да или нет: ')
        names = []
        if decision.lower() == 'да':
            num = int(input('Введите количество сохраняемых фото: '))
        elif decision.lower() != 'да':
            print('Принято значение по умолчанию')
            num = 5
        for index, photo in enumerate(all_photos):
            if index == num:
                break
            else:
                photo_id = photo['id']
                url = photo['sizes'][-1]['url']
                name = str(photo['likes']['count'])
                if name in names:
                    name = f"{name}_{datetime.datetime.fromtimestamp(photo['date']).strftime('%Y-%m-%d')}"
                names.append(name)
                size = photo['sizes'][-1]['type']
                best_resolution_all[name] = {'url': url, 'size': size}
        file_info = []
        for name, data in tqdm(best_resolution_all.items(), desc="Downloading files", unit="file"):
            response = requests.get(data['url'])
            file_name = name + '.jpg'
            with open(file_name, 'wb') as f:
                f.write(response.content)
            file_info.append({
                'file_name': file_name,
                'size': data['size']
            })
        with open('photos_info.json', 'w') as f:
            json.dump(file_info, f, ensure_ascii=False, indent=4)

