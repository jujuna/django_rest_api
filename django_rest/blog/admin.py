from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from blog.models import Blog,Category,Tag,Comment
# Register your models here.
@admin.register(Blog)
class BlogModel(SortableAdminMixin,admin.ModelAdmin):
    pass

admin.site.register([Category,Tag,Comment])