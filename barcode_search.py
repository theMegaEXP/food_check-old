import requests
import json
from pyhidden import fdc_api_key

def get_ingredients(barcode):
    url = 'https://api.nal.usda.gov/fdc/v1/foods/search'
    params = {
        'api_key': fdc_api_key,
        'query': barcode,
        'dataType': 'Branded'
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        try: 
            data = json.loads(response.text)
            return data['foods'][0]['ingredients']
        except (IndexError, AttributeError):
            return False
    else:
        return False
    

        

