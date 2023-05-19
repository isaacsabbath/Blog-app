from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'Status', 'created_on') #attribute, displayes the properties mwntioned in the tuple
	list_filter = ("Status",) #filter the post depending on their status and is done by list_filter() method.
	search_fields = ['title', 'content'] #brings the search bar on top the list, which wwill search the database from the search_field attributes
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)