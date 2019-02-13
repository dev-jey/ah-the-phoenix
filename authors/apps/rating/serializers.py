
from rest_framework import serializers
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Rating
from django.db.models import Avg


class RatingSerializer(serializers.ModelSerializer):
    """Serializers for the rating model"""
    max_rating = 5
    min_rating = 1
    user_rating = serializers.IntegerField(
        required = True,
        validators = [
            MinValueValidator(min_rating, message="The minimum allowed rating is 1"),
            MaxValueValidator(max_rating, message="The maximum allowed rating is 5")
        ],
        error_messages = {
            "required": "Please provide a rating between 1 and 5"
        }
    )
    article = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()

    def get_average_rating(self, obj):
        """Returns the average rating for an article"""
        average_rating = Rating.objects.filter(
            article = obj.article.id).aggregate(Avg('user_rating'))
        return average_rating["user_rating_avg"]

    def get_article(self, obj):
        """Returns an article that matches the slug"""
        return obj.article.slug

    class Meta:
        model = Rating
        fields = ("article", "user_rating", "average_rating")