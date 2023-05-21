import requests

url = 'https://script.google.com/macros/s/AKfycbypkokVPVlW2GvCK1DehSFoWbS2ngEayqLClBPRL76-RcU_SOxnZs_iAfQucov54GSf/exec'
response = requests.get(url)
# response2 = requests.get(url)
inner_data = response.json()['data']

total_cost = 0
gluten_free_cost = 0


for product_data in inner_data:
    print(product_data)

    price = product_data['price']
    residue = product_data['residue']
    contains_gluten = product_data['contains_gluten']

    total_cost += residue * price
    if not contains_gluten:
        gluten_free_cost += residue * price

print("Загальна вартість всіх товарів: ", total_cost)
print("Вартість товарів без глютену: ", gluten_free_cost)
