from django.urls import path
from . import views

urlpatterns = [
    path('', views.base_test, name='base-test'),
    path('receipe/', views.recipe_list, name='receipe'),
    path('recipes/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('contact/', views.contact_page, name='contact'),
    path('about/', views.about_page, name='about'),
    path('blog/', views.blog_view, name='blog'),
    path('element/', views.element_page, name='element'),
]
