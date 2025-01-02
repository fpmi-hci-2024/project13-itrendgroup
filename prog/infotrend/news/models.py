from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class PublishManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=News.Status.PUBLISHED)


class News(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'
        

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True,  verbose_name='Контент')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=Status.choices, default=Status.DRAFT)
    cat = models.ForeignKey('Cat', on_delete=models.PROTECT, related_name='posts',  verbose_name='Категории')    
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='posts', null=True, default=None)



    objects = models.Manager()
    published = PublishManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

        ordering = ['-time_create']
        indexes =[ 
            models.Index(fields = ['-time_create'])
        ]
        
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug}) 





class Cat(models.Model):
    icon = models.CharField(max_length=100, db_index=True)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)  


    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

    def __str__(self): 
        return self.name

    def get_absolute_url(self):
            return reverse('category', kwargs={'cat_slug': self.slug})

