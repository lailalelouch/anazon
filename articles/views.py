from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout

from .models import Book
from .forms import *


def home_page(request):
	name = "fay"
	context = {
		"y" : name,
		"y": "ghg",
		"age" : 55,
		"hobbies" : ["writing", "anythining"]
	}
	return render(request, 'home_page.html', context)


def about(request):
	context = {
		"y" : "tam",
		"age" : 77,
		"hobbies" : ["writing", "anythining", "boringing"]
	}
	return render(request, 'home_page.html', context)


def list_page(request):
	context = {
		"books" : Book.objects.all()
	}
	return render(request, 'list_page.html', context)


def detail_page(request, book_id):
	context = {
		"book" : Book.objects.get(id=book_id)

	}
	return render(request, "detail_page.html", context)


def create_book(request):
	if request.user.is_anonymous:
		return redirect("login")

	form = BookForm()
	if request.method == "POST":
		form = BookForm(request.POST, request.FILES)
		if form.is_valid():
			book = form.save(commit=False)
			book.sold_by = request.user
			book.save()
			return redirect("list-page")



	context = {
		"form" : form,

	}
	return render(request, 'create_book.html',context)


def update_book(request, book_id):
	book = Book.objects.get(id=book_id)

	if request.user.is_authenticated and request.user == book.sold_by:

		form = UpdateBookForm(instance=book)

		if request.method == "POST":
			form = UpdateBookForm(request.POST,instance=book)
			if form.is_valid():
				form.save()
				return redirect("list-page")


		context = {
			"form" : form,
			"id" : book_id
		}
		return render(request, 'update_book.html', context)
	else:
		return redirect("detail-page", book.id)


def delete_book(request, book_id):
	Book.objects.get(id=book_id).delete()
	return redirect("list-page")


def register_view(request):
	if request.user.is_authenticated:
		return redirect("list-page")

	form = RegistrationForm()

	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.set_password(user.password)
			user.save()
			return redirect("list-page")

	context = {
		"form" : form,

	}
	return render(request, 'register.html',context)


def login_view(request):
	if request.user.is_authenticated:
		return redirect("list-page")


	form = LoginForm()

	if request.method == "POST":
		form = LoginForm(request.POST)

		if form.is_valid():
			u = form.cleaned_data['username']
			p = form.cleaned_data['password']

			user = authenticate(username=u, password=p)
			if user is not None:
				login(request, user)
				return redirect("list-page")
			



	context = {
		"form" : form,
	}
	return render(request, 'login_view.html', context)


def logout_view(request):
	logout(request)
	return redirect("login")


def my_books(request):
	return render(request, "my_books.html")