from django import forms
from django.core.exceptions import ValidationError

from .models import Category, Alexnor


class AddPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Категория не выбрана", label="Категории")

    class Meta:
        model = Alexnor
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }
        labels = {'slug': 'URL'}

        def clean_title(self):
            title = self.cleaned_data['title']
            if len(title) > 50:
                raise ValidationError('Длина заголовка превышает 50 символов')

            return title


class UploadFileForm(forms.Form):
    file = forms.ImageField(label="Файл")
