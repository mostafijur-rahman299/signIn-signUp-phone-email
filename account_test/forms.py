from django import forms 

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField

User = get_user_model()


class UserAdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirm', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('full_name', 'email')
        
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('passwrod2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password don't match!")
        return password2
    
    def save(self, commit=True):
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user  
    
    
    
    
    
class UserAdminChangeform(forms.ModelForm):
    
    password = ReadOnlyPasswordHashField()
    
    class Meta:
        model = User  
        fields = ('email', 'full_name', 'password', 'is_active', 'admin')
        
        
    def clean_password(self):
        return self.initial['password']

class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
                                            attrs={
                                                    'id':'register-password', 
                                                    'placeholder': 'Password'
                                            }),help_text="i. Passwords must be at least 5 characters.<br>i. Passwords must be at least 1 number.<br>i. Passwords length must be at least 6 or more")
    
    password2 = forms.CharField(label='Re-enter password', widget=forms.PasswordInput(
                                            attrs={
                                                 'id': 'register-password2',
                                                'placeholder': 'Password Confirm'
                                            }))
    
    class Meta:
        model = User
        fields = ( 'email','full_name')
        widgets = {
            'email': forms.TextInput(attrs={'id': 'register-email', 'placeholder':'Email or Phone'}),
            'full_name': forms.TextInput(attrs={'id': 'register-fullname', 'placeholder': 'Full Name'})
        }
        
        
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        print(password1,password2)
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) <= 5:
            raise forms.ValidationError('Password length must be at least 6 charecter!')
        return password1

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = False
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={
                                                'placeholder': 'Email Address or phone',
                                                'id': 'login-email'
                                            }
                                        ),label="Email/Phone"
                                    )
    password = forms.CharField(widget=forms.PasswordInput(
                                            attrs={
                                                'placeholder': 'Password',
                                                'id': 'login-password'
                                            }
                                        )   
                                    )  










