from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Course, Author
from .forms import ReviewForm, CourseForm


def course_list(request):
    courses = Course.objects.all()
    paginator = Paginator(courses, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request, "courses/list.html", {"courses": courses, "page_obj": page_obj}
    )


def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.course = course
            review.save()
            messages.success(request, "Отзыв опубликован.")
            return redirect("course_detail", course_id=course.id)
    else:
        form = ReviewForm()

    reviews = course.reviews.all().order_by("-id")

    paginator = Paginator(reviews, 6)  # 6 отзывов на страницу
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "courses/detail.html",
        {"course": course, "reviews": reviews, "form": form, "page_obj": page_obj},
    )


def recommended_courses(request):
    recommended = Course.objects.annotate(avg_rating=Avg("reviews__rating")).filter(
        avg_rating__gt=4.5
    )
    return render(request, "courses/recommended.html", {"courses": recommended})


@login_required
def add_course(request):
    # убедимся что пользователь — автор
    try:
        author = request.user.author_profile
    except Author.DoesNotExist:
        messages.error(
            request, "Только зарегистрированные авторы могут добавлять курсы."
        )
        return redirect("login")

    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.author = author
            course.save()
            messages.success(request, "Курс успешно добавлен.")
            return redirect("course_detail", course_id=course.id)
    else:
        form = CourseForm()
    return render(request, "courses/add_course.html", {"form": form})


def author_profile(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    courses = author.courses.all()
    paginator = Paginator(courses, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "courses/author_profile.html",
        {"author": author, "courses": courses, "page_obj": page_obj},
    )
