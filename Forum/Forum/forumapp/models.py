from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Category(models.Model):
	category_title = models.CharField(max_length=100, db_index=True)
	slug = models.SlugField(max_length=100, db_index=True)
	image = models.ImageField(upload_to='media', help_text='150x150px', default=True)

	def __str__(self):
		return self.category_title

	def get_absolute_url(self):
		return reverse('category_detail_url', kwargs={'category_slug': self.slug})

	


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    post_slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media', help_text='150x150px', default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=True)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.post_slug})

    def get_update_url(self):
        return reverse('post_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('post_delete_url', kwargs={'slug': self.slug})

    

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_pub']


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self):
		super().save()

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)