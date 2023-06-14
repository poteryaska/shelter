from django.shortcuts import render

from dogs.models import Category, Dog


def index(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Питонник: главная'
    }
    return render(request, 'dogs/index.html', context)


def categories(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Питонник: наши породы'
    }
    return render(request, 'dogs/categories.html', context)

def dogs(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Dog.objects.filter(category_id=pk),
        'title': f'Питонник: наши собаки породы {category_item.name}'
    }
    return render(request, 'dogs/dogs.html', context)