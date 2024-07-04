from django.urls import path

from a_users import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('<username>/', views.profile, name='userprofile'),
    path('profile/edit/', views.profile_edit, name='profile-edit'),
    path('profile/onboarding/', views.profile_edit, name='profile-onboarding'),
    path('profile/delete/', views.profile_delete, name='profile-delete'),
    path('profile/verify-email/', views.profile_verify_email, name='profile-verify-email'),


]
