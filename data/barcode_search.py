import requests
import json

from pyhidden import fdc_api_key
from data.data import Foods

def get_product_ingredients(barcode):
    if Foods.check_barcode(barcode):
        return Foods.product_from_barcode(barcode), Foods.ingredients_from_barcode(barcode) 
    else:
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
                return data['foods'][0]['ingredients'], 'unavailable'
            except (IndexError, AttributeError):
                return False
        else:
            return False
   
        

