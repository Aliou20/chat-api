from django.urls import path , include
from .views import LoginView, RegisterView, RefreshView , UserProfileView , MeView
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)

router.register('profile' , UserProfileView)

urlpatterns = [
    path('' , include(router.urls)),
    path('login', LoginView.as_view()),
    path('register', RegisterView.as_view()),
    path('refresh', RefreshView.as_view()),
    path('me', MeView.as_view()),
    
]