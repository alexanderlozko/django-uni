from django.db import models

class BackCall(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    message = models.TextField(default=None)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone

class Comment(models.Model):
    author = models.CharField(max_length=50)
    comment = models.TextField(max_length=50)
    published = models.BooleanField(default=False)
    datetime = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.comment

class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

def user_directory_path(email, filename):
    return 'user_{0}/{1}'.format(email, filename)

class Order(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email