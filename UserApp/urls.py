from django.urls import path
from UserApp import views 
 
urlpatterns = [ 
    path('user/', views.user_list),
    path('data/', views.data_list),
    path('user/<int:id>/', views.user_detail),
    path('upload/', views.uploadSound),
]