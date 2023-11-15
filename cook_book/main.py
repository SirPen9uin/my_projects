import os


with open('Recipes.txt', 'r', encoding='utf8') as f:
    lines = f.readlines()

cook_book = {}
current_recipe = ''
current_ingredients = []
for line in lines:
    line = line.strip()
    if line:
        if not current_recipe:
            current_recipe = line
        elif line.isdigit():
            current_ingredients = []
        else:
            ingredient_name, quantity, measure = line.split(' | ')
            ingredient_info = {
                'ingredient_name': ingredient_name,
                'quantity': int(quantity),
                'measure': measure,
            }
            current_ingredients.append(ingredient_info)
    else:
        cook_book[current_recipe] = current_ingredients
        current_recipe = ''
        current_ingredients = []
if current_recipe:
    cook_book[current_recipe] = current_ingredients


def get_shop_list_by_dishes(dishes: list, person_count: int):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            ingredients = cook_book[dish]
            for ingredient in ingredients:
                name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']

                if name not in shop_list:
                    shop_list[name] = {'quantity': quantity, 'measure': measure}
                else:
                    shop_list[name] += quantity
        else:
            return 'Такое мы не умеем готовить'
    return shop_list

if __name__ == '__main__':
    print(cook_book.keys())
    print(get_shop_list_by_dishes(['Омлет'], 3))
    print(get_shop_list_by_dishes(['Утка по-пекински'], 1))
    print(get_shop_list_by_dishes(['Запеченный картофель'], 2))
    print(get_shop_list_by_dishes(['Фахитос'], 4))
    print(get_shop_list_by_dishes(['Оливье'], 2))