# from django.urls import path

# from cats.views import cat_list, hello

# urlpatterns = [
#    path('cats/', cat_list),
#    path('hello/', hello),
# ]

#################################################################################################
# Пример на классах
#################################################################################################
# urls.py
from django.urls import path

from cats.views import APICat

urlpatterns = [
    path('cats/', APICat.as_view()),
]
