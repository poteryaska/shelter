from django.shortcuts import render
from django.views import generic

from dogs.models import Category, Dog


def index(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Питонник: главная'
    }
    return render(request, 'dogs/index.html', context)


class CategoryListView(generic.ListView):
    model = Category
    extra_context = {
        'title': 'Питонник: наши породы'
    }

class DogDetailView(generic.DetailView):
    model = Dog
# def dogs(request, pk):
#     category_item = Category.objects.get(pk=pk)
#     context = {
#         'object_list': Dog.objects.filter(category_id=pk),
#         'title': f'Питонник: наши собаки породы {category_item.name}'
#     }
#     return render(request, 'dogs/dog_detail.html', context)