from django.contrib import admin
from .models import Profile, Journal, Comment, Foll

# Register your models here.
class JournalAdmin(admin.ModelAdmin):

    list_display = ('Your_Post_title', 'content', 'image', 'slug', 'Your_Appreciation_or_Critics_about_this_movie', 'timestamp')


    search_fields = ['Your_name']

    prepopulated_fields = {'slug': ('Your_Post_title',)}


admin.site.register(Profile)
admin.site.register(Journal, JournalAdmin)
admin.site.register(Comment)
admin.site.register(Foll)
