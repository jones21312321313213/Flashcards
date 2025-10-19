from django.shortcuts import render

# Create your views here.

from .models import Folder

# Display all folders
def index(request):
    folders = Folder.objects.all()
    return render(request, 'folder/index.html', {'folders': folders})

# Login page for folder app (if needed)
def login_page(request):
    return render(request, 'folder/login.html')