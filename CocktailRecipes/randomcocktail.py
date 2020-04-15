import requests
import json
import urllib.request

url = 'https://www.thecocktaildb.com/api/json/v1/1/random.php'
r = requests.get(url)
recipe = json.loads(r.content)
data = list(recipe.items())[0][1][0]
name = data['strDrink']
id = data['idDrink']
print(name)
print(id)
