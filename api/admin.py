from django.contrib import admin

# Register your models here.
from api.models import Movie, Person


class MovieAdmin(admin.ModelAdmin):
    class Meta:
        model = Movie
    list_display = ["__str__", "runtime", "imdb_score", "get_poster_html"]

class PersonAdmin(admin.ModelAdmin):
    class Meta:
        model = Person
    list_display = ["__str__", "get_movies_display"]

admin.site.register(Movie, MovieAdmin)
admin.site.register(Person, PersonAdmin)
