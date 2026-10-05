from django.urls import path

from main.views import *

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("skills/", show_skills, name="show_skills"),
    path("skills/add/", create_skill, name="create_skill"),
    path("api/skills/", get_skills_json, name="get_skills_json"),
    path("skills/<uuid:skill_id>/delete/",delete_skill,name="delete_skill"),
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/<uuid:experience_id>/delete/",delete_experience,name="delete_experience"),
    path("experience/<uuid:experience_id>/update/", update_experience, name="update_experience"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    # Tambahkan path ini ke dalam urlpatterns
    path(
        "skills/<uuid:skill_id>/star/",
        toggle_star_skill,
        name="toggle_star_skill",
    ),
    path(
        "experiences/<uuid:experience_id>/star/",
        toggle_star_experience,
        name="toggle_star_experience",
    ),
    path('json/', get_skills_json, name='get_skills_json'),
    path('json/', get_experiences_json, name='get_experiences_json'),


]