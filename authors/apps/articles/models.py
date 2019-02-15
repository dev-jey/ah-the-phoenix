from django.db import models
from django.utils.text import slugify

from authors.apps.authentication.models import User
from cloudinary.models import CloudinaryField


class Article(models.Model):
    """Create models for the articles"""
    title = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=400, blank=False)
    body = models.TextField(blank=False)
    image = CloudinaryField(blank=True, null=True)
    slug = models.SlugField(db_index=True, max_length=1000,
                            unique=True, blank=True, primary_key=True)
    author = models.ForeignKey(User, related_name='articles',
                               on_delete=models.CASCADE,
                               blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def generate_slug(self):
        """generating a slug for the title of the article
            eg: this-is-an-article"""
        slug = slugify(self.title)
        new_slug = slug
        s = 1
        while Article.objects.filter(slug=new_slug).exists():
            """increase value of slug by one"""
            new_slug = f'{slug}-{s}'
            s += 1
        return new_slug

    def save(self, *args, **kwargs):
        """create an article and save to the database"""
        if not self.slug:
            self.slug = self.generate_slug()
        super().save(*args, **kwargs)


class Rating(models.Model):
    """The rating model"""
    user = models.ForeignKey(
        User,
        related_name="rater",
        on_delete=models.CASCADE
    )
    article = models.ForeignKey(
        Article,
        related_name="rated_article",
        on_delete=models.CASCADE
    )
    user_rating = models.FloatField()

    def __str__(self):
        return self.user_rating
