from django.contrib import admin
from blog.models import OrderInfo, UserInfo, CommondityInfo, Publisher ,Author, Book, Account
from django.contrib.admin.templatetags.admin_list import date_hierarchy
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')
    
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    #list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    fields = ('title', 'publisher', 'authors') #'publication_date'
    filter_vertical = ('authors',)
    raw_id_fields = ('publisher',)
    
admin.site.register(OrderInfo)
admin.site.register(UserInfo)
admin.site.register(CommondityInfo)
admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Account)

