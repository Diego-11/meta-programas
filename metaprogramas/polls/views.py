from django.shortcuts import render, redirect, get_object_or_404
import json
from .forms import PollForm
from .models import Polls
from .utils.questions import (separate_options,
                              total,
                              past_present_future,
                              preferences)


# Create your views here.


def poll_form(request, pk):
    poll = get_object_or_404(Polls, pk=pk)

    form = PollForm()
    # Test Code
    if request.method == 'POST':

        form = PollForm(request.POST)

        if form.is_valid():

            # Acercarse a - Alejarse de
            question_one = form.cleaned_data.get('question_one')
            question_one = separate_options(question_one, ['a', 'c', 'd'])

            question_two = form.cleaned_data.get('question_two')
            question_two = separate_options(question_two, ['a', 'c', 'f'])

            question_three = form.cleaned_data.get('question_three')
            question_three = separate_options(question_three, ['b', 'c', 'd'])
            # Acercarse a - Alejarse de

            # Semejanzas - Diferencias
            question_five = form.cleaned_data.get('question_five')
            question_five = separate_options(question_five, ['a', 'c', 'e'])

            question_six = form.cleaned_data.get('question_six')
            question_six = separate_options(question_six, ['b', 'c', 'f'])
            # Semejanzas - Diferencias

            # Pasado -Presente - Futuro
            question_eight = form.cleaned_data.get('question_eight')
            question_eight = past_present_future(question_eight, [
                ['a', 'c', 'f', 'l'],
                ['b', 'e', 'h', 'j'],
            ])
            # Pasado -Presente - Futuro

            # Preferencias
            question_nine = form.cleaned_data.get('question_nine')

            question_ten = form.cleaned_data.get('question_ten')

            question_eleven = form.cleaned_data.get('question_eleven')
            # Preferencias

            # Interno - Externo
            question_twelve = form.cleaned_data.get('question_twelve')
            question_twelve = separate_options(question_twelve, ['c', 'd', 'f'])

            question_thirteen = form.cleaned_data.get('question_thirteen')
            question_thirteen = separate_options(question_thirteen, ['b', 'c', 'f'])
            # Interno - Externo

            question_fourteen = form.cleaned_data.get('question_fourteen')

            # Guardado en base de datos
            poll.question_one = question_one
            poll.question_two = question_two
            poll.question_three = question_three
            poll.question_four = question_five
            poll.question_five = question_six
            poll.question_six = question_eight
            poll.question_seven = question_nine
            poll.question_eight = question_ten
            poll.question_nine = question_eleven
            poll.question_ten = question_twelve
            poll.question_eleven = question_thirteen
            poll.question_twelve = question_fourteen

            poll.save()

        else:

            form = PollForm

    return render(request, 'polls/forms.html', {'form': form})
