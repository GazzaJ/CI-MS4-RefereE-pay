from django.contrib import admin
from .models import Club, Venue, Team, Game, Fee, Competition, Chat, Official


class ClubAdmin(admin.ModelAdmin):
    list_display = (
        'club_name',
        'club_badge',
        'website_url',
    )


class OfficialAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class CompetitionAdmin(admin.ModelAdmin):
    list_display = (
        'comp',
    )


class VenueAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'town_or_city',
        'postcode',
    )


class TeamAdmin(admin.ModelAdmin):
    list_display = (
        'team_name',
        'age',
        'manager_coach',
    )


class FeeAdmin(admin.ModelAdmin):
    list_display = (
        'age',
        'referee_fee',
        'asst_referee',        
    )

    ordering = ('age',)


class GameAdmin(admin.ModelAdmin):
    list_display = (        
        'home_team',
        'away_team',
        'venue',
        'date_time',
    )

    ordering = ('date_time',)


class ChatAdmin(admin.ModelAdmin):
    list_display = (
        'match',
        'author',
        'date',
    )

    ordering = ('date',)


admin.site.register(Chat, ChatAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Fee, FeeAdmin)
admin.site.register(Official, OfficialAdmin)
