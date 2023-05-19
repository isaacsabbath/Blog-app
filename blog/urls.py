from . import views
from django.urls import path

urlpatterns = [
	path('', views.PostList.as_view(), name = 'home'), # returns a list of posts for our homepage
	path('<slug:slug>/', views.PostDetail.as_view(), name ='post_detail'), #django uses <> to capture values from the url and return the equivalent post deatil page.
]