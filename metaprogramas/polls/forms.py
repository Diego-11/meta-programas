from django.forms import (Form,
                          MultipleChoiceField,
                          CheckboxSelectMultiple,
                          CharField,
                          Textarea,
                          ModelForm)



class Multiple(MultipleChoiceField):

    def __init__(self, choices, label, **kwargs):
        super().__init__(choices=choices, label=label, required=False, widget=CheckboxSelectMultiple)


class PollForm(Form):

    question_one = Multiple(choices=(
        ('a', 'Ponerme en Forma'),
        ('b', 'Evitar dolores o lesiones al hacer deporte'),
        ('c', 'Adquirir una sensación de logro personal'),
        ('d', 'Disfrutar del Ambiente'),
        ('e', 'Liberar la presión del trabajo'),
        ('f', 'Para no aumentar de peso')
    ), label="Piensa en hacer ejercicio: ¿Para qué lo harías?", )

    question_two = Multiple(choices=(
        ('a', 'El tipo de trabajo que más me gustaría hacer'),
        ('b', 'Las situaciones y personas que no me gustan y que deseo evitar'),
        ('c', 'La satisfacción que se obtienie de hacer lo que quiero'),
        ('d', 'Las frustraciones que estoy teniendo'),
        ('e', 'Las cosas que mi trabajo actual no me da'),
        ('f', 'La clase de trabajo que satisface mis necesidades')
    ), label="Pregunta 2 - Cuando piensas en cambiar de trabajo ¿En cuáles de los siguientes aspectos piensas?")

    question_three = Multiple(choices=(
        ('a', 'Pienso en los problemas de organizar una vacación'),
        ('b', 'Comienzo a imaginarme la vacación'),
        ('c', 'Pienso que es lo que me gustaría hacer'),
        ('d', 'Recuerdo los beneficios de salir de vacaciones'),
        ('e', 'Pienso en evitar los problemas que he tenido en vacaciones anteriores'),
        ('f', 'Pienso en todo lo que tengo que hacer primero')
    ), label="Pregunta 3 - Cuando decido irme de vacaciones: ¿Qué hago?")

    question_five = Multiple(choices=(
        ('a', 'Buscas aspectos de esta compra que sean similares a compras anteriores'),
        ('b', 'Usas el enfoque de descubrir en qué manera esto no llena tus necesidades'),
        ('c', 'Comparas con una lista (real o mental) de carecterísticas que tu quieres que tenga'),
        ('d', 'Buscas algo que sea diferente a lo que has tenido antes'),
        ('e', 'Buscas similaridades entre este producto y otros que conoces'),
        ('f', 'Quieres algo único, diferente a cualquier otro')
    ), label="Pregunta 5 - Piensa que estás en el proceso de comprar algo. ¿Cuál o cuáles de las siguientes cosas "
             "haces?")

    question_six = Multiple(choices=(
        ('a', 'Buscas un buen debate'),
        ('b', 'Buscas por los puntos de coincidencia'),
        ('c', 'Presionas para lograr un acuerdo'),
        ('d', 'Haces un "test" de los puntos de vista de los demás, para encontrar dónde están errados.'),
        ('e', 'Te encuentras a ti utilizando la expresión "Si, pero..."'),
        ('f', 'Encuentras que generalmente estás en compañía de gente que comparte tus ideas.')
    ), label="Pregunta 6 - En una conversación. ¿Cuáles de los siguientes aspectos aplica a ti?")

    question_eight = Multiple(choices=(
        ('a', 'Recordar las vacaciones que haz tenido'),
        ('b', 'Apreciar las cosas que ves, oyes y sientes, a tu alrededor'),
        ('c', 'Planificar lo que vas a hacer en el futuro'),
        ('d', 'Poner atención a lo que está sucediendo a tu alrededor'),
        ('e', 'Liberar la presión del trabajo'),
        ('f', 'Reflexionar sobre conversaciones que haz tenido'),
        ('g', 'Decidir cómo pasarás el día'),
        ('h', 'Disfrutar cada momento'),
        ('i', 'Soñar sobre dónde te gustaría estar'),
        ('j', 'Estar consciente de cómo te sientes'),
        ('k', 'Anticipar lo que va a suceder'),
        ('l', 'Recordar el pasado'),
    ), label="Pregunta 8 - ¿Cuáles de las siguientes son carecterísticas que corresponden a tu persona?")

    question_nine = Multiple(choices=(
        ('a', 'Lo que sucedió'),
        ('b', 'Quien estaba contigo'),
        ('c', 'Los objetos asociados: Un plato en particular, un regalo que te dieron, la decoración, etc'),
        ('d', 'El lugar: El restaurante, la ciudad, la urbanización, etc'),
        ('e', 'La fecha, la ocasión, la hora.'),
    ), label="Pregunta 9 - Piensa en la mejor comida que haz tenido. ¿En qué estás pensando?")

    question_ten = Multiple(choices=(
        ('a', 'Estar con alguna(s) persona(s) en particular'),
        ('b', 'Lo que estarías haciendo (la actividad)'),
        ('c', 'Con qué objetos lo harías (un libro, implementos deportivos, etc)'),
        ('d', 'Donde estarías'),
        ('e', 'El momento, la época (Navidad, un domingo, un día soleado, etc)'),
    ), label="Pregunta 10 - Piensa en cómo te gusta pasar el tiempo. ¿Piensas en?")

    question_eleven = Multiple(choices=(
        ('a', 'La fecha, la ocasión.'),
        ('b', 'Lo que estarías sucediendo'),
        ('c', 'La gente involucrada'),
        ('d', 'Las cosas asociadas al futuro'),
        ('e', 'El lugar'),
    ), label="Pregunta 11 - Piensa en algo importante que va a suceder en el futuro. Marca las que fueron parte de tu "
             "pensamiento")

    question_twelve = Multiple(choices=(
        ('a', 'Alguien me alaba'),
        ('b', 'Veo a la gente usando los resultados de lo que hice'),
        ('c', 'Me siento bien'),
        ('d', 'Se que alcancé los estándares que yo mismo me puse'),
        ('e', 'Escucho a los demás hablando del éxito que logré<'),
        ('f', 'Tengo un efecto de buena sensación')
    ), label="Pregunta 12 - ¿Cómo sabes que hiciste un buen trabajo?")

    question_thirteen = Multiple(choices=(
        ('a', 'La gente alrededor de mí está feliz'),
        ('b', 'Me siento feliz conmigo mismo'),
        ('c', 'Tengo espacio y tiempo para mí'),
        ('d', 'Otras personas están complacidas con lo que estoy haciendo'),
        ('e', 'Reconozco el efecto que estoy produciendo en los eventos a mi alrededor'),
        ('f', 'Tengo una buena sensación')
    ), label="Pregunta 13 - ¿Cómo sabes que estás disfrutando de algo?")

    question_fourteen = Multiple(choices=(
        ('a', 'Necesitaría ver la idea funcionando'),
        ('b', 'Alguien me la tendría que explicar'),
        ('c', 'Necesitaría probarla'),
        ('d', 'Tendría que ver la idea graficada de alguna manera'),
        ('e', 'Me gustaría discutirla a fondo'),
        ('f', 'Me gustaría hacer algún experimento práctico'),
        ('g', 'Necesitaría tiempo para pensarlo bien'),
        ('h', 'Necesitaría que me la expliquen varias veces'),
        ('i', 'Me gustaría conocer los detalles'),
    ), label="Pregunta 14 - ¿Qué tendría que ser verdad para que yo esté convencido de una nueva idea?")
