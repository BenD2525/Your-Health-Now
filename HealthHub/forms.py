# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from django.core.exceptions import ValidationError


# class RegistrationForm(UserCreationForm):
#     username = forms.CharField(label='Username', min_length=5,)
#     email = forms.EmailField(label='Email')
#     password1 = forms.CharField(label='Password')
#     password2 = forms.CharField(label='Confirm password')

#     def validate_user(self):
#         username = self.cleaned_data['Username'].lower()
#         check_user = User.objects.filter(username=username)
#         if check_user:
#             raise ValidationError("This username is already taken.")
#         return username

#     def validate_email(self):
#         email = self.cleaned_data['Email'].lower()
#         check_email = User.objects.filter(email=email)
#         if check_email:
#             raise ValidationError("This email is already registered.")
#         return email

#     def validate_password(self):
#         password1 = self.cleaned_data.get('password1')
#         password2 = self.cleaned_data.get('password2')

#         if password1 and password2:
#             if password1 != password2:
#                 raise ValidationError("Your passwords don't match.")
#         else:
#             raise ValidationError("Please enter a password in both boxes.")

#         return password2

#     def save_user(self):
#         user = User.objects.create_user(
#             self.cleaned_data['username'],
#             self.cleaned_data['email'],
#             self.cleaned_data['password2']
#         )
#         return user


# class LoginForm(forms.Form):
#     username = forms.CharField(label='Username')
#     password = forms.CharField(label='Password')

    # def validate_user(self):
    #     username = self.cleaned_data['Username'].lower()
    #     check_user = User.objects.filter(username=username)
    #     if not check_user:
    #         raise ValidationError("This username doesn't exist. Try again.")
    #     return username
    
    # def validate_password(self):
    #     password = self.cleaned_data.get['Password']
    #     check_password = User.objects.filter(password=password)
    #     if not check_password:
    #         raise ValidationError("Incorrect password, please try again.")
    #     return password
    
    # def save_user(self):
    #     user = User.objects.check()(
    #         self.cleaned_data['username'],
    #         self.cleaned_data['email'],
    #         self.cleaned_data['password2']
    #     )
    #     return user
