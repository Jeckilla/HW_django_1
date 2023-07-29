from django.http import HttpResponse
from django.shortcuts import render

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

def home_page(request):
    template_home = 'home.html'
    context = DATA
    return render(request, template_home, {'recipe': context})

def get_recipe(request, recipe):
    template_name = f'calculator/index.html'
    servings = int(request.GET.get('servings', 1))
    if recipe in DATA:
        recipe_query = DATA[recipe]
        context = {}
        context[recipe] = recipe_query
        for recipe, ingridients in context.items():
            for product, gr in ingridients.items():
                ingridients[product] = float(gr) * servings
            context = {recipe: ingridients}
    else:
        context = {}
    return render(request, template_name, {'recipe': context})

