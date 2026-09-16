from django.forms import ModelForm, TextInput, Textarea, URLInput

from main.models import Skills

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