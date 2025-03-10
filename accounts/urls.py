from django.urls import path
from .import views

urlpatterns = [
    path('login/', views.login_page, name="login"),
    path('register/', views.register_staff, name="register"),
    path('logout/', views.logout_user, name="logout"),
    
    path('', views.redirect_to_login, name="root"),  # Redirect root URL to login page
    path('dashboard/', views.home, name="home"),  # Move dashboard to its own URL
    path('products/', views.products, name="products"),
    path('customer/<str:pk_test>/', views.customer, name="customer"),
    
    path('create_customer/', views.createCustomer, name="create_customer"),
    
    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"), #str to make it dynamic and pk=primary key
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"), #str to make it dynamic and pk=primary key

]
