import json
import requests

class Api_post:
    
    @staticmethod
    def apifree():
        api = requests.get('https://jsonplaceholder.typicode.com/photos')
        print( f"good api works {api.status_code}")
        result = api.json()
        list_Api = list(result)
        return list_Api[1:100] 

   
api_input = Api_post()