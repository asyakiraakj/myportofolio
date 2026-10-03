from django.forms import ModelForm, TextInput, Textarea, URLInput, ModelChoiceField, Select

from main.models import Skills, Experience

from django.core.exceptions import ValidationError
from django.utils.html import strip_tags

class SkillsForm(ModelForm):
    class Meta:
        model = Skills
        fields = [
            "name",
            "type",
            "category",
            "description",
            "proficiency",
        ]

        labels = {
            "name": "Nama Skill",
            "type": "Tipe Skill (soft/hard)",
            "category": "Kategori",
            "description": "Deskripsi Proyek",
            "proficiency": "Proficiency",
        }

        widgets = {
            "name": TextInput(
                attrs={
                    "placeholder": "Nama skill",
                    "maxlength": 100,
                }
            ),
            "type": TextInput(
                attrs={
                    "placeholder": "(soft/hard)",
                    "maxlength": 100,
                }
            ),
            "category": TextInput(
                attrs={
                    "placeholder": "Design, Programming, Multimedia Production, Others",
                }
            ),
            "category": Textarea(
                attrs={
                    "placeholder": "deskripsi",
                }
            ),
            "proficiency": TextInput(
                attrs={
                    "placeholder": "1—10",
                }
            ),
        }

    def clean_name(self):
        name = strip_tags(self.cleaned_data["name"]).strip()
        if not name:
            raise ValidationError("Nama skill tidak boleh hanya berisi tag HTML.")
        return name

    def clean_category(self):
        return strip_tags(self.cleaned_data["category"]).strip()

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()

    

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
        ]
        labels = {
            "title": "Experience title",
            "description": "Description",
            "category": "Category",
            "thumbnail": "Insert url"
        }
        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Experience title",
                    "maxlength": 100
                }
            ),
            "description": TextInput(
                attrs={
                    "placeholder": "Experience description",
                    "maxlength": 500
                }
            ),
            "category": TextInput(
                attrs={
                    "placeholder": "Internship, Research, Volunteer, Part-time, Full-time, Freelance",
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "Experience title",
                }
            )
        }
