from repository import Extractor, FileRegister, S3Register
from repository.utils import format_date, set_date_before_today
import requests
import boto3


class ExtractorAndRegister:

    def __init__(self, extractor: Extractor, register: S3Register):
        self.register = S3Register(session, s3_resource, s3_path, bucket_name)
        self.extractor = extractor(requests=requests, registerer=register.save)

    def start(self, base_url, start_date, end_date, auth):
        self.extractor.fetch_content(base_url, start_date, end_date, auth)
