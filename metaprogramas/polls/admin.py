from django.contrib import admin
from .models import *


# Register your models here.


class PollAdmin(admin.ModelAdmin):

    readonly_fields = [
        'question_one',
        'question_two',
        'question_three',
        'question_four',
        'question_five',
        'question_six',
        'question_seven',
        'question_eight',
        'question_nine',
        'question_ten',
        'question_eleven',
        'question_twelve',
    ]

    def get_queryset(self, request):
        qs = super(PollAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)


admin.site.register(Polls, PollAdmin)
admin.site.register(Candidate)
admin.site.register(AnsweredPolls)
