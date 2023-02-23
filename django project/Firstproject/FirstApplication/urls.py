
from django.urls import path
from FirstApplication.views import home
urlpatterns = [
    path('', home,name="home"),
]
