from django.shortcuts import render, reverse
from django.http import HttpResponse
DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def home_view(request, recipe1):


    i = request.GET.get("servings", "")
    print(i)

    if i :
        name_recipe = recipe1
        x = {}
        for k, v in DATA[name_recipe].items():
            x[k] = v * int(i)
            DATA[name_recipe].update(x)
        name_recipe = recipe1
        context = {
            "recipe": DATA[name_recipe]

        }
    else:
        name_recipe = recipe1
        context = {
            "recipe": DATA[name_recipe]

        }


    return render(request, template_name="calculator/index.html", context=context)