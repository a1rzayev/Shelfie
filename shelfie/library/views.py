from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from .models import Book

def main_menu(request):
    books = Book.objects.all()
    return render(request, 'main_menu.html', {'books': books})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'user'
            user.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'library/register.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.role == 'admin')
def admin_dashboard(request):
    books = Book.objects.all()
    return render(request, 'library/admin_dashboard.html', {'books': books})

@login_required
@user_passes_test(lambda u: u.role == 'writer')
def writer_dashboard(request):
    books = Book.objects.filter(added_by=request.user)
    return render(request, 'library/writer_dashboard.html', {'books': books})

@login_required
def user_dashboard(request):
    books = Book.objects.all()
    return render(request, 'library/user_dashboard.html', {'books': books})
