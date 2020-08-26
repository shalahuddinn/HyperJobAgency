from django.shortcuts import render
from django.views import View
from .models import Vacancy


# Create your views here.
class VacanciesView(View):
    def get(self, request, *args, **kwargs):
        obj = Vacancy.objects.all()
        context = {
            "objects": obj
        }
        return render(request, 'vacancy/vacancies.html', context)
