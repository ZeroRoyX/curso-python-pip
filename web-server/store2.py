import requests

url_categories = 'https://api.escuelajs.co/api/v1/categories'
url_products = 'https://api.escuelajs.co/api/v1/products'
url_users = 'https://api.escuelajs.co/api/v1/users'

def get_categories():
    r = requests.get(url_categories)
    print(r.status_code)
    print(type(r.text))
    categories = r.json()

    for category in categories:
        print(category['name'])

def get_products():
    r = requests.get(url_products)
    # print(r.text)
    products = r.json()
    # print(products)

    # unique_keys = set()
    
    # for product in products:
    #     # print(product.keys())
    #     for key in product.keys():
    #         unique_keys.add(key)

    # print(unique_keys)
    # print(type(unique_keys))
# ---

    for product in products:
        print(product['title'])

def get_users():
    r = requests.get(url_users)
    print(r.text)

    users = r.json()

    for user in users:
        print(user['avatar'])







