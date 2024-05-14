from django.contrib import admin
from .models import *


# Register your models here.

class AboutPAge(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ['id', 'title']
    filter_horizontal = ['tags',]


admin.site.register(HomePage)
admin.site.register(Home)
admin.site.register(Sermons)
admin.site.register(About, AboutPAge)
admin.site.register(Tag)
admin.site.register(Testimonial)
admin.site.register(Author)
admin.site.register(OurS)
admin.site.register(Ministries)
admin.site.register(Events)
admin.site.register(Blog)
