# -*- coding: utf-8 -*-
from django.contrib import admin
from library.models import Book, Borrowing, Author


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'copies', 'author', 'owner')

admin.site.register(Book, BookAdmin)


class BorrowingAdmin(admin.ModelAdmin):
    list_display = ('book', 'borrowing_to', 'borrowing_date', 'return_date')

admin.site.register(Borrowing, BorrowingAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')

admin.site.register(Author, AuthorAdmin)