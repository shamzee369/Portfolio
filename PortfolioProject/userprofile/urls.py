

from . import views
from django.urls import path
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('',views.firstpage_view,name='firstpage'),
    path('create/', views.register_view, name='create'),  # Create Profile view
    path('login/',views.login_view, name='login'),  # Login view,
    path('profile/',views.profile_view,name='profile'),
    path('logout/',views.logout_view,name='logout')

]
