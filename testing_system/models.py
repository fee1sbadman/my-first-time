from django.db import models

# Create your models here.


class Discipline(models.Model):
    name = models.CharField(max_length = 30)
    info = models.TextField
    

    def __str__(self):
        return self.name


class Test(models.Model):
    Discipline = models.ForeignKey(Discipline, on_delete = models.CASCADE)
    name = models.CharField(max_length=30)
    info = models.TextField
    

    def __str__(self):
        return self.name


class Question(models.Model):
    Test = models.ForeignKey(Test, on_delete = models.CASCADE)
    name = models.TextField()
    answer1 = models.TextField
    answer1 = models.TextField
    answer1 = models.TextField
    answer1 = models.TextField
    right_answer = models.IntegerField()
  

    def __str__(self):
        return self.name

    