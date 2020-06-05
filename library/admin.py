from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Book, User, Author, HistoryOfRenting
#
#
# class UserInList(admin.TabularInline):
#     model = User
#
class BookInLine(admin.TabularInline):
    model = Book
#
#
# class HistoryInLine(admin.TabularInline):
#     model = HistoryOfRenting
#
class AuthorAdmin(admin.ModelAdmin):
    model = Author

    inlines = [
        BookInLine,


    ]
#
admin.site.register(Author, AuthorAdmin)
# admin.site.register(Author)
# admin.site.register(Book)
admin.site.register(User)
admin.site.register(HistoryOfRenting)