from django.urls import path
from .views import course_list, course_detail, recommended_courses
# from .views import coursereview, course_list, course_detail, recommended_courses

urlpatterns = [
    # path("", coursereview),
    path("", course_list, name="course_list"),
    path("course/<int:course_id>/", course_detail, name="course_detail"),
    path("recommended/", recommended_courses, name="recommended_courses"),
]
