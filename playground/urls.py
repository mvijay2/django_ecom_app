from django.urls import path
from . import views

#url configuration
#hello.html nothing but home page
urlpatterns = [
    path('', views.say_hello, name= 'hello'), #name variable is usefull/mandatory when we give it as ref in html files.
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name= 'login'),
    path('logout/', views.logout_user, name= 'logout'),
    path('register/', views.register_user, name='register'),
    path('product/<int:pk>', views.product, name='product'),
    path('category/<str:foo>', views.category, name= 'category'),


]