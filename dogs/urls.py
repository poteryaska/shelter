from django.urls import path


from dogs.apps import DogsConfig
from dogs.views import index, categories, dogs

app_name = DogsConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('categories/', categories, name='categories'),
    path('<int:pk>/dogs/', dogs, name='dogs'),
]