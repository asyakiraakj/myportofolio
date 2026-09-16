# Create your views here.
from django.shortcuts import render

from main.models import Experience
from main.models import Skills
from main.forms import SkillsForm

from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

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

def create_skill(request):
    form = SkillsForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Skill baru berhasil ditambahkan!")
        return redirect("main:show_skills")

    context = {
        "name": "Syakira",
        "form": form,
    }
    return render(request, "skills_form.html", context)