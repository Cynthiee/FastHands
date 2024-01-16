from django.urls import path
from .views import UsersViewSet

urlpatterns = [
    path('', UsersViewSet.as_view()),
]