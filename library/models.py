from django.db import models

from django.urls import reverse  # Used to generate URLs by reversing the URL patterns

LOAN_STATUS = (
    ('a', 'Available'),
    ('r', 'Reserved'),
)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='a', help_text='Book availability')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)


    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)



class HistoryOfRenting(models.Model):
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    date_of_rent = models.DateTimeField(auto_now_add=True)
    date_of_return = models.DateTimeField(blank=True, null=True)

