from django.shortcuts import render
from .models import Post
from django.views import generic

class PostList(generic.ListView): 
	queryset = Post.objects.filter(Status=1).order_by('created_on') # a filter so that the post with status published be shown at the front end of our blog. Created_on signifies the latest posts will be at the top and so on.
	template_name = 'index.html'

class PostDetail(generic.ListView): # DetailView provides a detail view for a given object of the model
	model = Post
	template_name = 'post_detail.html'
