from django.shortcuts import render
from . import models, forms
from bands.models import Band
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from users import mixins as user_mixins
from django.views.generic import ListView, DetailView, UpdateView, FormView


class SchoolListView(ListView):
    """school 관련된 전체 게시글 list를 볼 수 있음 """
    pass

class UploadView(FormView):
    """ 일반적인 post들 전부 upload 할 수 있음 """
    pass

class EditPostView(FormView):
    """ post edit 가능함 """
    pass
