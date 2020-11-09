from django.urls import path

from .views import index, by_classification, BBCreateView

urlpatterns = [
    path('<int:classification_id>/', by_classification, name='by_classification'),
    path('add/', BBCreateView.as_view(), name='add'),
    path('', index, name='index'),
]