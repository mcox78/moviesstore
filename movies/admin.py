from django.contrib import admin
from .models import Movie, Review, Petition, PetitionVote

class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']

admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)


@admin.register(Petition)
class PetitionAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_at', 'vote_count')
    search_fields = ('title', 'description', 'created_by__username')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

    # Optional: show vote count in the admin list
    def vote_count(self, obj):
        return obj.votes.count()
    vote_count.short_description = 'Votes'


@admin.register(PetitionVote)
class PetitionVoteAdmin(admin.ModelAdmin):
    list_display = ('petition', 'user', 'voted_at')
    search_fields = ('petition__title', 'user__username')
    list_filter = ('voted_at',)
    ordering = ('-voted_at',)