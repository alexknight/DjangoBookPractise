from django.contrib import admin
from .models import Publisher,Author,Book
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
	list_display=('first_name','last_name','email')
	search_fields=('first_name','last_name')
	list_filter=('email',)

class BookAdmin(admin.ModelAdmin):
	list_display=('title','publisher','publication_date')
	list_filter=('publication_date',)
	date_hierarchy='publication_date'
	ordering=('-publication_date',)
	# fields=('publication_date','Publisher','title')
	filter_horizontal = ('authors',)

admin.site.register(Book,BookAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Publisher)