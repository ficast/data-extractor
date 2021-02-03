from datetime import date
from utils import format_date
from abc import ABC, abstractmethod


class FileRegister(ABC):

    def __init__(self):
        self.format_date = format_date

    def save(self, data: bytes, base_name='file', page=1, reg_date=date.today()):
        day, month, year = self.format_date(reg_date)
        self.__register(day, month, year, data, base_name, page)

    @abstractmethod
    def __register(self, day, month, year, data: bytes, base_name='file', page=1):
        """ Should be implemented in inheritance """
        pass

    def format_url(self, year, month, day, base_name, page, base_url=""):
        """ base_url should end with '/'
            Example: base_url='raw/batch_layer/' 
        """

        return f"{base_url}{year}/{month}/{day}/{base_name}_{year}_{month}_{day}__{page:04d}.json"
