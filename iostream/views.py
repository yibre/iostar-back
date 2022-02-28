from django.shortcuts import render, redirect, reverse
from . import models, forms
from django.views.generic import ListView, FormView
from django.views.generic.edit import ModelFormMixin, FormMixin

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404


class FormListView(FormMixin, ListView):
    form_class = forms.UploadIostreamForm
    queryset = models.Iostream.objects.latest('created')
    template_name = "iostream/main.html"
    context_object_name = "iostream"

    def form_valid(self, form):
        print("hello 5")
        iostream = form.save()
        iostream.author = self.request.user
        print("come form form valid in form list view : ", self.request.user)
        iostream.save()
        form.save_m2m()
        messages.success(self.request, "Advertisement Uploads")
        return redirect("iostream:main")
    

    def post(self, request, *args, **kwargs):
        print("hello there")
        form = self.get_form()
        if form.is_valid():
            form.save()
        return super().post(request, *args, **kwargs)


def add_data(request):
    print("hello there2")
    if request.method == "POST":
        print("hello there3")
        form = forms.UploadIostreamForm(request.POST)

        if form.is_valid():
            print("hello there4")
            form.save()
            # models.Iostream.objects.create(address=form.cleaned_data['form'])
            return redirect(reverse('iostream:main'))


class ListWithForm(ListView, ModelFormMixin):
    # model = models.Iostream
    form_class = forms.UploadIostreamForm
    queryset = models.Iostream.objects.all().order_by("created")
    template_name = "iostream/main.html"
    context_object_name = "iostream"

    def get(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)
        return ListView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)

        if self.form.is_valid():
            self.object = self.form.save()

        return self.get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(ListWithForm, self).get_context_data()


class IostreamListView(ListView):
    # iostream main view
    context_object_name = "iostream"
    queryset = models.Iostream.objects.all().order_by('-created')
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
현재 코드 이 시점인데 이걸로 부족한듯

https://forum.djangoproject.com/t/understanding-how-to-combine-formview-and-listview/1879
이거 해보기 -> 두개를 함께 묶는 방법

https://stackoverflow.com/questions/63828671/django-listview-with-form-how-to-redirect-back-to-the-form-page
이것도 해보는 중

현재 여기를 하나의 페이지에 통합하기 위해 노력하고 있다.

"""

class UploadIostreamView(FormView):
    form_class = forms.UploadIostreamForm
    template_name = "iostream/upload_iostream.html"

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save()
        return super().post(request, *args, **kwargs)


    def form_valid(self, form):
        iostream = form.save()
        iostream.author = self.request.user
        iostream.save()
        form.save_m2m()
        messages.success(self.request, "Advertisement Uploads")
        return redirect("iostream:main")

