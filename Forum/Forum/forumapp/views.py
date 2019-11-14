from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .forms import RegisterForm
from .forms import ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.urls import reverse
from django.views.generic import ListView, DetailView

# Create your views here.
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, "profile.html", context)


def register(response):
	if response.method == "POST":
		form = RegisterForm(response.POST)
		if form.is_valid():
			form.save()
		return redirect("home_url")
	else:
		form = RegisterForm()
	return render(response, 'register.html', {"form": form})

def logoutUser(request):
	logout(request)
	return render(request, 'base.html')



def home_view(request):
	categories = Category.objects.all()
	context = {
		'categories': categories
		}
	return render(request, 'base.html', context)


def category_view(request, category_slug):
	category = Category.objects.get(slug=category_slug)
	posts_of_category = Post.objects.filter(category=category)
	
	context = {
		'category': category,
		'posts_of_category': posts_of_category,
		}
	return render(request, 'base.html', context)


def category(request, slug):
    categori = Category.objects.get(slug=slug)
    return render(request, 'category.html', {'categori': categori})








