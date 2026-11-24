from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('crop-guidance/', views.crop_guidance_view, name='crop_guidance'),
    path('weather/', views.weather_dashboard, name='weather'),
    path('market-prices/', views.market_prices_view, name='market_prices'),
    path('schemes/', views.government_schemes_view, name='schemes'),
    path('articles/', views.articles, name='articles'),
    path('articles/<str:article_id>/', views.article_detail, name='article_detail'),
]