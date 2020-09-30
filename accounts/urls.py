from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.registerPage,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('home',views.home,name='home'),
    path('busdevclerk',views.busclerk,name='busdevclerk'),
    path('consengineer',views.consengineer,name='engineer'),
    path('',views.indexPage,name='index'),
    path('user/',views.userPage,name='user'),
    path('profile/',views.userProfile,name='profile'),
    path('products/',views.products,name='products'),
    path('customerforclerk/<str:pk_test>/',views.customerforclerk,name='customerforclerk'),
    path('customer/<str:pk>/',views.customer,name='customer'),
    path('create_order/<str:pk>/',views.create_order,name='create_order'),
    path('create_ordertwo/<str:pk>/',views.create_ordertwo,name='create_ordertwo'),
    path('create_orderthree/<str:pk>/',views.create_orderthree,name='create_orderthree'),
    path('supply_agreement/<str:pk>/',views.supply_agreement,name='supply_agreement'),
    path('wayleave_agreement/<str:pk>/',views.wayleave_agreement,name='wayleave_agreement'),
    path('create_order/',views.create_order,name='create_order'),
    path('update_order/<str:pk>/',views.update_order,name='update_order'),
    path('delete/<str:pk>/',views.delete,name='delete'),
    
    #Customer Qoutations page 
    path('qoutations/<str:pk>/',views.qoutations,name='qoutations'),
    path('payment/<str:pk>/',views.payment,name='payment'),
    path('icms/<str:pk>/',views.icms,name='icms'),
    path('icmsclerk',views.icmsclerk,name='icmsclerk'),
    path('busdev/<str:pk>/',views.busdev,name='busdev'),
    path('proposal/<str:pk>/',views.proposal,name='proposal'),
    path('map/<str:pk>/',views.maplatlon,name='map'),
    
    #Analytics page
    path('analytics/',views.analytics,name='analytics'),
    
    #Application form
    path('create_app/<str:pk>/',views.create_app,name='create_app'),
]