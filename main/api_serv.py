
import requests

class Api_post:
    
    @staticmethod
    def apifree():
        api = requests.get('https://jsonplaceholder.typicode.com/photos')
        if api:
            print("Success!")
        else:
            raise Exception(f"Non-success status code: {api.status_code}")
        result = api.json()
        list_Api = list(result)
        return list_Api[1:100] 

    @staticmethod
    def apifree_info():
        api = requests.get('https://date.nager.at/api/v2/publicholidays/2024/UA')
        if api:
            print("Success!")
        else:
            raise Exception(f"Non-success status code: {api.status_code}")
        
        result = api.json()
        list_result = list(result)
        return list_result[:6] 
       
        

   
api_input = Api_post()