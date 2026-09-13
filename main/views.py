from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from main.models import Experience
from main.models import Skills


def show_main(request):
    context = {
        "name": "Syakira",
        "npm": "2506610595",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "A highly motivated CS student with a strong passion for technology and information system. "
            "I look forward to building a strong foundation while developing practical skills."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Syakira",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_skills(request):
    hard_skills = Skills.objects.filter(type='hard')
    soft_skills = Skills.objects.filter(type='soft')

    context = {
        "name": "Syakira",
        "hard_skills": hard_skills,
        "soft_skills": soft_skills
    }

    return render(request, "skills.html", context)