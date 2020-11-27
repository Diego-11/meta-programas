def separate_options(question, options):

    # if len(options) > 3:

    #     raise ValueError("Sólo se permiten 3 opciones")

    p = 0
    n = 0

    for value in question:

        if value == options[0]:
            p += 1
        elif value == options[1]:
            p += 1
        elif value == options[2]:
            p += 1
        else:
            n += 1

    return f'{p}-{n}'


def total(value_one, value_two, value_three):

    p = 0
    n = 0

    value_one = value_one.split('-')
    value_two = value_two.split('-')
    value_three = value_three.split('-')

    p = int(value_one[0]) + \
        int(value_two[0]) + \
        int(value_three[0])

    n = int(value_one[1]) + \
        int(value_two[1]) + \
        int(value_three[1])

    result = {'d': p, 'i': n}

    return result

def past_present_future(question, options):

    past = 0
    present = 0
    future = 0

    for value in question:

        if value == options[0][0]:
            past += 1 

        elif value == options[0][1]:
            past += 1

        elif value == options[0][2]:
            past += 1

        elif value == options[0][3]:
            past += 1

        else:
            if value == options[1][0]:
                present += 1

            elif value == options[1][1]:
                present += 1
                
            elif value == options[1][2]:
                present += 1

            elif value == options[1][3]:
                present += 1

            else:

                future += 1
    
    result = {'past': past, 'present': present, 'future': future}

    return result


def sep_pref(question, values):

    pref = [0, 0, 0, 0, 0]
    print(question)
    for i in range(len(question)):

        if question[i] == values[0]:
            pref[0] += 1

        elif question[i] == values[1]:
            pref[1] += 1

        elif question[i] == values[2]:
            pref[2] += 1

        elif question[i] == values[3]:
            pref[3] += 1

        elif question[i] == values[4]:
            pref[4] += 1

    return f"{pref[0]}-{pref[1]}-{pref[2]}-{pref[3]}-{pref[4]}"
