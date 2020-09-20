from django.db import models


# Create your models here.

class User(models.Model):
    GENDER_CHOICES = [
        ("USA/LA", "AMERICA/LOS_ANGELS"),
        ("AS/WB", "ASIA/KOLKATA")
    ]
    id = models.AutoField(primary_key=True)
    real_name = models.CharField(max_length=100, blank=True)
    time_zone = models.CharField(max_length=50, choices=GENDER_CHOICES)

    class Meta:
        verbose_name_plural = "user"

    def __str__(self):
        return self.real_name


class ActivityPeriod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        verbose_name_plural = "activity_period"

    def __str__(self):
        return str(self.start_time and self.end_time)
