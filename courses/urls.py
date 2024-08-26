from django.urls import path
from .views import home, detail_view

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:id>/', detail_view , name='detail'),
]