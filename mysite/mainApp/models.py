from django.db import models

class BackCall(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    message = models.TextField(default=None)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone

class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class Comment(models.Model):
    name = models.CharField(max_length=50)
    message = models.TextField(max_length=100)
    published = models.BooleanField(default=False)
    datetime = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.comment

def user_directory_path(email, filename):
    return 'user_{0}/{1}'.format(email, filename)

class Order(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email