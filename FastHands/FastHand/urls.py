from django.urls import path
from .views import UsersViewSet, UsersDetailView

urlpatterns = [
    path('', UsersViewSet.as_view()),
    path('FastHand/<int:pk>/', UsersDetailView.as_view()),
]