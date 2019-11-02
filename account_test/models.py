from django.db import models


from django.conf import settings


from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)


from datetime import timedelta
from django.utils import timezone
from django.urls import reverse 



# send_mail(subject, message, from_email, recipient_list, html_message)



class UserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None, is_admin=False, is_staff=False, is_active=True):
        if not email:
            raise ValueError("User must have an email address")
        if not password:
            raise ValueError("User must have a password")
        
        user_obj = self.model(
            email = self.normalize_email(email),
            full_name = full_name,
        )
        
        user_obj.set_password(password)
        user_obj.staff = is_staff 
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj
    
    def create_staffuser(self, email, full_name, password):
        user = self.create_user(
            email,
            full_name,
            password=password,
            is_staff=True
        )
        
        return user
    
    def create_superuser(self, email, full_name, password):
        user = self.create_user(
            email,
            full_name,
            password=password,
            is_staff=True,
            is_admin=True
        )
        
        return user



class User(AbstractBaseUser):
    email           = models.CharField(max_length=255, unique=True, help_text="i. Keep an unique email.", verbose_name="Email/Phone")
    full_name       = models.CharField(max_length=250)
    # active          = models.BooleanField(default=True)
    is_active       = models.BooleanField(default=True)
    staff           = models.BooleanField(default=False)
    admin           = models.BooleanField(default=False)
    timestamp       = models.DateTimeField(auto_now_add=True)
     
    USERNAME_FIELD = "email" 
    
    # USERNAME_FIELD and password are by default REQUIRED_FIELDS
    REQUIRED_FIELDS = ['full_name'] # [full_name]
    
    objects = UserManager()
    
    def __str__(self): 
        return self.email 
    
    # def mobile_number(self):
    #     return self.mobile_number
    
    def get_full_name(self):
        if self.full_name:
            return self.full_name
        return self.email
    
    def get_short_name(self):
        return self.email  
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.staff  
    
    @property
    def is_admin(self):
        return self.admin 



