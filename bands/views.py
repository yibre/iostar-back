from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models

class HomeView(ListView):

    """ HomeView Definition """

    model = models.Band
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    template_name = "home.html"


class BandDetail(DetailView):

    """ RoomDetail Definition """

    model = models.Band

class SchoolBandDetail(DetailView):
    """  """
    model = models.Band