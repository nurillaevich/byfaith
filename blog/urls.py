from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('sermons/', sermons, name='sermons'),
    path('ministries/', ministries, name='ministries'),
    path('events/', events, name='events'),
    path('detail/<int:pk>/', detail_page, name='detail'),

]
