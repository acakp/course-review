from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User


# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="author_profile"
    )
    display_name = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.display_name or self.user.username


class Course(models.Model):
    title = models.CharField(max_length=200)  # название курса
    description = models.TextField(blank=True)
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, blank=True, related_name="courses"
    )

    @property
    def average_rating(self):
        return self.reviews.aggregate(Avg("rating"))["rating__avg"] or 0.0

    def __str__(self):
        return self.title


class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="reviews")
    author = models.TextField()
    rating = models.IntegerField()
    text = models.TextField()

    def __str__(self):
        return f"Review for {self.course.title} - Rating: {self.rating}"
