from django.contrib import admin
from django.urls import path
from accounts.views import google_login, home, create, logouts, store, painel, dologin, dashboard, changepass, changePassword, depositar
app_name='accounts'

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site
    path('', painel, name='painel'),  # Home page
    path('create/', create, name='create'),  # Create account
    path('store/', store, name='store'),  # Store data
    path('dologin/', dologin, name='dologin'),  # Login
    path('dashboard/', dashboard, name='dashboard'),  # User dashboard
    path('logouts/', logouts, name='logouts'),  # Logout
    path('changepass/', changepass, name='changepass'),  # Change password for user
    path('changepassword/', changePassword, name='changepassword'),  # Change password
    path('depositar/', depositar, name='depositar'),  # Deposit money
    path('login/google/', google_login, name='google_login'),
]