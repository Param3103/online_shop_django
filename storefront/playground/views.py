from django.shortcuts import render
from .forms import LoginForm
from .models import user
from django.core.files.storage import FileSystemStorage

# Create your views here.
def registration_page(request):
    # instantiate form object with data sent from user
    form = LoginForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form = form.save()
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']  # no errors
            instance = user(name=name, age=age)
            instance.save()
    return render(request, 'hello.html', {'form': form})
def file_upload(request):
    if request.method == 'POST' and request.FILES['my_file']:
        myfile = request.FILES['my_file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'file_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'file_upload.html')