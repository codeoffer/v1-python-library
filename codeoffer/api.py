import requests


class Request:
    def __init__(self, method, url, data=None, headers=None):
        self.method = method
        self.url = url
        self.data = data
        self.headers = headers or {}


class Response:
    def __init__(self, status, code, message, data, experimental):
        self.status = status
        self.code = code
        self.message = message
        self.data = data
        self.experimental = experimental


class Controller:
    @staticmethod
    def sendrequest(request):
        response = requests.request(request.method, request.url, data=request.data, headers=request.headers)
        json_data = response.json()
        code = json_data["code"]
        message = json_data["message"]
        data = json_data["data"]
        experimental = json_data["experimental"]
        return Response(response.status_code, code, message, data, experimental)
