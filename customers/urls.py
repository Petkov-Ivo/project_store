from django.urls import path, include

from customers.views import signup_user, logout_user, login_user, user_profile

urlpatterns = [

    path('profile/<int:pk>/', user_profile, name='user profile'),
    path('signup/', signup_user, name='signup user'),
    path('logout/', logout_user, name='logout'),
    path('login/', login_user, name='login'),
]

