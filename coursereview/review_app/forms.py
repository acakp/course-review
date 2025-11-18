from django import forms
from .models import Review


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
