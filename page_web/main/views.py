"""
importamos la librerias que necesitamos al igual las de django 
"""
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import (
		Review,
		Blog,
	)

from django.views import generic
from . forms import BlogForm, ContactForm, CreateUserForm, ReviewForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect

""""
aqui tenemos las funciones views 
"""

"""
Aqui esta la funcion de vista para la creacion de usuarios nuevos 
"""
def registerPage(request):
	if request.user.is_authenticated:
		return redirect("main:home")
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'La cuenta fue creada por ' + user)

				return redirect('main:login')
			

		context = {'form':form}
		return render(request, 'main/register.html', context)

"""
Aqui esta la funcion para logearse en la pagina la cual tiene una secuencia
que si el usuarios es autentificado entra al html home, si no envia mensaje que 
indica que son incorrectos y sigue en el login
"""

def loginPage(request):
	if request.user.is_authenticated:
		return redirect("main:home")
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect("main:home")
			else:
				messages.info(request, 'Usuario o contraseña incorrecta')

		context = {}
		return render(request, 'main/login.html', context)

""""
funcion para deslogear el usuario
"""
def logoutUser(request):
	logout(request)
	return redirect('main:home')

"""
clase que obtiene la informacion de la base de datos y permite colocarla en el front end 
"""

class IndexView(generic.TemplateView):
	template_name = "main/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		blogs = Blog.objects.filter(is_active=True)
		review = Review.objects.filter(is_active=True)
		
		context["reviews"] = review
		context["blogs"] = blogs
		return context


"""
Vista de la creacion de contacto , colocamos los parametros
que nos permite que sea necesarios logearse para hacerlos,  si no lo esta debe logearse
luego tiene una funcion que guarda la informacion, envia un mensajes y guarda la informacion en el 
form 
"""
class ContactView( LoginRequiredMixin,generic.FormView):
	login_url = 'main:login'
	redirect_field_name = 'login'
	template_name = "main/contact.html"
	form_class = ContactForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Muchas gracias, estaremos en contacto :)')
		return super().form_valid(form)

"""
Vista de la creacion de nuevos Blogs por la comunidad, colocamos los parametros
que nos permite que sea necesarios logearse para hacerlos,  si no lo esta debe logearse
luego tiene una funcion que guarda la informacion, envia un mensajes y guarda la informacion en el 
form 
"""
class BlogAddInfo(LoginRequiredMixin,generic.FormView):
	login_url = 'main:login'
	redirect_field_name = 'login'
	template_name = "main/blogaddinfo.html"
	form_class = BlogForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Muchas gracias por aportar a la comunidad :)')
		return super().form_valid(form)

"""
Vista de la creacion de nuevas review por la comunidad, colocamos los parametros
que nos permite que sea necesarios logearse para hacerlos,  si no lo esta debe logearse
luego tiene una funcion que guarda la informacion, envia un mensajes y guarda la informacion en el 
form 
"""
class ReviewAddInfo( LoginRequiredMixin,generic.FormView):
	login_url = 'main:login'
	redirect_field_name = 'login'
	template_name = "main/reviewaddinfo.html"
	form_class = ReviewForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Muchas gracias por aportar a la comunidad :)')
		return super().form_valid(form)


"""
Vista de el blog utilizamos el model de blog 
y le colocamos el template que vamos a utilizar es decir el url que queremos
tiene la funcion que obtiene los datos y los filtras si son activos 
"""
class BlogView(generic.ListView):
	model = Blog
	template_name = "main/blog.html"
	paginate_by = 10
	
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)

"""
Vista de el blog utilizamos el model de blog 
y le colocamos el template que vamos a utilizar es decir el url que queremos
"""
class BlogDetailView(generic.DetailView):
	model = Blog
	template_name = "main/blog-detail.html"

"""
Vista de el blog utilizamos el model de Review 
y le colocamos el template que vamos a utilizar es decir el url que queremos
tiene la funcion que obtiene los datos y los filtras si son activos 
"""

class ReviewView(generic.ListView):
	model = Review
	template_name = "main/review.html"
	paginate_by = 10
	
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


"""
Vista de el blog utilizamos el model de Review  
y le colocamos el template que vamos a utilizar es decir el url que queremos
"""
class ReviewDetailView(generic.DetailView):
	model = Review
	template_name = "main/Review-detail.html"