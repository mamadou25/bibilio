from django.urls import path

from . import views 

urlpatterns = [
    path('',views.home),
    path('add',views.add),
    path('pop',views.pop),
    path('genre',views.genre),
    path('voir',views.voir),
    path('genreplus',views.genreplus),
    path('nouveauté',views.nouveauté),
    path('nouveautéplus',views.nouveautéplus)
    
    
]