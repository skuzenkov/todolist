from django.db import models


# Create your models here.

class Todo(models.Model):  # наследование models, модель:  Model
    objects = False
    title = models.CharField('Название задания', max_length=100)  # поле, каждое поле представленно экзепляром класса Field (сюда мы пишем название задач)
    is_complete = models.BooleanField('Отложено', default=True) # заверешение задание
    scores = models.IntegerField(default=0)




    def __str__(self):
        return self.title
