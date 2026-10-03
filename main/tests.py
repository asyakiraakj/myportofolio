from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience
from main.models import Skills


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "Sedang berlangsung")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Selesai")
        self.assertNotContains(response, "Sedang berlangsung")

class SkillsPageTest(TestCase):
    def setUp(self):
        self.hard_skill = Skills.objects.create(
            name="Python",
            type="hard",
            category="programming",
            description="Backend web development using Django.",
            proficiency=9,
        )
        # Sample soft skill
        self.soft_skill = Skills.objects.create(
            name="Communication",
            type="soft",
            category="other",
            description="I communicate.",
            proficiency=8,
        )

    def test_skills_url_and_template(self):
        response = self.client.get(reverse("main:show_skills"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "skills.html")

        self.assertContains(response, "<title>Skills - Syakira</title>")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')
        self.assertContains(response, f'href="{reverse("main:show_skills")}"')

    def test_skills_page(self):
        response = self.client.get(reverse("main:show_skills"))

        self.assertContains(response, self.hard_skill.name)
        self.assertContains(response, self.hard_skill.description)
        self.assertContains(response, "Proficiency: 9/10")
        self.assertContains(response, self.hard_skill.category)

        self.assertContains(response, self.soft_skill.name)
        self.assertContains(response, self.soft_skill.description)
        self.assertContains(response, "Proficiency: 8/10")

    def test_skills_page_empty_state(self):
        Skills.objects.all().delete()
        response = self.client.get(reverse("main:show_skills"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Belum ada skill yang ditambahkan", count=2) #count=2: "Belum ada skill yang ditambahkan" ada 2 (soft & hard)