from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_posts, name='get_posts'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('add/', views.create_or_edit_post, name='add_post'),
    path('edit/<int:pk>/', views.create_or_edit_post, name='edit_post'),
    path('delete/<int:pk>/', views.delete_post, name='delete_post'),
    path('delete-comment/<int:comment_id>/', views.delete_comment,
         name='delete_comment'),
]
