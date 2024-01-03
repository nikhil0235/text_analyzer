# analyzer/urls.py

from django.urls import path
from .views import analyze_text, CustomLoginView, signup, CustomLogoutView

urlpatterns = [
    path('analyze/', analyze_text, name='analyze_text'),
    path('signup/', signup, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(next_page='analyze_text'), name='logout'),  # Specify the redirect URL

]
