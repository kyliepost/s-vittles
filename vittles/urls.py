from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from vittlesapi.views.tag import TagView
from vittlesapi.views import register_user, login_user
from rest_framework import routers
from vittlesapi.views.family import FamilyView
from vittlesapi.views.familyBook import FamilyBookView
from vittlesapi.views.recipe import RecipeView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'families', FamilyView, 'family')
router.register(r'familyBook', FamilyBookView,'familyBook')
router.register(r'recipes', RecipeView, 'recipe')
router.register(r'tags', TagView, 'tag')

urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
