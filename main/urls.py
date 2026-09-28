from django.urls import path

from main.views import (
    show_main, 
    show_experience, 
    show_skills, 
    create_skill, 
    get_skills_json,
    delete_skill,
    create_experience,
    update_experience,
    delete_experience,
    register,
    login_user,
    logout_user,
    toggle_star
)

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
        "projects/<uuid:project_id>/star/",
        toggle_star,
        name="toggle_star",
    ),

]