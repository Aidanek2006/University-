from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


@admin.register(Course)
class CourseAdmin(TranslationAdmin):
    list_display = ("description",)

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(UserProfile)
admin.site.register(Faculty)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Cabinet)
admin.site.register(Schedule)
admin.site.register(Recording)
admin.site.register(HomeWork)
admin.site.register(HandingHomeWork)
