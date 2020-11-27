from django.db import models

# Create your models here.


class Candidate(models.Model):
    name = models.CharField(verbose_name="Nombre Completo", max_length=120)
    email = models.EmailField(verbose_name="Correo Electrónico", unique=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} - {self.email}'


class Polls(models.Model):
    author = models.CharField(max_length=120, verbose_name="Emisor de la encuesta", null=True)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, verbose_name="Candidato", null=True)
    # TODO random_link = models.URLField(verbose_name="Link de la encuesta", unique=True, null=True)
    purpose = models.CharField(max_length=200, null=True)
    question_one = models.CharField(max_length=10, null=True, blank=True,
                                    verbose_name="Piensa en hacer ejercicio: ¿Para qué lo haría?")
    question_two = models.CharField(max_length=10, null=True, blank=True,
                                    verbose_name="Cuando piensas en cambiar de trabajo ¿En cuáles de los siguientes aspectos piensas?")
    question_three = models.CharField(max_length=10, null=True, blank=True,
                                      verbose_name="Cuando decido irme de vacaciones: ¿Qué hago?")

    question_four = models.CharField(max_length=10, null=True, blank=True,
                                     verbose_name="Piensa que estás en el proceso de comprar algo. ¿Cuál o cuáles de las siguientes cosas haces?")
    question_five = models.CharField(max_length=10, null=True, blank=True,
                                     verbose_name="En una conversación. ¿Cuáles de los siguientes aspectos aplica a ti?")
    question_six = models.CharField(max_length=10, null=True, blank=True,
                                    verbose_name="¿Cuáles de las siguientes son carecterísticas que corresponden a tu persona")
    question_seven = models.CharField(max_length=10, null=True, blank=True,
                                      verbose_name="Piensa en la mejor comida que haz tenido. ¿En qué estás pensando?")
    question_eight = models.CharField(max_length=10,
                                      verbose_name="Piensa en cómo te gusta pasar el tiempo. ¿Piensas en?", null=True,
                                      blank=True, )
    question_nine = models.CharField(max_length=10, null=True, blank=True,
                                     verbose_name="Piensa en algo importante que va a suceder en el futuro. Marca las que fueron parte de tu pensamiento")
    question_ten = models.CharField(max_length=10, null=True, blank=True,
                                    verbose_name="¿Cómo sabes que hiciste un buen trabajo?")
    question_eleven = models.CharField(max_length=10, null=True, blank=True,
                                       verbose_name="¿Cómo sabes que estás disfrutando de algo?")
    question_twelve = models.CharField(max_length=10, null=True, blank=True,
                                       verbose_name="¿Qué tendría que ser verdad para que yo esté convencido de una nueva idea?")

    def __str__(self):
        return f'{self.id} - {self.author} - {self.candidate.name}'


class AnsweredPolls(models.Model):
    poll = models.ForeignKey(Polls, on_delete=models.CASCADE)
    file = models.FileField(verbose_name="Descargables", upload_to='answered/')

    def __str__(self):
        return self.poll.candidate.name
