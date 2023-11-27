from . import views
from django.urls import path

urlpatterns = [      
    path('', views.authors, name='Authors'),  
        path('author_status_/<int:author_id>/', views.change_status_author, name='author_status'),                      
]