from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import CustomUser
from .models import Author, Book
from django.core.exceptions import ValidationError


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'birth_date']

    def __init__(self, *args, **kwargs):
        super(AuthorForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите имя'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите фамилию'})
        self.fields['birth_date'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите дату рождения'})

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if Author.objects.filter(first_name=first_name, last_name=last_name).exists():
            raise ValidationError('Автор с таким именем и фамилией уже существует.')

        return cleaned_data


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'publication_date', 'author']

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите название книги'})
        self.fields['publication_date'].widget.attrs.update({
            'class': 'form-control', 'placeholder': 'Введите дату публикации'
        })
        self.fields['author'].widget.attrs.update({'class': 'form-control'})


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=False,
                                   help_text='Необязательное поле. Введите ваш номер телефона.')
    username = forms.CharField(max_length=50, required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'phone_number', 'password1', 'password2')

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError('Номер телефона должен состоять только из цифр!')
        return phone_number

