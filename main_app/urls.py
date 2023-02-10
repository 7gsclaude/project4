from django.urls import path
from . import views 

# Add the include function to the import


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path("posts/", views.post_index, name="post_index"),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('posts/create/', views.PostCreate.as_view(), name='post_create'),
    path('posts/<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),

    path('posts/<int:post_id>/assoc_comment/<int:comment_id>/',views.assoc_comment, name='assoc_comment'),

    
    
    path('comment/create/', views.CommentCreate.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', views.CommentUpdate.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', views.CommentDelete.as_view(), name='comment_delete'),
   
    
    
    path('accounts/signup/', views.signup, name='signup'),

]