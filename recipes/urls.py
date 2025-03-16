from django.urls import path
from recipes.views import contact, home, about

urlpatterns = [
    path('', home),
    path('about/', about),
    path('contact/', contact),
]
