from django.shortcuts import render, redirect
import json
from .forms import PollForm
from .models import AnsweredPolls, Polls
from .utils.questions import (separate_options, 
                                total,
                                past_present_future,
                                preferences)

# Create your views here.


def poll_form(request):

    form = PollForm()
# Test Code
    if request.method == 'POST':

        form = PollForm(request.POST)

        if form.is_valid():

            data = {'answers': []}
            answered_polls = AnsweredPolls()
            

            # Acercarse a - Alejarse de
            question_one = form.cleaned_data.get('question_one')
            question_one = separate_options(question_one, ['a', 'c', 'd'])

            question_two = form.cleaned_data.get('question_two')
            question_two = separate_options(question_two, ['a', 'c', 'f'])

            question_three = form.cleaned_data.get('question_three')
            question_three = separate_options(question_three, ['b', 'c', 'd'])
            # Acercarse a - Alejarse de


            # Semejanzas - Diferencias
            question_five  = form.cleaned_data.get('question_five')
            question_five = separate_options(question_five, ['a', 'c', 'e'])

            question_six = form.cleaned_data.get('question_six')
            question_six = separate_options(question_six, ['b', 'c', 'f'])
            # Semejanzas - Diferencias


            # Pasado -Presente - Futuro
            question_eight = form.cleaned_data.get('question_eight')
            question_eight = past_present_future(question_eight, [
                                                                    ['a','c', 'f', 'l'], 
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

            
            # Acercarse a - Alejarse de
            data['answers'].append({'Acercarse a - Alejarse de': total(question_one, question_two, question_three)})

            # Semejanzas - Diferencias
            data['answers'].append({'Semejanzas - Diferencias': total(question_five, question_six, '0-0')})

            # Pasado -Presente - Futuro
            data['answers'].append({'Pasado -Presente - Futuro': preferences(question_nine, question_ten, question_eleven)})

            # Preferencias
            data['answers'].append({'Preferencias': total(question_twelve, question_thirteen, '0-0')})

            # Guardado en base de datos
            answered_polls.answers = data
            AnsweredPolls.save(self=answered_polls)
        else:

            form = PollForm

    return render(request, 'polls/forms.html', {'form': form})
