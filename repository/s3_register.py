from file_register import FileRegister
from concurrent.futures import ThreadPoolExecutor


class S3Register(FileRegister):

    def __init__(self, session, s3_resource, s3_path, bucket_name, threads=4):
        """Example: session=boto3.session.Session(profile_name="default")"""
        super().__init__()
        self.session = session
        self.s3_resource = s3_resource
        self.s3_path = s3_path
        self.bucket_name = bucket_name
        self.threads = threads

    def _FileRegister__register(self, day, month, year, data: bytes, base_name='file', page=1):

        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            executor.submit(
                self.s3_resource.meta.client.put_object,
                Body=data,
                Bucket=self.bucket_name,
                Key=self.format_url(year, month, day, base_name, page, base_url=self.s3_path))
