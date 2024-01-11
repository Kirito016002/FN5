from django.db import models

class Make_trip(models.Model):
    pick_up_location = models.CharField(max_length=255)
    drop_off_location = models.CharField(max_length=255)
    pick_up_date = models.DateField()
    drop_off_date = models.DateField()
    pick_up_time = models.TimeField()
