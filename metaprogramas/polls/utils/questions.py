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

    result = {'derecha': p, 'izquierda': n}

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


def preferences(a, b, c):

    preferences = {'actividades': 0,
                    'personas': 0,
                    'objetos': 0,
                    'lugares': 0,
                    'tiempos': 0}

    for i in range(3):

        if a[i] == 'a':
            preferences['actividades'] += 1
        elif b[i] == 'b':
            preferences['actividades'] += 1
        elif c[i] == 'b':
            preferences['actividades'] += 1

        if a[i] == 'b':
            preferences['personas'] += 1
        elif b[i] == 'a':
            preferences['personas'] += 1
        elif c[i] == 'c':
            preferences['personas'] += 1

        if a[i] == 'c':
            preferences['objetos'] += 1
        elif b[i] == 'c':
            preferences['objetos'] += 1
        elif c[i] == 'd':
            preferences['objetos'] += 1

        if a[i] == 'd':
            preferences['lugares'] += 1
        elif b[i] == 'd':
            preferences['lugares'] += 1
        elif c[i] == 'e':
            preferences['lugares'] += 1

        if a[i] == 'e':
            preferences['tiempos'] += 1
        elif b[i] == 'e':
            preferences['tiempos'] += 1
        elif c[i] == 'a':
            preferences['tiempos'] += 1


    return preferences