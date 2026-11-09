from django.urls import path
from main import api_views

app_name = "api"
urlpatterns = [
    path("experience/", api_views.experience_list, name="experience-list"),
    path("experience/<uuid:experience_id>/", api_views.experience_detail, name="experience-detail"),
    path("experience/<uuid:experience_id>/star/", api_views.experience_star, name="experience-star"),

    path("skills/", api_views.skills_list, name="skills-list"),
    path("skills/<uuid:skill_id>/", api_views.skills_detail, name="skills-detail"),
    path("skills/<uuid:skill_id>/star/", api_views.skills_star, name="skills-star"),
]