import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code, r.text, type(r.text), sep='\n')
    categories = r.json()
    for category in categories:
        print(category['name'])
