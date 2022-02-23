from django.shortcuts import render
from . import models, forms
from django.views.generic import ListView, FormView
from django.contrib import messages
from django.shortcuts import render, redirect

class IostreamListView(ListView):
    """ iostream main view """
    context_object_name = "iostream"
    queryset = models.Iostream.objects.all()
    template_name = "iostream/main.html"

    def get_context_data(self, **kwargs):
        context = super(IostreamListView, self).get_context_data(**kwargs)
        context['form'] = forms.UploadIostreamForm
        return context


"""
https://stackoverflow.com/questions/50275355/django-listview-with-a-form
현재 코드는 이 시점인데 이게 안 통함

https://stackoverflow.com/questions/18664182/is-it-possible-to-have-a-form-in-a-listview-template
이거 한 번 해보기 

현재 여기를 하나의 페이지에 통합하기 위해 노력하고 있다.

"""

class UploadIostreamView(FormView):
    form_class = forms.UploadIostreamForm
    template_name = "iostream/main.html"

    def form_valid(self, form):
        iostream = form.save()
        iostream.author = self.request.user
        iostream.save()
        form.save_m2m()
        messages.success(self.request, "Advertisement Uploads")
        return redirect("iostream:main")

