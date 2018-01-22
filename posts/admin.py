from django.contrib import admin
from .models import Post 
# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title","updated","timestamp"]
	list_display_links = ["updated"]   #display as link
	list_editable = ["title"]  #items that you can actually edit
	list_filter = ["updated","timestamp"]  #showing filter panel
	search_fields = ["title","content"]
	class Meta:
		model = Post


admin.site.register(Post,PostModelAdmin)