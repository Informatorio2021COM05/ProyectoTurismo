from django.contrib import admin
from blog.models import *
# Register your models here.

class PostAdmin(admin.ModelAdmin):
	readonly_fields=('created', 'updated')

admin.site.register(Categoria)

admin.site.register(Post, PostAdmin) 