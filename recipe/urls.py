from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('recipes/', views.RecipeListView.as_view(), name="recipes"),
    path('recipe/<int:pk>', views.RecipeDetailView.as_view(), name='recipe-detail'),
    path("myrecipes/", views.RecipeByUserListView.as_view(), name='my-recipe'),
    path("diets/", views.DietListView.as_view(), name='diets'),
    path("diet/<int:pk>", views.DietDetailView.as_view(), name='diet-detail'),
    path("recipe/create/", views.RecipeCreate.as_view(), name='recipe-create'),
    path("recipe/<int:pk>/update/", views.RecipeUpdateView.as_view(), name='recipe-update'),
    path("recipe/<int:pk>/delete/", views.RecipeDelete.as_view(), name='recipe-delete'),
    path("diet/create/", views.DietCreate.as_view(), name='diet-create'),
    path("diet/<int:pk>/update/", views.DietUpdate.as_view(), name='diet-update'),  # not using, add admin 2 site?
    path('register/', views.register_page, name='register')

]