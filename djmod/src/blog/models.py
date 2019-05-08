from datetime import timedelta, datetime, date

from django.db import models
from django.utils.encoding import smart_text
from django.utils import timezone
from django.utils.text  import slugify
from django.utils.timesince import timesince

from django.db.models.signals import post_save, pre_save

from .validators import validate_author_email


# Create your models here.



PUBLISH_CHOICES = (
    ('draft', 'Draft'),
    ('publish', 'Publish'),
    ('private', 'Private')
)

class PostModelManager(models.Manager):
    def all(self, *args, **kwargs):
        qs = super(PostModelManager, self).all(*args, **kwargs).filter(active=True)
        print(qs)
        return


class PostModel(models.Model):
    id              = models.BigAutoField(primary_key=True)
    active          = models.BooleanField(default=True)
    title           = models.CharField(
                                max_length=30, 
                                default="New Title", 
                                verbose_name='Post Title', 
                                unique=True,
                                error_messages={
                                    'unique': 'This Title is not Unique, Please Try Again!!!'
                                },
                                help_text='Must be Unique Title'
                            )
    slug            = models.SlugField(null=True, blank=True)
    content         = models.TextField(null=True, blank=True)
    publish         = models.CharField(max_length=120, default='draft', choices=PUBLISH_CHOICES)
    view_count      = models.IntegerField(default=0)
    publish_date    = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    # author_email    = models.CharField(max_length=50, null=True, blank=True, validators=[validate_author_email])
    author_email    = models.EmailField(max_length=50, null=True, blank=True)
    updated         = models.DateTimeField(auto_now=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    

    objects = PostModelManager()  # Overiding or extending the current PostModel.objects with new all method 

    def save(self, *args, **kwargs):
        # if not self.slug:
        #     self.slug = slugify(self.title)
        super(PostModel, self).save(*args, **kwargs)
        

    class Meta:
        verbose_name        = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return smart_text(self.title)

    @property
    def age(self):
        # return '{t} ago'.format(t=timesince(self.publish_date))
        if self.publish == 'publish':
            now = datetime.now()
            publish_time = datetime.combine(
                                self.publish_date,
                                datetime.now().min.time()
                        )
            try:
                difference = now - publish_time
            except:
                return 'Unknown'
            if difference <= timedelta(minutes=1):
                return 'Just Now'
            return '{time} ago'.format(time=timesince(publish_time).split(', ')[0])
        return 'Not Published'

def blog_post_model_pre_save_reciever(sender, instance, *args, **kwargs):
    print('before save')
    if not instance.slug and instance.title:
        instance.slug = slugify(instance.title)

pre_save.connect(blog_post_model_pre_save_reciever, sender=PostModel)

def blog_post_model_post_save_reciever(sender, instance, created, *args, **kwargs):
    print('after save')
    if not instance.slug and instance.title:
        instance.slug = slugify(instance.title)
        instance.save()

post_save.connect(blog_post_model_post_save_reciever, sender=PostModel)