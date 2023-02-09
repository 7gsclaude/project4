from django.urls import path
from . import views 

# Add the include function to the import


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path("posts/", views.post_index, name="post_index"),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('posts/create/', views.PostCreate.as_view(), name='post_create'),

    
    
    path('accounts/signup/', views.signup, name='signup'),

]