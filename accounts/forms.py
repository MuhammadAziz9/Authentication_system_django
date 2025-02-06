from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser
# Register your models here.

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username','email','age']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username','email','age']