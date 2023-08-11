from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
def login_view(request):
  if request.method == "POST":
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      user = form.get_user()
      login(request,user)
      return redirect("/")
  else:
    form = AuthenticationForm(request)
    content = {
      "form":form
    }
    return render(request, "accounts/login.html", context=content)
  
def logout_view(request):
  if request.method == "POST":
    logout(request)
    return redirect("/login")
  return render(request, "accounts/logout.html", {})

def register_view(request):
  form = UserCreationForm(request.POST or None)
  if form.is_valid():
    user_obj= form.save()
    return redirect("/login")
  content = {
    "form": form
  }
  return render(request, "accounts/register.html", content)