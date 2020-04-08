from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import DayCreateForm
from .models import Day

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'diary/day_list.html'
    model = Day

class AddView(generic.CreateView):
    template_name = 'diary/day_form.html'
    model = Day
    form_class = DayCreateForm
    success_url = reverse_lazy('diary:index')