from django.urls import path
from .views import IndexAPI

urlpatterns = [
    path('index/', IndexAPI.as_view()),
    #path('api/', admin.site.urls),
]
