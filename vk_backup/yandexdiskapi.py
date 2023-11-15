import requests
import json
from tqdm import tqdm

class YandexDiskUploader():
    YA_BASE_URL = 'https://cloud-api.yandex.net'
    def __init__(self, token):
        self.token = token


    def create_folder(self):
        url = f'{self.YA_BASE_URL}/v1/disk/resources/'
        headers = {'Content-Type': 'application/json',
                   'Authorization': self.token}
        params = {'path': 'VKPhotosBackUp',
                  'overwrite': 'false'}
        response = requests.put(url=url, headers=headers, params=params)

    def upload_photo(self):
        with open('photos_info.json', 'r') as f:
            data = json.load(f)

        for file in tqdm(data, desc="Uploading files", unit="file"):
            file_name = file['file_name']
            headers = {
                       'Authorization': self.token
            }
            params = {
                'path': f'VKPhotosBackUp/{file_name}'
            }

            try:
                response = requests.get(
                    f'{self.YA_BASE_URL}/v1/disk/resources/upload',
                                        params=params,
                                        headers=headers
                )
                response.raise_for_status()  # Проверка на ошибку
                path_to_upload = response.json().get('href', '')

                with open(file_name, 'rb') as file_content:
                    upload_response = requests.put(
                        path_to_upload, files={"file": file_content}
                    )
                    upload_response.raise_for_status()  # Проверка на ошибку
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")