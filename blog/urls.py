from django.urls import path
from django.views.generic.base import TemplateView,RedirectView
from . import views

urlpatterns = [
    path('cbv/', TemplateView.as_view(template_name='index.html', extra_context={'name':'Hoda'}), name='cbv'),
    path('cbv-index/', views.IndexView.as_view(), name='cbv-index'),
    path('go-to-maktabkhooneh/', RedirectView.as_view(pattern_name="cbv"), name='go-to-maktabkhooneh'),
    path('post/', views.PostListView.as_view(), name='post'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/create/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
]