from django.urls import path
from rest_framework.authtoken import views as authtoken_views
from main import api_views

app_name = "api"
urlpatterns = [
    path("auth/token/", authtoken_views.obtain_auth_token, name="api_token_auth"),
    # Register auth/logout/ pointing to api_views.api_logout
    path("auth/logout/", api_views.api_logout, name="api_logout"),
    path("experience/", api_views.experience_list, name="experience-list"),
    path("experience/<uuid:experience_id>/", api_views.experience_detail, name="experience-detail"),
    path("experience/<uuid:experience_id>/star/", api_views.experience_star, name="experience-star"),

    path("skills/", api_views.skills_list, name="skills-list"),
    path("skills/<uuid:skill_id>/", api_views.skills_detail, name="skills-detail"),
    path("skills/<uuid:skill_id>/star/", api_views.skills_star, name="skills-star"),
]