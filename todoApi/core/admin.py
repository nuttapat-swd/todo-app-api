from django.contrib import admin
from core import models
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    model = models.Task
    list_display = ['title', 'description', 'status']
    readonly_fields = ['owner']

    # def get_name(self,obj):
    #     return obj.tags
    # get_name.short_description = 'Name'
    # get_name.admin_order_field = 'tagname'

class TagAdmin(admin.ModelAdmin):
    model = models.Tag
    list_display = ['tagname']
    

class StatusAdmin(admin.ModelAdmin):
    model = models.Status
    list_display = ['statusname']
    

admin.site.register(models.User)
admin.site.register(models.Task, TaskAdmin)
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Status, StatusAdmin)

