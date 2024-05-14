from django.db import models


# Create your models here.

class HomePage(models.Model):
    title = models.CharField(max_length=212)
    des = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title


class Home(models.Model):
    title = models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField(upload_to='post')

    def __str__(self):
        return self.title


class Sermons(models.Model):
    title = models.CharField(max_length=212)
    image = models.ImageField(upload_to='post', null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=212)
    description = models.TextField()

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=212)
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='post')

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    title = models.CharField(max_length=212)
    description = models.TextField()
    author = models.ForeignKey(About, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=212)
    image = models.ImageField('post', null=True, blank=True)

    def __str__(self):
        return self.name


class OurS(models.Model):
    title = models.CharField(max_length=212)
    des = models.TextField()

    def __str__(self):
        return self.title


class Events(models.Model):
    title = models.CharField(max_length=212)
    des = models.TextField()
    image = models.ImageField()
    crt = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Ministries(models.Model):
    title = models.CharField(max_length=212)
    des = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title


class Blog(models.Model):
    text = models.TextField()
    image = models.ImageField()
