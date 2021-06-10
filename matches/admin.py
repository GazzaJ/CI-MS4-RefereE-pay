from django.contrib import admin
from .models import Club, Venue, Team, Game, Fee


class ClubAdmin(admin.ModelAdmin):
    list_display = (
        'club_name',
        'club_badge',
        'website_url',
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


admin.site.register(Club, ClubAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Fee, FeeAdmin)
