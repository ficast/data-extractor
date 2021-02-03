from .file_register import FileRegister
import json
import os


class LocallyRegister(FileRegister):

    def __init__(self):
        super().__init__()

    def __register(self, day, month, year, data: bytes, base_name='file', page=1):

        dir_path = os.path.join(year, month, day)
        if os.path.exists(dir_path) == False:
            try:
                os.makedirs(dir_path)
            except OSError:
                print("path already exists")

        with open(self.format_url(year, month, day, base_name, page), "w") as write_file:
            json.dump(json.loads(data), write_file)
