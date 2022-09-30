import json
import requests
import datetime
import time





class YD_user:
    def __init__(self, token: str):
        self.token = token
        
    def add_directory(self, name_dir):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        # today = datetime.date.today()
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}
        params = {'path': name_dir}
        response = requests.put(upload_url, headers = headers, params=params)
        # print(response.status_code)
        return response.status_code
        
    def dir_name(a,b):
        return a + b

if __name__ =='__main__':
    Yandex_token = input('Введите токен с полигона ЯндексДиск: ')
    nikita = YD_user(Yandex_token)
    nikita.add_directory('Папка')