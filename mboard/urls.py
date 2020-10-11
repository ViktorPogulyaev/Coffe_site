from django.urls import path

from .views import index, by_classification

urlpatterns = [
    path('<int:classification_id>/', by_classification, name='by_classification'),
    path('', index, name='index'),
]