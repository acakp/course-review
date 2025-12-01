import re
from django import forms
from .models import Review
from django.contrib.auth.models import User

# from django.contrib.auth.forms import AuthenticationForm
from .models import Author, Course


class ReviewForm(forms.ModelForm):
    RATING_CHOICES = [
        (5, "5 — Отлично"),
        (4, "4 — Хорошо"),
        (3, "3 — Нормально"),
        (2, "2 — Плохо"),
        (1, "1 — Очень плохо"),
    ]

    rating = forms.TypedChoiceField(
        choices=RATING_CHOICES,
        coerce=int,
        empty_value=None,
        label="Оценка",
    )

    class Meta:
        model = Review
        fields = ["author", "rating", "text"]
        labels = {
            "author": "Ваше имя",
            "text": "Текст отзыва",
        }
        widgets = {
            "author": forms.TextInput(attrs={"placeholder": "Иван"}),
            "text": forms.Textarea(
                attrs={"rows": 4, "placeholder": "Поделитесь впечатлениями..."}
            ),
        }

    def clean_rating(self):
        rating = self.cleaned_data.get("rating")
        if rating is None or rating < 1 or rating > 5:
            raise forms.ValidationError("Оценка должна быть от 1 до 5.")
        return rating


class AuthorRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    password_confirm = forms.CharField(
        widget=forms.PasswordInput, required=True, label="Confirm password"
    )
    email = forms.EmailField(required=False)

    class Meta:
        model = Author
        fields = ["display_name", "bio"]

    def clean(self):
        cleaned = super().clean()
        # проверка имени пользователя
        u = cleaned.get("username")
        if u and not re.match(r"^[A-Za-z0-9]+$", u):
            raise forms.ValidationError(
                "имя пользователя может содержать только латинские буквы и цифры."
            )
        if u and User.objects.filter(u=u).exists():
            raise forms.ValidationError("пользователь с таким именем уже существует.")
        # проверка паролей
        p = cleaned.get("password")
        pc = cleaned.get("password_confirm")
        if p and pc and p != pc:
            raise forms.ValidationError("пароли не совпадают")
        return cleaned

    def save(self, commit=True):
        cleaned = self.cleaned_data
        username = cleaned["username"]
        password = cleaned["password"]
        email = cleaned.get("email") or ""
        user = User.objects.create_user(
            username=username, password=password, email=email
        )
        author = super().save(commit=False)
        author.user = user
        if commit:
            author.save()
        return author


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["title", "description"]
