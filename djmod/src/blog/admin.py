from django.contrib import admin

from .models import PostModel

# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'slug',
        'content',
        'publish',
        'publish_date',
        'active',
        'updated',
        'timestamp',
        'get_age'
    ]
    readonly_fields = ['updated', 'timestamp', 'get_age']

    def new_content(self, obj, *args, **kwargs):
        return str(obj.title)

    def get_age(self, obj, *args, **kwargs):
        return str(obj.age)

    class Meta:
        model = PostModel


admin.site.register(PostModel, PostModelAdmin)