import json
import requests

class Api_post:
    
    @staticmethod
    def apifree():
        api = requests.get('https://jsonplaceholder.typicode.com/photos')
        
        result = api.json()
        list_Api = list(result)
        return list_Api[1:100] 

    @staticmethod
    def apifree_image():
        api = requests.get('https://date.nager.at/api/v2/publicholidays/2024/UA')
        print( f"good api works 2 {api.status_code}")
        result = api.json()
       
        print(result)
        

   
api_input = Api_post()