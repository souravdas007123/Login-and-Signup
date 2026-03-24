from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request, 'authent/login.html')

def signup_view(request):
    return render(request, 'authent/signup.html')