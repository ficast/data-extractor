class Extractor:

    def __init__(self, requests, registerer):
        self.data = []
        self.requests = requests

    def get_data(self, base_url, start_date, end_date, auth, page=1) -> bytes:
        url = base_url.format(start_date, end_date, page)
        try:
            response = self.requests.get(url, headers={'Authorization': auth})
            return response
        except Exception as e:
            print(e)
            return b""

    def fetch_first_page(self, base_url, start_date, end_date, auth):
        try:
            response = self.get_data(base_url, start_date, end_date, auth)
            first_page = dict(response.json())
            self.total_pages = first_page["total"]
            self.registerer.save(response.content, base_name='file',
                            page=1, reg_date=end_date)
        except Exception as e:
            print(e)

    def fetch_content(self, base_url, start_date, end_date, auth):

        start_page = 2 if self.first_page else 1

        if start_page == 1:
            self.fetch_first_page(base_url, start_date, end_date, auth)

        for i in range(2, self.total_pages+1):
            response = self.get_data(
                base_url, start_date, end_date, auth, page=i)
            curr_page_data = response.content
            self.registerer.save(response.content, base_name='file',
                            page=1, reg_date=end_date)
