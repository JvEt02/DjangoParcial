"""
importamos la librerias que necesitamos al igual las de django 
"""
from django.urls import path
from . import views


"""
LLamamos la app como main
"""
app_name = "main"

"""
Aqui creamos los paths para los url que utilizaremos en la pagina web
estos permiten las subdiviciones en la pagina web y son necesarias 
estos url los vamos a utilizar en las vistas mas adelantes
"""

urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),
	path('logout/', views.logoutUser, name="logout"),

	path('', views.IndexView.as_view(), name="home"),
	path('contact/', views.ContactView.as_view(), name="contact"),

	path('blogaddinfo/', views.BlogAddInfo.as_view(), name="blogaddinfo"),
	path('reviewaddinfo/', views.ReviewAddInfo.as_view(), name="reviewaddinfo"),

	path('blog/', views.BlogView.as_view(), name="blogs"),
	path('blog/<slug:slug>', views.BlogDetailView.as_view(), name="blog"),
	path('review/', views.ReviewView.as_view(), name="reviews"),
	path('review/<slug:slug>', views.ReviewDetailView.as_view(), name="review"),
	]

    