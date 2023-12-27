from django.urls import path
from .views import get_advantage, get_navigation_menu

urlpatterns = [
    path('advantages/', get_advantage, name='advantage'),
    path('nav_menu/', get_navigation_menu, name='nav_menu')
]
