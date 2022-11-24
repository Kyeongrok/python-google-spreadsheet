import requests


class ApiTester:
    host = ""
    api_endpoint = ""

    def __init__(self, host):
        self.host = host

    def post(self, obj):
        # 등록 하는 기능
        url = f'{self.host}{self.api_endpoint}'
        r = requests.post(url, data=obj)
        print(r)  # status code출력

    def get(self):
        # 조회 하는 기능
        url = f'{self.host}{self.api_endpoint}'
        r = requests.get(url)
        return r.json()

    def createAndRead(self, obj):
        self.post(obj)
        r = self.get()
        print(r)


if __name__ == '__main__':
    print("eee")
