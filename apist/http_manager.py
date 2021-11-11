import requests
import jsonpath


class HttpManager:
    headers_without_auth = {'Content-Type': 'application/json'}

    #Не доделал
    @staticmethod
    def auth(url, body):
        result = requests.post(url,
                               json=body,
                               headers=HttpManager.headers_without_auth)
        HttpManager.jwt = jsonpath.jsonpath(result.json(), "jwt")
        return result

    @staticmethod
    def get(url, body=None, auth=False, head=None):
        if auth == False:
            heads = HttpManager.headers_without_auth
        if auth == True:
            heads = head
        result = requests.get(url, json=body, headers=heads, verify=False)
        return result

    @staticmethod
    def post(url, body=None, auth=False, head=None):
        if auth == False:
            heads = HttpManager.headers_without_auth
        if auth == True:
            heads = head
        result = requests.post(url, json=body, headers=heads, verify=False)
        return result

    @staticmethod
    def put_with_auth(url, body=None, auth=False, head=None):
        if auth == False:
            heads = HttpManager.headers_without_auth
        if auth == True:
            heads = head
        result = requests.put(url, json=body, headers=heads, verify=False)
        return result

    #Не доделал
    @staticmethod
    def delete(url):
        result = requests.delete(url,
                                 headers=HttpManager.headers_with_auth,
                                 cookies=HttpManager.cookie)
        return result
