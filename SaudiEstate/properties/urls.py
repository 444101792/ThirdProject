from django.urls import path
from . import views

app_name = 'properties'

urlpatterns = [
    path('<int:pk>/', views.property_detail, name='detail'),
]