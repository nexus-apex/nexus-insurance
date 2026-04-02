from django.urls import path
from . import views

urlpatterns = [
    path('', lambda r: views.redirect('/dashboard/')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('policies/', views.policy_list, name='policy_list'),
    path('policies/create/', views.policy_create, name='policy_create'),
    path('policies/<int:pk>/edit/', views.policy_edit, name='policy_edit'),
    path('policies/<int:pk>/delete/', views.policy_delete, name='policy_delete'),
    path('claims/', views.claim_list, name='claim_list'),
    path('claims/create/', views.claim_create, name='claim_create'),
    path('claims/<int:pk>/edit/', views.claim_edit, name='claim_edit'),
    path('claims/<int:pk>/delete/', views.claim_delete, name='claim_delete'),
    path('insurecustomers/', views.insurecustomer_list, name='insurecustomer_list'),
    path('insurecustomers/create/', views.insurecustomer_create, name='insurecustomer_create'),
    path('insurecustomers/<int:pk>/edit/', views.insurecustomer_edit, name='insurecustomer_edit'),
    path('insurecustomers/<int:pk>/delete/', views.insurecustomer_delete, name='insurecustomer_delete'),
    path('settings/', views.settings_view, name='settings'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
