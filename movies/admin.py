from django.contrib import admin

# Register your models here.
from movies.models import Watchlist, WatchlistMovie


class WatchlistMovieInline(admin.TabularInline):
    model = WatchlistMovie
    extra = 0


class WatchlistAdmin(admin.ModelAdmin):
    inlines = (WatchlistMovieInline,)
    list_display = ("__str__", "get_movies_html", "get_progress_html")


admin.site.register(Watchlist, WatchlistAdmin)