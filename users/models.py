import uuid
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.shortcuts import reverse
from django.template.loader import render_to_string
# 아바타를 가져오기 위한 코드
from urllib.request import urlopen
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.contrib.staticfiles.templatetags.staticfiles import static
# -*- coding: utf-8 -*-
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM



class CustomUserManager(BaseUserManager):

    # Custom user model manager where email is the unique identifiers
    # for authentication instead of usernames.

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
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
    # email = models.EmailField(_('email address'), unique=True)
    email = models.EmailField(_('email adress'), unique=True, null=True)
    email_2nd = models.EmailField(_('email address for second'), null=True, blank=True)
    # second email: this is for second verified email if school email is expired.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    first_name=models.CharField(null=True, blank=True, max_length=30)
    last_name=models.CharField(null=True, blank=True, max_length=30)
    full_name=models.CharField(null=True, blank=True, max_length=30)
    # full name is for korean users, 우선은 생략하자, 한국인도 성이랑 이름 따로 쓸 수 있으니까
    nickname = models.CharField(max_length=15, null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True, upload_to = "user_profiles/")
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )
    school = models.CharField(
        max_length=10, null=True, blank=True
    )
    stutus = models.CharField(
        choices=STATUS_CHOICES, max_length=15, null=True, blank=True
    )
    student_id = models.IntegerField(null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, null=True, blank=True
    )
    email_verified = models.BooleanField(default=False)
    email_2nd_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default="", blank=True)
    objects = CustomUserManager()

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})

    def get_profile(self):
        if self.avatar:
            return self.avatar.url
        else: 
            return static('images/anonymous-person-icon-18.jpeg')

    def __str__(self):
        return self.email

    def make_avatar(self):
        # api 를 이용해 랜덤 아바타 만들기, 현 미완성
        #h ttps://stackoverflow.com/questions/64263748/how-download-image-from-url-to-django
        # 해당 코드를 보고 발견함
        api = "https://avatars.dicebear.com/api/identicon/"
        api_ask = api+self.email_secret+".svg"
        # svg 코드를 다운받게 됨
        img_tmp = NamedTemporaryFile(delete=True)
        with urlopen(api_ask) as uo:
           assert uo.status == 200
           img_tmp.write(uo.read())
           img_tmp.flush()
        img = File(img_tmp)
        #svg 파일을 png 파일로 수정하기
        # svg2png(bytestring=svg_code, write_to='output.png')
        self.avatar.save(str(self.pk)+".svg", img) # 여기서는 svg 파일로 save하게 됨

        

    def is_verified(self):
        return self.email_verified

    def verify_email(self):
        if self.email_verified is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            self.make_avatar()
            html_message = render_to_string(
                "emails/verify_email.html", {"secret": secret}
            )
            send_mail(
                "IOSTAR 이메일 인증",
                strip_tags(html_message),
                settings.EMAIL_FROM,
                [self.email],
                fail_silently=False,
                html_message=html_message,
            )
            self.save()
        return