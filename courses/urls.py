from django.urls import path
from .views import home, detail_view, detail_view_category

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:id>/', detail_view , name='detail'),
    path('detail/category/<int:id>/', detail_view_category , name='detail_category'),
]