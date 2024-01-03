# TextAnalyzer/urls.py

from django.contrib import admin
from django.urls import path, include
from analyzer.views import CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('analyzer/', include('analyzer.urls')),
    path('login/', CustomLoginView.as_view(), name='login'),
    
]
