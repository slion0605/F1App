from django.urls import path
from f1StatsApp import views
app_name = 'f1statsapp'
urlpatterns = [
path('', views.lap_times, name='lap_times'),
path('hamilton/', views.hamilton_monaco_race, name='hamilton_data'),

]
