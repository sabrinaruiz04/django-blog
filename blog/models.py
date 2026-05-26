from django.db import models
from django.core.validators import MinLengthValidator

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=150, validators=[MinLengthValidator(5)])
    slug = models.SlugField(unique=True)
    excerpt = models.CharField(max_length=300)
    content = models.TextField(validators=[MinLengthValidator(10)])
    date = models.DateField()
    image = models.ImageField(upload_to="posts/", blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="posts")
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-date"]