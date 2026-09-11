# Create your models here.
import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None

class Skills(models.Model):
    SKILLS_TYPES = [
        ('soft', 'Soft Skills'),
        ('hard', 'Hard Skills'),
    ]

    CATEGORY_CHOICES = [
        ('design', 'UI/UX and Visual Design'),
        ('programming', 'Programming and Development'),
        ('multimedia_production', 'Multimedia Production'),
        ('digital_productivity', 'Digital Productivity'),
        ('other', 'Others'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=SKILLS_TYPES, default='hard')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='others')
    description = models.TextField()
    proficiency = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )

    def __str__(self):
        return self.name

