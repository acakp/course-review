from django.urls import path, include
from .views import (
    course_list,
    course_detail,
    recommended_courses,
    add_course,
    author_profile,
)

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("", course_list, name="course_list"),
    path("course/<int:course_id>/", course_detail, name="course_detail"),
    path("recommended/", recommended_courses, name="recommended_courses"),
    path("add-course/", add_course, name="add_course"),
    path("author/<int:author_id>/", author_profile, name="author_profile"),
]
