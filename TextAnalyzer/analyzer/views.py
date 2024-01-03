# analyzer/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
from .models import File
from .forms import UploadFileForm
from collections import Counter
import re
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm

# analyzer/views.py

from django.contrib.auth.views import LogoutView
from django.shortcuts import render

class CustomLogoutView(LogoutView):
    template_name = 'registration/logged_out.html'  # Customize the template if needed

@login_required(login_url='login')
def analyze_text(request):
    result = {}

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            content = uploaded_file.read().decode('utf-8')

            # Use regex to extract words from the document
            words = re.findall(r'\b\w+\b', content.lower())

            # Count the occurrences of each word
            word_count = Counter(words)

            # Convert result to a readable format
            result = dict(word_count)

    else:
        form = UploadFileForm()

    return render(request, 'analyzer/analyze.html', {'form': form, 'result': result})


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    def get_success_url(self):
        return '/analyzer/analyze/'

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('analyze_text')  # Redirect to a different page after signup
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

