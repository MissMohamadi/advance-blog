from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin

class UserManager(BaseUserManager):
    '''
    class for manager custom user model before create user
    '''
    def create_user(self,email,password,**extra_fields):
        '''
        this method for manage normal custom user before create user
        '''
        if not email:
            raise ValueError("email must be set")
        email = self.normalize_email(email)
        user= self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

    def create_superuser(self,email,password,**extra_fields):
        '''
                this method for manage superuser custom user before create user
        '''
        extra_fields.setdefault('is_active' , True)
        extra_fields.setdefault('is_superuser' , True)
        extra_fields.setdefault('is_staff' , True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(" superuser must be have is_staff True ")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(" superuser must be have is_superuser True ")
        return self.create_user(email,password,**extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=250,unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # is_verified = models.BooleanField(default=False)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

class Profile(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email


