from django.urls import path


from dogs.apps import DogsConfig
from dogs.views import index, CategoryListView, DogDetailView

app_name = DogsConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('<int:pk>/dogs/', DogDetailView.as_view(), name='dogs'),
]