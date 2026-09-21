# Create your views here.
from django.shortcuts import render

from main.models import Experience
from main.models import Skills
from main.forms import SkillsForm
from main.forms import ExperienceForm

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
    json_response = get_experience_json(request)
    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )

    experiences = [experience.object for experience in experiences]
    name_query = request.GET.get("name", "").strip()
    category_query = request.GET.get("category", "").strip()
    context = {
        "name": "Syakira",
        "experience_list": experiences,
        "name_query": name_query,
        "category_query": category_query,
        "experience_categories": Experience.EXPERIENCE_CHOICES,
    }
    return render(request, "experience.html", context)

def show_skills(request):
    json_response = get_skills_json(request)

    skills = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    skills = [skill.object for skill in skills]
    name_query = request.GET.get("name", "").strip()

    hard_skills = [skill for skill in skills if skill.type == 'hard']
    soft_skills = [skill for skill in skills if skill.type == 'soft']

    context = {
        "name": "Syakira",
        "skills_list": skills,
        "hard_skills": hard_skills,
        "soft_skills": soft_skills,
        "name_query": name_query,
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

def delete_skill(request, skill_id):
    skill = get_object_or_404(Skills, pk=skill_id)

    if request.method == "POST":
        skill.delete()
        messages.success(request, "Skill berhasil dihapus!")
        return redirect("main:show_skills")

    return redirect("main:show_skills")

def get_skills_json(request):
    name_query = request.GET.get("name", "").strip()
    skills = Skills.objects.all()

    if name_query:
        skills = skills.filter(name__icontains=name_query)

    skills_json = serializers.serialize("json", skills)
    return HttpResponse(skills_json, content_type="application/json")

def get_experience_json(request):
    name_query = request.GET.get("name", "").strip()
    category_query = request.GET.get("category", "").strip()
    experiences = Experience.objects.all()

    if name_query:
        experiences = experiences.filter(title__icontains=name_query)
    if category_query:
        experiences = experiences.filter(category=category_query)
    experiences_json = serializers.serialize("json", experiences)
    return HttpResponse(experiences_json, content_type="application/json")

def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Burhan",
        "form": form,
    }
    return render(request, "experience_form_create.html", context)

def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

def update_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience berhasil diperbarui!")
        return redirect("main:show_experience")

    context = {
        "name": "Syakira",
        "form": form,
        "experience": experience,
    }
    return render(request, "experience_form_update.html", context)