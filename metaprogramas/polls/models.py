from django.db import models


class Candidates(models.Model):

    name = models.CharField(max_length=120, verbose_name="Nombre", null=True)
    email = models.EmailField(unique=True, null=True)
    phone = models.CharField(max_length=10, verbose_name="Número de Teléfono", null=True)

    class Meta:
        verbose_name = "Candidato"
        verbose_name_plural = "Candidatos"

    def __str__(self):
        return self.email


class Polls(models.Model):

    candidate = models.ManyToManyField(Candidates)
    url_form = models.URLField(verbose_name="Link", null=True)
    creator = models.CharField(max_length=20, default="Admin")
    email_creator = models.EmailField(null=True)

    class Meta:
        verbose_name = "Encuesta"
        verbose_name_plural = "Encuestas"

    def __str__(self):
        return self.creator


class AnsweredPolls(models.Model):

    # poll_id = models.ForeignKey(Polls, on_delete=models.CASCADE)
    answers = models.JSONField(null=True)

    class Meta:
        verbose_name = "Encuesta Respondida"
        verbose_name_plural = "Encuestas Respondidas"

    def __str__(self):
        return str(self.id)
