from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.home, name='home' ),
    path('profile/', views.profile, name='profile' ),
    path('post/', views.post, name='post' ),
    path('post/<slug:url>',views.blog_page, name='blog_page'),
    path('about/', views.about, name='about' ),
    path('contact/', views.contact, name='contact')
]
