from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.shortcuts import reverse
from fontawesome.fields import IconField


class Carosue(models.Model):
    title1 = models.CharField(max_length=200)
    image1 = models.ImageField(upload_to='images', verbose_name='image1')
    content1 = models.CharField(max_length=300)

    def __str__(self):
        return self.title1


class Index_writeup(models.Model):
    title = models.CharField(max_length=200)
    content_para1 = models.TextField()
    content_para2 = models.TextField()
    content_para3 = models.TextField()

    def __str__(self):
        return self.title


class Vision_mission(models.Model):
    vision = models.TextField()
    mission = models.TextField()
    value = models.TextField()

    def __str__(self):
        return self.vision


class Quote(models.Model):
    services = models.TextField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date_time = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return self.name


class Stats(models.Model):
    name = models.CharField(max_length=1, blank=True)
    yearsofxperience = models.PositiveIntegerField()
    projectscompleted = models.PositiveIntegerField()
    happyclients = models.PositiveIntegerField()
    bussinesspartners = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Services(models.Model):
    images = models.ImageField(upload_to='images')
    title = models.CharField(max_length=100)
    title_extension = models.CharField(blank=True,max_length=200)
    content_small = models.TextField(blank=True,max_length=1000)
    content = models.TextField(max_length=2000,blank=True)
    icon = IconField()

    def __str__(self):
        return self.title


class Projects(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    pictures = models.ImageField(upload_to='images', verbose_name='pictures')


class Category(models.Model):
    cat_name = models.CharField(max_length=50, verbose_name='Category Name')

    class Meta:
        ordering = ('cat_name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.cat_name


class Blog(models.Model):
    blog_title = models.CharField(max_length=150, verbose_name='Post Title')
    blog_img = models.ImageField(upload_to='images', verbose_name='Post Image')
    upload_date = models.DateTimeField(default=timezone.now)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_category = models.ManyToManyField(Category, verbose_name='Category')
    content = models.TextField()
    slug = models.SlugField()
    
    class Meta:
        ordering = ('-upload_date',)

    def __str__(self):
        return self.blog_title
    
    def save(self, *args, **kwargs):
        # self.slug = slug(self.title)
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        return f'/{self.slug}'
        
    

class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

class Media(models.Model):
    name = models.CharField(max_length=100)
    media = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

class About(models.Model):
    directors_contentp1 = models.TextField(max_length=2000)
    directors_contentp2 = models.TextField(max_length=2000)
    directors_contentp3 = models.TextField(max_length=2000)
    directors_signature = models.ImageField(
        upload_to='images', verbose_name='pictures')
    directors_name = models.CharField(max_length=110)
    directors_title = models.CharField(max_length=50)

    def __str__(self):
        return self.directors_name


class Our_clients(models.Model):
    client_name = models.CharField(max_length=20)
    client_logo = models.ImageField(upload_to='images')

    def __str__(self):
        return self.client_name


class Business_hours(models.Model):
    bussiness_opening_days = models.CharField(max_length=50)
    bussiness_vacation_days = models.CharField(max_length=50)

    def __str__(self):
        return self.bussiness_opening_days


class Office_address(models.Model):
    office_address = models.CharField(max_length=500)

    def __str__(self):
        return self.office_address


class Official_telephone_number(models.Model):
    title = models.CharField(max_length=10, blank=True)
    official_telephone_number = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Office_mail(models.Model):
    office_mail = models.CharField(max_length=200)

    def __str__(self):
        return self.office_mail


class Core_services(models.Model):
    service_title = models.CharField(max_length=200)
    service_content = models.CharField(max_length=2000)

    def __str__(self):
        return self.service_title


class Other_services(models.Model):
    title = models.CharField(max_length=300)
    content = models.CharField(max_length=3000)
    # font_awesome_image = models.Fo

    def __str__(self):
        return self.title


class Core_team(models.Model):
    name = models.CharField(max_length=300)
    picture = models.ImageField(upload_to='images')
    job_title = models.CharField(max_length=500)
    content = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=300)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Productlist(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    images1 = models.ImageField(upload_to='images')
    images2 = models.ImageField(upload_to='images')
    images3 = models.ImageField(upload_to='images',blank=True)
    images4 = models.ImageField(upload_to='images',blank=True)
    images5 = models.ImageField(upload_to='images',blank=True)
    images6 = models.ImageField(upload_to='images',blank=True)
    images7 = models.ImageField(upload_to='images',blank=True)
    images8 = models.ImageField(upload_to='images',blank=True)
    images8 = models.ImageField(upload_to='images',blank=True)
    images9 = models.ImageField(upload_to='images',blank=True)
    images10 = models.ImageField(upload_to='images',blank=True)
    
    def __str__(self):
        return self.name
        
class CategoryP(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('powercool_app:product_list_by_category', args=[self.slug])

class ShopProduct(models.Model):
    category = models.ForeignKey(CategoryP, related_name='shopproduct', on_delete=models.CASCADE)
    product_name1 = models.CharField(max_length=100, verbose_name='product1')
    product_content = models.CharField(max_length=500, verbose_name='content')
    product_img1 = models.ImageField(upload_to='images', verbose_name='product1 image')
    product_desc1 = models.CharField(max_length=100, verbose_name='product1_desc')
    product_price1 = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, db_index=True)
    available = models.BooleanField(default=True)
    


    class Meta:
        ordering = ('product_name1', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.product_name1

    def get_absolute_url(self):
        return reverse('powercool_app:shop_single', args=[self.id, self.slug])
        
   