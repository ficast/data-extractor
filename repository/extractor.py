class Extractor:

    def __init__(self, requests, registerer):
        self.data = []
        self.requests = requests
        self.registerer = registerer
        self.first_page = None

    def get_data(self, base_url, start_date, end_date, auth, page=1) -> bytes:
        url = base_url.format(s=start_date, e=end_date, p=page)
        try:
            response = self.requests.get(url, headers={'Authorization': auth})
            return response
        except Exception as e:
            print(e)
            return b""

    def fetch_first_page(self, base_url, start_date, end_date, auth):
        try:
            response = self.get_data(base_url, start_date, end_date, auth)
            self.first_page = dict(response.json())
            self.total_pages = self.first_page["total"]
            print(self.first_page["total"])
            self.registerer(response.content, base_name='file', page=1)
        except Exception as e:
            print(e)

    def fetch_content(self, base_url, start_date, end_date, auth):

        start_page = 2 if self.first_page else 1

        if start_page == 1:
            self.fetch_first_page(base_url, start_date, end_date, auth)

        for i in range(2, self.total_pages+1):
            try:
                response = self.get_data(
                    base_url, start_date, end_date, auth, page=i)
                self.registerer(response.content, base_name='file', page=i)
            except Exception as e:
                print(e)
