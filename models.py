from django.db import models

# Create your models here.
class Info(models.Model):
    school_list = (
        (1, '서강대학교'),
    )
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    birthday = models.DateField()
    tel = models.CharField(max_length=11)
    school = models.PositiveIntegerField(choices=school_list)
    active = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username
