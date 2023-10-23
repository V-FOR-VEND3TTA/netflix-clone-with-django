from django.contrib import admin
from netflixapp.models import CustomUser, Profile, Movie, Video

admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(Movie)
admin.site.register(Video)