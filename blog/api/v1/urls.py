from django.urls import path,include
from . import views


urlpatterns = [
    path('post/', views.postList, name='post-list'),
    path('post/<int:id>/', views.postDetail, name='post-detail'),
]
