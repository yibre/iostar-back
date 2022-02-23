from django.forms.models import modelformset_factory
from django.shortcuts import render
from . import models, forms
from bands.models import Band
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from users import mixins as user_mixins
from django.views.generic import ListView, DetailView, UpdateView, FormView

from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from .forms import ImageForm, PostForm

@login_required
def post(request):
    
    ImageFormSet = modelformset_factory(models.Images,
                                        form=ImageForm, extra=3)
    #'extra' means the number of photos that you can upload   ^
    if request.method == 'POST':
    
        postForm = PostForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=models.Images.objects.none())
    
    
        if postForm.is_valid() and formset.is_valid():
            print("form is valid 1")
            print(postForm)
            post_form = postForm.save(commit=False)
            post_form.user = request.user
            print("form is valid 2")
            post_form.save()
            print("form is valid 3")
    
            for form in formset.cleaned_data:
                #this helps to not crash if the user   
                #do not upload all the photos
                if form:
                    image = form['image']
                    photo = models.Images(post=post_form, image=image)
                    photo.save()
            # use django messages framework
            messages.success(request,
                             "Yeeew, check it out on the home page!")
            return HttpResponseRedirect("/")
        else:
            print(postForm.errors, formset.errors)
    else:
        postForm = PostForm()
        formset = ImageFormSet(queryset=models.Images.objects.none())
    return render(request, 'uploadexample.html',
                  {'postForm': postForm, 'formset': formset})



class SchoolListView(ListView):
    """school 관련된 전체 게시글 list를 볼 수 있음 """
    pass

class UploadView(FormView):
    """ 일반적인 post들 전부 upload 할 수 있음 """
    pass

class EditPostView(FormView):
    """ post edit 가능함 """
    pass



# 하나의 post에 여러 photo를 업로드하는 방법