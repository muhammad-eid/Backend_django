from dataclasses import field
from pyexpat import model
from django import forms
from account.forms import UserCreationForm, UserChangeForm
from account.models import User


class SingupForm(UserCreationForm):
    class meta:
        model = User
        fields = ["email", "first_name", "last_name", "phone", "company_name", "password1", "password2",]

    # def __init__(self, *args, **kwargs) -> None:
        
    #     # for
    #     super(SingupForm, self).__init__(*args, **kwargs)
    #     self.fields['email'].widget.attrs['class']='block w-11/12 bg-green-500 rounded-lg text-white p-2 mx-auto font'


        
class ConfirmSignupForm(UserChangeForm):
    class meta:
        model = User
        fields = ["email", "first_name", "last_name", "phone", "company_name", "password1", "password2",]