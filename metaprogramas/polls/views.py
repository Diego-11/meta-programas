from django.shortcuts import render, redirect, get_object_or_404
import json
from .forms import PollForm
from .models import Polls
from .utils.questions import (separate_options,
                              total,
                              past_present_future,
                              sep_pref)
from .utils.split_values import split_values
from .utils.pdf import generate_pdf


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
            question_nine = sep_pref(form.cleaned_data.get('question_nine'), ['a', 'b', 'c', 'd', 'e'])

            question_ten = sep_pref(form.cleaned_data.get('question_ten'), ['b', 'a', 'c', 'd', 'e'])

            question_eleven = sep_pref(form.cleaned_data.get('question_eleven'), ['b', 'a', 'c', 'd', 'e'])
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

            return redirect('result', pk=pk)
        else:

            form = PollForm

    return render(request, 'polls/forms.html', {'form': form})


def result(request, pk):
    poll = Polls.objects.get(pk=pk)

    question_one = split_values(poll.question_one)
    question_two = split_values(poll.question_two)
    question_three = split_values(poll.question_three)
    question_four = split_values(poll.question_four)
    question_five = split_values(poll.question_five)
    # question_twelve = split_values(poll.question_twelve)

    acer_alej = total(poll.question_one, poll.question_two, poll.question_three)
    sem_diff = {'d': int(question_four['d']) + int(question_five['d']),
                'i': int(question_four['i']) + int(question_five['i'])}

    past = poll.question_six.split("{")[1].split("}")[0].split(",")[0].split(":")[1]
    present = poll.question_six.split("{")[1].split("}")[0].split(",")[1].split(":")[1]
    future = poll.question_six.split("{")[1].split("}")[0].split(",")[2].split(":")[1]
    question_six = {'past': past, 'present': present, 'future': future}

    question_seven = poll.question_seven.split("-")
    question_eight = poll.question_eight.split("-")
    question_nine = poll.question_nine.split("-")

    pref = [0, 0, 0, 0, 0]
    for i in range(5):
        pref[i] += int(question_seven[i]) + int(question_eight[i]) + int(question_nine[i])

    question_ten = split_values(poll.question_ten)
    question_eleven = split_values(poll.question_eleven)

    int_ext = {'d': (int(question_ten['d']) + int(question_eleven['d'])),
               'i': (int(question_ten['i']) + int(question_eleven['i']))}

    print(int_ext)
    ctx = {'poll': poll,
     'question_one': question_one,
     'question_two': question_two,
     'question_three': question_three,
     'question_four': question_four,
     'question_five': question_five,
     'question_six': question_six,
     'question_seven': question_seven,
     'question_eight': question_eight,
     'question_nine': question_nine,
     'question_ten': question_ten,
     'question_eleven': question_eleven,
     'acer_alej': acer_alej,
     'sem_diff': sem_diff,
     'pref': pref,
     'int_ext': int_ext
     }

    
    return render(request, 'polls/result.html', ctx)



