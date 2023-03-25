from django.contrib import admin
from .models import HomeLogo, HomeBgInfo, HomeSlider, Lastest_Episode
# Register your models here.

admin.site.register(HomeLogo)
admin.site.register(HomeBgInfo)
admin.site.register(Lastest_Episode)

@admin.register(HomeSlider)
class HomeSliderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'proff1', 'proff2']