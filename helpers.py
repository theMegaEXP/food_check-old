from datetime import datetime
import re

def format_datetime(date_str, time_str):
    date = datetime.strptime(date_str, '%m-%d-%Y')
    time = datetime.strptime(time_str, '%I:%M%p')

    combined_datetime =  datetime(date.year, date.month, date.day, time.hour, time.minute)
    formatted_datetime = combined_datetime.strftime('%Y-%m-%d %H:%M:%S')

    return formatted_datetime

def ingredients_to_array(ingredients):
    return [elem for elem in re.split(r', |\(|\)', ingredients) if elem != '']