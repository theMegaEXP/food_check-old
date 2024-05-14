import random
from datetime import datetime

class Generate:
    def barcode():
        return ''.join([str(random.randint(0, 9)) for _ in range(12)])
    
    def ingredients():
        ingredients = ['apple', 'banana', 'cherry', 'grape', 'orange', 'pear', 'tangerine', 'mango', 'watermelon', 'cantalope', 'honeydew', 'strawberry', 'blackberry', 'raspberr', 'blueberry', 'carrot', 'celary', 'brocoli', 'cabbage', 'onion', 'tomato', 'bell pepper', 'jalepenio']
        length = random.randint(3, 20)
        return [ingredients[random.randint(0, len(ingredients) - 1)] for _ in range(length)]
    
    def date():
        return datetime.today().strftime('%m-%d-%Y')
    
    def time():
        hour = str(random.randint(1, 12))
        hour_padded = f'0{hour}' if len(hour) < 2 else hour
        minute = str(random.randint(1, 12) * 5)
        ampm = 'AM' if random.randint(0, 1) == 0 else 'PM'
        return f"{hour_padded}:{minute}{ampm}"
