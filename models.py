from django.db import models

# Create your models here.


class Info(models.Model):
    school_list = (
        (1, '서강대학교'),
        (2, '연세대학교'),
        (3, '가천대학교'),
        (4, '이화여자대학교'),
        (5, '울산대학교'),
        (6, '인천대학교'),
        (7, '서울예술대학교'),
        (8, '가톨릭대학교'),
        (9, '한신대학교'),
        (10, '국민대학교'),
        (11, '서울과학기술대학교'),
        (12, '계원예술대학교'),
        (13, '서울대학교'),
        (14, '홍익대학교'),
        (15, '숭실대학교'),
        (16, '순천향대학교'),
        (17, '동덕여자대학교'),
    )
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    birthday = models.DateField()
    tel = models.CharField(max_length=11)
    school = models.PositiveIntegerField(choices=school_list)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
