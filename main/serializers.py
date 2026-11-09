from django.utils.html import strip_tags
from rest_framework import serializers

from main.models import Experience, Skills


class ExperienceSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = [
            "id", "title", "description", "category",
            "thumbnail", "started_at", "ended_at",
            "starred_by", "star_count", "is_starred", "starred_by_names"
        ]
        read_only_fields = [
            "id", "starred_by", "star_count", "is_starred", "starred_by_names",
        ]

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_description(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Description cannot be empty.")
        return value

    def validate_category(self, value):
        return strip_tags(value)

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return request.user in obj.starred_by.all()

    def get_starred_by_names(self, obj):
        return ", ".join(user.username for user in obj.starred_by.all())

from main.models import Experience, Skills

class SkillsSerializer(serializers.ModelSerializer):
    # Use a plain field so validate_category can strip markup before the
    # model's generated ChoiceField rejects the raw value.
    category = serializers.CharField(max_length=50)
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()

    class Meta:
        model = Skills
        fields = [
            "id", "name", "type", "category",
            "description", "proficiency",
            "starred_by", "star_count", "is_starred", "starred_by_names"
        ]
        read_only_fields = [
            "id", "starred_by", "star_count", "is_starred", "starred_by_names",
        ]

    def validate_name(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Name cannot be empty.")
        return value

    def validate_description(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Description cannot be empty.")
        return value

    def validate_type(self, value):
        return strip_tags(value).strip()

    def validate_category(self, value):
        value = strip_tags(value).strip()
        valid_categories = {choice[0] for choice in Skills.CATEGORY_CHOICES}
        if value not in valid_categories:
            raise serializers.ValidationError("Select a valid choice.")
        return value

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return request.user in obj.starred_by.all()

    def get_starred_by_names(self, obj):
        return ", ".join(user.username for user in obj.starred_by.all())
