from django.contrib import admin
from .models import Course, Review


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "platform", "average_rating")
    search_fields = ("title", "platform")
    fields = ("title", "platform", "description")


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("course", "rating")
    search_fields = ("course__title", "text")
