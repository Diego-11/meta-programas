from django.contrib import admin
from .models import *


# Register your models here.


class PollAdmin(admin.ModelAdmin):

    """def queryset(self, request):
        qs = super(PollAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)"""

    def get_queryset(self, request):
        qs = super(PollAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)


admin.site.register(Polls, PollAdmin)
admin.site.register(Candidate)
