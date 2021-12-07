from django.shortcuts import render
from .forms import LoginForm
from .models import User

# Create your views here.
def registration_page(request):
    # instantiate form object with data sent from user
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'hello.html', {'form': form})
def file_upload(request):
    return render(request, 'file_upload.html')
