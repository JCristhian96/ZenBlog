from django.db import models
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth.models import User
#
from tinymce import models as tinymce_models
from easy_thumbnails.fields import ThumbnailerImageField

class Category(models.Model):
    title = models.CharField('Titulo', max_length=50)    
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categorys"
                
    def __str__(self):
        return self.title
    
    
class Post(models.Model):
    title = models.CharField('Titulo', max_length=200)    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoria')
    image = ThumbnailerImageField(verbose_name='Imagen', upload_to='images', blank=True)
    content = tinymce_models.HTMLField(verbose_name='Contenido')
    description = models.TextField(null=True, blank=True, verbose_name='Descripcion')
    created = models.DateTimeField('Creacion', default=timezone.now)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("core:post", kwargs={"pk": self.pk})
    
    
class Favorite(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_favorites')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_favorites')

    class Meta:
        verbose_name = "Favorite"
        verbose_name_plural = "Favorites"
        unique_together = ('post', 'user')