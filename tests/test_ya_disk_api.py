import pytest
from ya_disk_folder import YaDiskWorkspace


class TestYaDisk:
    def setup_method(self):
        self.ya_disk_client = YaDiskWorkspace()

    def test_create_folder(self):
        response = self.ya_disk_client.create_folder("test_folder")
        assert response.status_code == 201

    def test_check_folder(self):
        response = self.ya_disk_client.check_folder("test_folder")
        assert response.status_code == 200

    @pytest.mark.parametrize(
        "folder_name, expected",
        [
            ("test_folder", 204),
            ("test_folder", 404),
        ],
    )
    def test_delete_folder(self, folder_name, expected):
        response = self.ya_disk_client.delete_folder(folder_name)
        assert response.status_code == expected
