from repository import Extractor, FileRegister, S3Register
import requests

class ExtractorAndRegister:

    def __init__(self, extractor: Extractor, register: S3Register):
        self.register = S3Register()
        self.extractor = Extractor(requests=requests, registerer=register.save)
        
    def start(base_url, start_date, end_date, auth):
        self.extrator.fetch_content(base_url, start_date, end_date, auth)




