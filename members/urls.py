from django.urls import path, include
from members.views import UserRegisterView, UserEditView, PasswordChangeView, password_success, choose_profile, \
    CreateUserProfileView, CreateConsultantProfileView, ShowUserProfileView, ShowConsultantProfileView, \
    UpdateUserProfileView, UpdateConsultantProfileView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_settings/', UserEditView.as_view(), name='edit_settings'),
    path('password/', PasswordChangeView.as_view()),
    path('password/success/', password_success, name='password_success'),
    path('choose_profile/', choose_profile, name='choose_profile'),
    path('create_user_profile/', CreateUserProfileView.as_view(), name='create_user_profile'),
    path('create_consultant_profile/', CreateConsultantProfileView.as_view(), name='create_consultant_profile'),
    path('user_profile/<int:pk>/', ShowUserProfileView.as_view(), name='show_user_profile'),
    path('consultant_profile/<int:pk>/', ShowConsultantProfileView.as_view(), name='show_consultant_profile'),
    path('update_user_profile/<int:pk>/', UpdateUserProfileView.as_view(), name='update_user_profile'),
    path('update_consultant_profile/<int:pk>/', UpdateConsultantProfileView.as_view(), name='update_consultant_profile'),
]