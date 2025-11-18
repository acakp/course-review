from django.db import models
from django.db.models import Avg


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200)  # название курса
    platform = models.CharField(max_length=100)  # платформа (компания)
    description = models.TextField(blank=True)

    # @property
    # def average_rating(self):
    #     return self.reviews.aggregate(Avg("rating"))["rating__avg"] or 0.0

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
