from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=64)
    task = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
