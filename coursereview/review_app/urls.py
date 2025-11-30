from django.urls import path
from .views import (
    course_list,
    course_detail,
    recommended_courses,
    login_view,
    register_author,
    logout_view,
    add_course,
    author_profile,
)

urlpatterns = [
    path("", course_list, name="course_list"),
    path("course/<int:course_id>/", course_detail, name="course_detail"),
    path("recommended/", recommended_courses, name="recommended_courses"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_author, name="register"),
    path("add-course/", add_course, name="add_course"),
    path("author/<int:author_id>/", author_profile, name="author_profile"),
]
