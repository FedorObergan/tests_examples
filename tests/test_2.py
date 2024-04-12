import pytest
import requests




class TestYandexDisk:
    def setup_class(self):
        POLYGON_TOKEN = '' # впишите токен с Яндекс Полигона
        self.headers = {
            'Authorization': f'OAuth {POLYGON_TOKEN}'
        }

    def test_create_folder(self):
        url_create_folder = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {
            'path': 'Photos'
        }
        response = requests.put(url_create_folder, params=params, headers=self.headers)

        assert response.status_code == 201

    def test_create_folder_again(self):
        url_create_folder = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {
            'path': 'Photos'
        }
        response = requests.put(url_create_folder, params=params, headers=self.headers)

        assert response.status_code == 409

    def test_forget_path(self):
        url_create_folder = 'https://cloud-api.yandex.net/v1/disk/resources'
        response = requests.put(url_create_folder, headers=self.headers)

        assert response.status_code == 400

    def test_forget_headers(self):
        url_create_folder = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {
            'path': 'Photos'
        }
        response = requests.put(url_create_folder, params=params)

        assert response.status_code == 401
