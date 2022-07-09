from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app_account.models import Profile, Softrequest
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from app_book.models import Book, Category, Files
from .fields import GroupedModelChoiceField


GEEKS_CHOICES = (
    ("1", "One"),
    ("2", "Two"),
    ("3", "Three"),
    ("4", "Four"),
    ("5", "Five"),
)


def student_id_validation(value):
    if not value.isdigit():
        raise ValidationError('شماره دانشجویی باید یک عدد باشد.')


def student_id_validation_len(value):
    if not (8 <= len(value) <= 10):
        raise ValidationError('طول شماره دانشجویی نباید کوچکتر لز 8 و بزرگتر از 10 باشد.ُ')


def name_validation(value):
    if value.isdigit():
        raise ValidationError('نامو نام خانوادگی نمیتواند عدد باشد.')


def softname_validation(value):
    if value.isdigit():
        raise ValidationError('اسم نرم افزار نمیتواند فقط عدد باشد.')

class SignUpForm(UserCreationForm):

    email = forms.EmailField(max_length=254, label="ایمیل")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
        labels = {
            'username': 'نام کاربری',

        }


class ProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    first_name = forms.CharField(label='نام', max_length=50, validators=[name_validation])
    last_name = forms.CharField(label='نام خانوادگی', max_length=50, validators=[name_validation])
    username = forms.CharField(label='نام کاربری', max_length=50)
    student_id = forms.CharField(label='شماره دانشجویی', max_length=50, validators=[
                                 student_id_validation, student_id_validation_len])
    email = forms.EmailField(max_length=254, label="ایمیل")
    avatar = forms.ImageField(required=False, label="اواتار")

    def save(self, *args, **kwargs):
        profile = Profile.objects.get(user=self.user)
        profile.student_id = self.cleaned_data.get('student_id')
        profile.avatar = self.cleaned_data.get('avatar')
        profile.user.first_name = self.cleaned_data.get('first_name')
        profile.user.last_name = self.cleaned_data.get('last_name')
        profile.user.username = self.cleaned_data.get('username')
        profile.user.email = self.cleaned_data.get('email')
        profile.email = self.cleaned_data.get('email')
        profile.save()
        profile.user.save()

    class Meta:
        model = Profile
        exclude = ('user',)
        fields = ('username', 'email', 'student_id', 'first_name', 'last_name', 'avatar')


class Softrequestform(forms.ModelForm):
    softname = forms.CharField(label='نام نرم افزار و یا برنامه مبایل', required=True,
                               max_length=100, validators=[softname_validation])
    description = forms.CharField(label='توضیحات', widget=forms.Textarea, required=True)

    class Meta:
        model = Softrequest
        fields = ('softname', 'description')


class Booksendform(forms.ModelForm):
    title = forms.CharField(max_length=100, label='نام کتاب یا جزوه')
    author = forms.CharField(max_length=100, label='نویسنده')
    description = forms.CharField(max_length=600, label='خلاصه کتاب')
    category = GroupedModelChoiceField(
        queryset=Category.objects.exclude(parent=None),
        choices_groupby='parent',
        label='دسته بندی'
    )
    image = forms.ImageField(required=False, label="عکس کتاب")
    file = forms.FileField(required=False,
                           label="فایل کتاب")

    class Meta:
        model = Book
        fields = ('title', 'author', 'description', 'category', 'image', 'file')
