import requests
import json
import os


class YaDiskWorkspace:
    def __init__(self):
        file_path = os.path.abspath(os.path.dirname(__file__))
        with open(file_path + "\\data.json", encoding="utf-8") as token_file:
            data = json.load(token_file)
            token = data["token"]

        self.token = token
        self.base_url = "https://cloud-api.yandex.net/v1/disk/resources"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": "OAuth " + token
        }

    def create_folder(self, folder_name):
        params = {"path": folder_name}
        response = requests.put(self.base_url, headers=self.headers, params=params)
        return response

    def delete_folder(self, folder_name):
        params = {"path": folder_name}
        response = requests.delete(self.base_url, headers=self.headers, params=params)
        return response

    def check_folder(self, folder_name):
        params = {"path": folder_name}
        response = requests.get(self.base_url, headers=self.headers, params=params)
        return response


if __name__ == '__main__':
    ya_disk_client = YaDiskWorkspace()
    print(ya_disk_client.create_folder("test_folder"))
    print(ya_disk_client.delete_folder("test_folder"))
    print(ya_disk_client.check_folder("test_folder"))
