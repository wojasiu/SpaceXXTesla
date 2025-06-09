
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='main'),
    path('auth/', views.login_register_view, name='auth'),
    path('index/', views.index_view, name='index'),
    path('spacex/', views.home_view, name='home'),
    path('premium/', views.premium_view, name='premium'),
    path('tesla/', views.tesla_view, name='tesla-home'),
    path('tesla/kontakt/', views.tesla_kontakt_view, name='tesla-kontakt'),
    path('tesla/o-nas/', views.tesla_onas_view, name='tesla-onas'),
    path('logout/', views.logout_view, name='logout'),
]