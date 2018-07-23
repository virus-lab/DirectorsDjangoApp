from django.db import models

# Create your models here.


class Info(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    birthday = models.DateField()
    tel_prefix = models.CharField(max_length=3)
    tel_space1 = models.CharField(max_length=4)
    tel_space2 = models.CharField(max_length=4)
    school = models.ForeignKey('directors.School', on_delete=models.CASCADE)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class School(models.Model):
    name = models.CharField(max_length=15)


class Position(models.Model):
    name = models.CharField(max_length=15)
    group = models.ForeignKey('auth.Group', on_delete=models.CASCADE)


class Season(models.Model):
    quarter_list = (
        (1, '상반기'),
        (2, '하반기'),
    )
    year = models.DateField()
    quarter = models.PositiveIntegerField(choices=quarter_list)


class History(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    position = models.ForeignKey('directors.History', on_delete=models.CASCADE)
    season = models.ForeignKey('directors.Season', on_delete=models.CASCADE)
