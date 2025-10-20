from django.db import models

# Create your models here.

class ZooBooking(models.Model):

    booking_id = models.AutoField(primary_key=True, editable=False)
    zoo_user_id = models.ForeignKey(ZooUser, on_delete=models.CASCADE)
    zoo_booking_date = models.DateField(auto_now_add=True)
    zoo_booking_date_arrive = models.Datefield()
    zoo_booking_adults =  models.IntegerField(default=0)
    zoo_booking_children = models.IntegerField(default=0)
    zoo_booking_oap = models.Integerfield(default=0)
    zoo_total_cost = models.FloatField(default=0)

class ZooUser(AbsractUser):
    address = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=14, blank=True)
    icon = models.CharField(max_length=64, default="lion")
