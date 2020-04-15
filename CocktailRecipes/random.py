import requests
import json
import urllib.request
from PIL import Image

url = 'https://www.thecocktaildb.com/api/json/v1/1/random.php'
r = requests.get(url)
recipe = json.loads(r.content)
data = list(recipe.items())[0][1][0]

def number_of_ingredients():
    number = 1
    for i in range(2, 16):
        index = 'strIngredient{}'.format(i)
        if data[index] is None:
            return number
        else:
            number += 1
            continue


class cocktail:
    def __init__(self, drink, glass, instructions, ingredients, category):
        self.drink = drink
        self.glass = glass
        self.instructions = instructions
        self.ingredients = ingredients
        self.category = category


def contents():
    a = {}
    n = number_of_ingredients()
    for i in range(1, n + 1):
        ingredient_index = 'strIngredient{}'.format(i)
        amount_index = 'strMeasure{}'.format(i)
        ingredient = data[ingredient_index]
        amount = data[amount_index]
        a[amount] = ingredient
    amounts = a.items()
    return amounts


random = cocktail(str(data['strDrink']), str(data['strGlass']), str(data['strInstructions']), contents(),
                  str(data['strCategory']))
img = "{}/preview".format(data['strDrinkThumb'])
urllib.request.urlretrieve(img, "{}.jpg".format(random.drink))
pic = Image.open("{}.jpg".format(random.drink))
method = ['{}: {}'.format(i, a) for a, i in random.ingredients if a is not None]
add = [a for a, i in random.ingredients if a is None]
print("{}\n({})\n\nServe in a {}".format(random.drink, random.category, random.glass))
print("\nIngredients:\n")
if len(add) == 0:
    for i in method:
        print(i)
else:
    print(add)
    for i in method:
        print(i)
print("\nInstructions: {}\n".format(random.instructions))
pic.show()
