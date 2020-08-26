from django.shortcuts import render
from django.views import View
from .models import Resume


# Create your views here.
class ResumeView(View):
    def get(self, request, *args, **kwargs):
        obj = Resume.objects.all()
        print(obj)
        context = {
            "objects": obj
        }
        return render(request, 'resume/resumes.html', context)
