from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, 
    **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)



class User(AbstractUser):
    """ custom user model """
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )
    
    SCHOOL_DGIST = "dgist"
    SCHOOL_KAIST = "kaist"
    SCHOOL_UNIST = "unist"
    SCHOOL_GIST = "gist"
    SCHOOL_POSTECH = "postech"
    SCHOOL_OTHERS = "others"

    SCHOOL_CHOICES = (
        (SCHOOL_DGIST, "DGIST"),
        (SCHOOL_KAIST, "KAIST"),
        (SCHOOL_UNIST, "UNIST"),
        (SCHOOL_GIST, "GIST"),
        (SCHOOL_POSTECH, "POSTECH"),
        (SCHOOL_OTHERS, "OTHER")
    )

    STATUS_CHOICES = (
        ("bachelor", "학부과정"),
        ("master", "석사과정"),
        ("phD", "박사과정"),
        ("researcher", "연구원"),
        ("professor", "교수"),
        ("employee", "직원"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"
    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, "English"), (LANGUAGE_KOREAN, "Korean"))

    username = None
    email = models.EmailField(_('email address'), unique=True)
    schoolEmail = models.EmailField(_('email address 2nd'), unique=True, null=True)
    # second email: this is for second verified email if school email is expired.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    first_name=models.CharField(null=True, blank=True, max_length=30)
    last_name=models.CharField(null=True, blank=True, max_length=30)
    full_name=models.CharField(null=True, blank=True, max_length=30)
    # full name is for korean users
    nickname = models.CharField(max_length=15, null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )
    school = models.CharField(
        choices=SCHOOL_CHOICES, max_length=10, null=True, blank=True
    )
    stutus = models.CharField(
        choices=STATUS_CHOICES, max_length=15, null=True, blank=True
    )
    student_id = models.IntegerField(null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, null=True, blank=True
    )

    
    def __str__(self):
        return self.email
