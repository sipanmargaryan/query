from django.urls import path

from .views import OrderView

app_name = 'order'
urlpatterns = [
    path('test_view/', OrderView.as_view(), name='test_view'),
]
